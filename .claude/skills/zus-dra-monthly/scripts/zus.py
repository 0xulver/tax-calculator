#!/usr/bin/env python3
"""ZUS ePłatnik automation helpers (Dojo/dijit + iframe aware).

Connects to the debug Chrome started by setup-browser.sh and exposes the
low-level operations needed for the monthly DRA flow. Run with the mise python
that has playwright:  ~/.local/share/mise/installs/python/latest/bin/python

Subcommands:
  status                         print active page URL + title
  shot PATH [--full]             screenshot (viewport, or --full page)
  clip PATH X Y W H              screenshot a rectangle (readable crops)
  click "LABEL"                  click a dijit button by accessible name (topmost visible)
  dialog "LABEL"                 click a button scoped to the visible modal dialog
  menu "TEXT"                    click a left-nav / menu item by text
  radio IDX                      check the Nth radio input
  audit                          list visible text fields with label + error flag
  get "ROW LABEL"                read a field's value by its row label
  set "ROW LABEL" "VALUE"        type VALUE into the field in that labelled row
  frames                         list frames
  fetch-pdf DEST                 save the document PDF served at downloadFile.npi

Dojo gotchas baked in:
  * dijit buttons expose text via ARIA role / .dijitButtonText, NOT plain text;
    the real <input> is moved off-screen (class dijitOffScreen) — never click it.
  * Modal underlays intercept clicks; dialog buttons must be clicked dialog-scoped.
  * The opened form viewer lives in an iframe (url contains dokumentySformalizowane).
  * Printing renders client-side; the real PDF is fetched from downloadFile.npi.
"""
import os, sys, time, base64
from playwright.sync_api import sync_playwright

PORT = os.environ.get("ZUS_PORT", "9224")
CDP = f"http://localhost:{PORT}"


def pick_page(ctx):
    for pg in ctx.pages:
        if "eplMain" in pg.url:
            return pg
    for pg in ctx.pages:
        if "zus.pl" in pg.url:
            return pg
    return ctx.pages[-1] if ctx.pages else ctx.new_page()


def dojo_click(pg, label):
    """Click a dijit button by accessible name; fallback to its text span."""
    loc = pg.get_by_role("button", name=label, exact=True)
    best = None
    for i in range(loc.count()):
        e = loc.nth(i)
        try:
            if e.is_visible() and e.is_enabled():
                y = (e.bounding_box() or {}).get("y", 1e9)
                if y is not None and y >= 0 and (best is None or y < best[0]):
                    best = (y, e)
        except Exception:
            pass
    if best:
        best[1].click(); return True
    spans = pg.locator(".dijitButtonText").filter(has_text=label)
    for i in range(spans.count()):
        e = spans.nth(i)
        if e.is_visible():
            e.scroll_into_view_if_needed(); e.click(); return True
    return False


def dialog_click(pg, label):
    for d in [pg.locator(".dijitDialog").nth(i) for i in range(pg.locator(".dijitDialog").count())]:
        try:
            if not d.is_visible():
                continue
            b = d.get_by_role("button", name=label, exact=True)
            if b.count() and b.first.is_visible():
                b.first.click(); return True
        except Exception:
            pass
    return False


def row_input(pg, row_label):
    """The first text input in the table row whose label contains row_label."""
    row = pg.locator("tr", has_text=row_label).first
    return row.locator("input[type=text]").last


def main():
    if len(sys.argv) < 2:
        print(__doc__); return
    cmd = sys.argv[1]
    with sync_playwright() as p:
        b = p.chromium.connect_over_cdp(CDP)
        ctx = b.contexts[0]
        pg = pick_page(ctx)
        pg.bring_to_front()

        if cmd == "status":
            print("URL:", pg.url); print("TITLE:", pg.title())

        elif cmd == "shot":
            path = sys.argv[2]
            full = "--full" in sys.argv
            pg.screenshot(path=path, full_page=full); print("saved", path)

        elif cmd == "clip":
            path, x, y, w, h = sys.argv[2], *map(float, sys.argv[3:7])
            pg.screenshot(path=path, clip={"x": x, "y": y, "width": w, "height": h})
            print("saved", path)

        elif cmd == "click":
            print("clicked" if dojo_click(pg, sys.argv[2]) else "NOT FOUND", sys.argv[2])
            time.sleep(2)

        elif cmd == "dialog":
            print("clicked" if dialog_click(pg, sys.argv[2]) else "NOT FOUND", "(dialog)", sys.argv[2])
            time.sleep(2)

        elif cmd == "menu":
            node = pg.get_by_text(sys.argv[2], exact=True)
            ok = False
            for i in range(node.count()):
                if node.nth(i).is_visible():
                    node.nth(i).click(); ok = True; break
            print("clicked" if ok else "NOT FOUND", "(menu)", sys.argv[2]); time.sleep(2)

        elif cmd == "radio":
            r = pg.locator("input[type=radio]").nth(int(sys.argv[2]))
            try:
                r.check(timeout=4000)
            except Exception:
                r.click(force=True)
            for i in range(pg.locator("input[type=radio]").count()):
                print(i, "checked=", pg.locator("input[type=radio]").nth(i).is_checked())

        elif cmd == "audit":
            rows = pg.evaluate(r"""()=>{const o=[];for(const inp of document.querySelectorAll('input[type=text]')){
              const r=inp.getBoundingClientRect(); if(!(r.width>0&&r.top>-100)) continue;
              let lab=''; const tr=inp.closest('tr'); if(tr){const c=tr.querySelector('td,th'); if(c) lab=(c.innerText||'').trim().slice(0,60);}
              let err=false,n=inp; for(let k=0;k<5&&n;k++){if(n.className&&/Error/i.test(n.className)){err=true;break;}n=n.parentElement;}
              if(inp.getAttribute('aria-invalid')==='true') err=true;
              o.push({v:inp.value,lab,err});} return o;}""")
            for r in rows:
                print(("ERR " if r["err"] else "    ") + repr(r["v"].replace("\xa0", " ")), "|", r["lab"])

        elif cmd == "get":
            print(repr(row_input(pg, sys.argv[2]).input_value()))

        elif cmd == "set":
            inp = row_input(pg, sys.argv[2])
            inp.scroll_into_view_if_needed(); inp.click()
            inp.press("Control+a"); inp.press("Delete")
            inp.type(sys.argv[3], delay=30); inp.press("Tab"); time.sleep(0.8)
            print("now:", repr(inp.input_value()))

        elif cmd == "frames":
            for f in pg.frames:
                print(f.url[:120])

        elif cmd == "fetch-pdf":
            dest = sys.argv[2]
            fr = [f for f in pg.frames if "downloadFile.npi" in f.url]
            if not fr:
                print("NO downloadFile.npi frame — open the doc and click Drukuj first"); b.close(); return
            url = fr[0].url.split("#")[0]
            b64 = fr[0].evaluate(
                "async(u)=>{const r=await fetch(u);const bl=await r.blob();"
                "return await new Promise(res=>{const f=new FileReader();"
                "f.onload=()=>res(f.result.split(',')[1]);f.readAsDataURL(bl);});}", url)
            data = base64.b64decode(b64)
            if data[:4] != b"%PDF":
                print("not a PDF, head=", data[:8]); b.close(); return
            with open(dest, "wb") as f:
                f.write(data)
            print("SAVED", dest, len(data), "bytes")

        else:
            print("unknown cmd", cmd)
        b.close()


if __name__ == "__main__":
    main()

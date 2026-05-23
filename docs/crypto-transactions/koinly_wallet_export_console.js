/*
Paste this into DevTools Console while logged in at:
https://app.koinly.io/p/wallets

Workflow:
1. Paste this snippet. It starts automatically.
2. Reload the Koinly wallets page and wait until the wallet list is loaded.
3. Run: koinlyWalletExport.download()

The downloaded JSON can be saved under:
private/evidence/koinly/wallets/
*/

(() => {
  const ADDRESS_PATTERNS = [
    /\b0x[a-fA-F0-9]{64}\b/g,
    /\b0x[a-fA-F0-9]{40}\b/g,
    /\bbc1[ac-hj-np-z02-9]{11,71}\b/gi,
    /\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b/g,
    /\b(?:cosmos|terra|osmo|juno|akash|secret|kujira|stride|celestia)1[0-9a-z]{38,80}\b/gi,
    /\b[1-9A-HJ-NP-Za-km-z]{45,60}\b/g,
    /\b[1-9A-HJ-NP-Za-km-z]{32,44}\b/g,
  ];

  const MAX_CAPTURED_BODY_BYTES = 5_000_000;
  const walletExport = {
    startedAt: new Date().toISOString(),
    pageUrl: window.location.href,
    userAgent: window.navigator.userAgent,
    domSnapshots: [],
    network: [],
    installed: false,
  };

  function extractAddresses(text) {
    const found = new Set();
    for (const pattern of ADDRESS_PATTERNS) {
      pattern.lastIndex = 0;
      for (const match of text.matchAll(pattern)) {
        found.add(match[0]);
      }
    }
    return [...found];
  }

  function compactText(value) {
    return String(value || "").replace(/\s+/g, " ").trim();
  }

  function visibleRows() {
    const selectors = [
      "tr",
      "[role='row']",
      "[data-testid*='wallet' i]",
      "[class*='wallet' i]",
      "li",
      "a[href*='wallet']",
    ];

    const elements = new Set();
    for (const selector of selectors) {
      for (const element of document.querySelectorAll(selector)) {
        const text = compactText(element.innerText || element.textContent);
        if (!text) continue;
        if (/wallet|exchange|blockchain|address|0x|bc1|cosmos1|terra1/i.test(text)) {
          elements.add(element);
        }
      }
    }

    return [...elements].map((element) => {
      const text = compactText(element.innerText || element.textContent);
      const links = [...element.querySelectorAll("a[href]")].map((link) => ({
        text: compactText(link.innerText || link.textContent),
        href: link.href,
      }));
      return {
        text,
        addresses: extractAddresses(text),
        links,
      };
    });
  }

  function snapshotDom() {
    const pageText = compactText(document.body.innerText || document.body.textContent);
    const snapshot = {
      capturedAt: new Date().toISOString(),
      url: window.location.href,
      title: document.title,
      pageAddresses: extractAddresses(pageText),
      rows: visibleRows(),
    };
    walletExport.domSnapshots.push(snapshot);
    return snapshot;
  }

  function relevantResponse(url, text, contentType) {
    const haystack = `${url}\n${contentType || ""}\n${text.slice(0, 5000)}`;
    return /wallet|account|address|blockchain|exchange|integration/i.test(haystack);
  }

  async function captureFetchResponse(url, response) {
    const contentType = response.headers.get("content-type") || "";
    if (!/json|text|javascript/i.test(contentType)) return;

    const clone = response.clone();
    const text = await clone.text();
    if (!relevantResponse(url, text, contentType)) return;

    walletExport.network.push({
      capturedAt: new Date().toISOString(),
      transport: "fetch",
      url,
      status: response.status,
      contentType,
      addresses: extractAddresses(text),
      bodyTruncated: text.length > MAX_CAPTURED_BODY_BYTES,
      body: text.slice(0, MAX_CAPTURED_BODY_BYTES),
    });
  }

  function installFetchCapture() {
    if (window.__koinlyWalletExportOriginalFetch) return;
    window.__koinlyWalletExportOriginalFetch = window.fetch;
    window.fetch = async (...args) => {
      const response = await window.__koinlyWalletExportOriginalFetch(...args);
      const url = typeof args[0] === "string" ? args[0] : args[0]?.url || "";
      captureFetchResponse(url, response).catch((error) => {
        walletExport.network.push({
          capturedAt: new Date().toISOString(),
          transport: "fetch",
          url,
          error: String(error),
        });
      });
      return response;
    };
  }

  function installXhrCapture() {
    if (window.__koinlyWalletExportOriginalXhrOpen) return;

    window.__koinlyWalletExportOriginalXhrOpen = XMLHttpRequest.prototype.open;
    window.__koinlyWalletExportOriginalXhrSend = XMLHttpRequest.prototype.send;

    XMLHttpRequest.prototype.open = function open(method, url, ...rest) {
      this.__koinlyWalletExportUrl = url;
      return window.__koinlyWalletExportOriginalXhrOpen.call(this, method, url, ...rest);
    };

    XMLHttpRequest.prototype.send = function send(...args) {
      this.addEventListener("load", function onLoad() {
        const url = String(this.__koinlyWalletExportUrl || "");
        const contentType = this.getResponseHeader("content-type") || "";
        const text = typeof this.responseText === "string" ? this.responseText : "";
        if (!text || !relevantResponse(url, text, contentType)) return;

        walletExport.network.push({
          capturedAt: new Date().toISOString(),
          transport: "xhr",
          url,
          status: this.status,
          contentType,
          addresses: extractAddresses(text),
          bodyTruncated: text.length > MAX_CAPTURED_BODY_BYTES,
          body: text.slice(0, MAX_CAPTURED_BODY_BYTES),
        });
      });
      return window.__koinlyWalletExportOriginalXhrSend.apply(this, args);
    };
  }

  function download() {
    snapshotDom();
    const blob = new Blob([JSON.stringify(walletExport, null, 2)], {
      type: "application/json",
    });
    const link = document.createElement("a");
    const date = new Date().toISOString().replace(/[:.]/g, "-");
    link.href = URL.createObjectURL(blob);
    link.download = `koinly-wallet-export-${date}.json`;
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(link.href);
  }

  function start() {
    installFetchCapture();
    installXhrCapture();
    walletExport.installed = true;
    snapshotDom();
    return "Koinly wallet export capture is active. Reload the wallets page, wait for it to finish loading, then run koinlyWalletExport.download().";
  }

  window.koinlyWalletExport = {
    start,
    snapshotDom,
    download,
    data: walletExport,
  };

  console.log(start());
})();

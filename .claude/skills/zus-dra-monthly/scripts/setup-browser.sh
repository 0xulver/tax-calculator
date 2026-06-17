#!/usr/bin/env bash
# Ensure a CDP-debuggable Chrome is running on the dedicated ZUS profile.
#
# Strategy (reuse > relaunch > recreate):
#   1. If CDP is already up on the port -> reuse the live session (do nothing).
#   2. Else if the dedicated profile dir exists -> relaunch Chrome on it.
#   3. Else (first run) -> recreate it by copying the real Default profile.
#
# Chrome refuses --remote-debugging-port on the *default* user-data-dir, so we
# always use a dedicated copy. ZUS sessions expire fast, so you will re-auth via
# Profil Zaufany each month regardless — that is expected, not a failure.
#
# Usage: setup-browser.sh [PORT]   (default port 9224)
set -u
PORT="${1:-9224}"
PROFILE="$HOME/.chrome-zus-copy"          # persistent dedicated debug profile
SRC="$HOME/.config/google-chrome"          # real profile (source for first copy)
CHROME="$(command -v google-chrome || command -v chromium || command -v chromium-browser)"

cdp_up() { curl -s "http://localhost:${PORT}/json/version" >/dev/null 2>&1; }

if cdp_up; then
  echo "REUSE: CDP already live on :${PORT}"
  exit 0
fi

# First run: build the dedicated profile from Default (needs main Chrome closed
# so cookie/Login Data DBs aren't locked). Keyring decrypts the copied cookies.
if [ ! -d "$PROFILE/Default" ]; then
  echo "FIRST RUN: creating dedicated profile copy at $PROFILE"
  if pgrep -f "google-chrome.*--user-data-dir=$SRC" >/dev/null 2>&1 || \
     ( pgrep -x chrome >/dev/null 2>&1 && ! pgrep -f "remote-debugging-port" >/dev/null 2>&1 ); then
    echo "  >> Close your MAIN Chrome first (it locks the profile), then re-run." >&2
    exit 2
  fi
  mkdir -p "$PROFILE"
  cp -a "$SRC/Local State" "$PROFILE/Local State"
  rsync -a --exclude 'Cache' --exclude 'Code Cache' --exclude 'GPUCache' \
        --exclude 'DawnCache' --exclude 'GraphiteDawnCache' \
        --exclude 'Service Worker/CacheStorage' --exclude 'IndexedDB' \
        --exclude 'File System' "$SRC/Default/" "$PROFILE/Default/"
fi

# Clear any stale singleton lock and launch on the dedicated profile.
rm -f "$PROFILE/SingletonLock" "$PROFILE/SingletonSocket" "$PROFILE/SingletonCookie" 2>/dev/null
nohup "$CHROME" \
  --remote-debugging-port="$PORT" \
  --user-data-dir="$PROFILE" \
  --profile-directory=Default \
  --no-first-run --no-default-browser-check \
  "https://www.zus.pl/ezus/obszar-platnika/platnik/dashboard" \
  >/tmp/chrome-zus.log 2>&1 &
echo "LAUNCHED Chrome on $PROFILE (pid $!), waiting for CDP..."
for i in $(seq 1 15); do sleep 1; cdp_up && { echo "CDP up on :${PORT}"; exit 0; }; done
echo "CDP did not come up; see /tmp/chrome-zus.log" >&2
exit 1

#!/usr/bin/env bash
# ABOUTME: Captures uniform hero screenshots of the four designs with headless Chrome
# ABOUTME: (1440x900 desktop, 390x844 mobile) into site/shots/ as WebP for the sprint page.
set -euo pipefail
cd "$(dirname "$0")/.."

CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
[ -x "$CHROME" ] || { echo "Chrome not found at $CHROME"; exit 1; }
command -v magick >/dev/null || { echo "magick not found (brew install imagemagick)"; exit 1; }

DIRS=(01-shotgun-house 02-front-porch 03-shop-sign 04-combined)
PORT=${PORT:-8797}
mkdir -p site/shots
TMP=$(mktemp -d)

python3 -m http.server "$PORT" --bind 127.0.0.1 >/dev/null 2>&1 &
SERVER=$!
cleanup() { kill "$SERVER" 2>/dev/null || true; pkill -f "user-data-dir=$TMP" 2>/dev/null || true; rm -rf "$TMP"; }
trap cleanup EXIT
sleep 1

# Chrome writes the screenshot and then tends to hang on exit, so wait for the
# file to appear and then kill the browser rather than waiting for it to quit.
shoot() { # dir width height scale label
  local d=$1 w=$2 h=$3 scale=$4 label=$5
  local out="$TMP/$d-$label.png"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --no-first-run --no-default-browser-check \
    --user-data-dir="$TMP/profile-$d-$label" \
    --window-size="$w,$h" --force-device-scale-factor="$scale" \
    --screenshot="$out" "http://127.0.0.1:$PORT/designs/$d/" >/dev/null 2>&1 &
  local pid=$!
  for _ in $(seq 1 60); do [ -s "$out" ] && break; sleep 1; done
  sleep 1; kill "$pid" 2>/dev/null || true; wait "$pid" 2>/dev/null || true
  [ -s "$out" ] || { echo "FAILED $d $label"; return 1; }
  magick "$out" -quality 82 "site/shots/$d-$label.webp"
  echo "shot $d $label $(magick identify -format '%wx%h' "site/shots/$d-$label.webp")"
}

for d in "${DIRS[@]}"; do
  [ -f "designs/$d/index.html" ] || { echo "skip $d: no index.html"; continue; }
  shoot "$d" 1440 900 1 desktop
  shoot "$d" 390 844 2 mobile
done

#!/usr/bin/env bash
set -euo pipefail
mkdir -p build
cp app.py requirements.txt build/
python3 -m compileall -q build/app.py
printf 'Application build: %s\n' "$(git rev-parse --short HEAD)" > build/build-info.txt

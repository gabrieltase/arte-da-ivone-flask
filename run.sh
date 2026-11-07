#!/usr/bin/env bash
cd "$(dirname "$0")"
[ -d venv ] || python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
[ -f .env ] || cp .env.exemplo .env
(sleep 2; xdg-open http://127.0.0.1:5000/ 2>/dev/null || open http://127.0.0.1:5000/ 2>/dev/null) &
python -m flask --app app run --debug

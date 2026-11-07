@echo off
cd /d %~dp0
if not exist venv python -m venv venv
call venv\Scripts\activate
python -m pip install -r requirements.txt
if not exist .env copy .env.exemplo .env
start "" http://127.0.0.1:5000/
python -m flask --app app run --debug

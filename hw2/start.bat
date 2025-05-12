@echo off
REM
python -m venv venv

REM
call venv\Scripts\activate

REM
pip install -r requirements.txt

REM
python main.py

REM
pause

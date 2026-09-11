@echo off
cd /d C:\Users\PC_User\terminal_search_app
start "" pythonw app2.py
timeout /t 2 >nul
start "" http://127.0.0.1:5000
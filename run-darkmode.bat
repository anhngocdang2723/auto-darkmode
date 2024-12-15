@echo off
:: Kiểm tra và kích hoạt môi trường ảo
if not defined VIRTUAL_ENV (
    call .\venv\Scripts\activate.bat
)

:: Chạy script Python
.\venv\Scripts\python.exe src/darkmode.py

pause

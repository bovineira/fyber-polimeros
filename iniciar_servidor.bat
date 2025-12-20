@echo off
chcp 65001 >nul
echo ============================================================
echo   SERVIDOR HTTP LOCAL - FYBER POLÍMEROS
echo ============================================================
echo.
echo Iniciando servidor na porta 8000...
echo.
cd /d "%~dp0"
python server.py
pause

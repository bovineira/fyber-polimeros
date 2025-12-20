# Script PowerShell para iniciar o servidor HTTP
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  SERVIDOR HTTP LOCAL - FYBER POLIMEROS" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Iniciando servidor na porta 8000..." -ForegroundColor Yellow
Write-Host ""

# Parar qualquer servidor anterior
Get-Process python -ErrorAction SilentlyContinue | Where-Object {
    $_.CommandLine -like "*server.py*"
} | Stop-Process -Force -ErrorAction SilentlyContinue

Start-Sleep -Seconds 1

# Iniciar o servidor
python server.py

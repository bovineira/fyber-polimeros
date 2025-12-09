@echo off
chcp 65001 > nul
echo ========================================
echo Gerando Páginas HTML dos Produtos Novos
echo ========================================
echo.
echo Este script vai criar as páginas HTML de todos os produtos novos.
echo.
echo ATENÇÃO: Para funcionar, você precisa ter Python instalado!
echo.
echo Se NÃO tiver Python instalado:
echo 1. Baixe em: https://www.python.org/downloads/
echo 2. Durante instalação, marque "Add Python to PATH"
echo 3. Reinicie o terminal
echo 4. Execute este script novamente
echo.
pause
echo.
echo Executando gerar_produtos.py...
python gerar_produtos.py
echo.
if %ERRORLEVEL% EQU 0 (
    echo ========================================
    echo ✓ Sucesso! Todas as páginas foram criadas!
    echo ========================================
) else (
    echo ========================================
    echo ✗ Erro! Python não encontrado ou erro na execução.
    echo ========================================
    echo.
    echo Instale Python em: https://www.python.org/downloads/
)
echo.
pause


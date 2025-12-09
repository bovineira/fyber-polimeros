@echo off
chcp 65001 > nul
echo ========================================
echo Copiando instruções para todas as pastas de produtos
echo ========================================
echo.

set "origem=assets\img\produtos\fibra-de-vidro\tecido-peel-ply\LEIA-ME.txt"

REM Fibra de Vidro
copy "%origem%" "assets\img\produtos\fibra-de-vidro\tecido-pranchas-stand-up\" > nul 2>&1
copy "%origem%" "assets\img\produtos\fibra-de-vidro\tecido-multiaxial\" > nul 2>&1
copy "%origem%" "assets\img\produtos\fibra-de-vidro\manta-450\" > nul 2>&1

REM Equipamentos
copy "%origem%" "assets\img\produtos\equipamentos-acessorios\fita-crepe\" > nul 2>&1
copy "%origem%" "assets\img\produtos\equipamentos-acessorios\estopas\" > nul 2>&1
copy "%origem%" "assets\img\produtos\equipamentos-acessorios\mascaras\" > nul 2>&1
copy "%origem%" "assets\img\produtos\equipamentos-acessorios\rolos-de-la\" > nul 2>&1
copy "%origem%" "assets\img\produtos\equipamentos-acessorios\pinceis\" > nul 2>&1
copy "%origem%" "assets\img\produtos\equipamentos-acessorios\lixas\" > nul 2>&1
copy "%origem%" "assets\img\produtos\equipamentos-acessorios\bucha-celeron\" > nul 2>&1
copy "%origem%" "assets\img\produtos\equipamentos-acessorios\roletes-fura-bolha\" > nul 2>&1
copy "%origem%" "assets\img\produtos\equipamentos-acessorios\picador-roving\" > nul 2>&1
copy "%origem%" "assets\img\produtos\equipamentos-acessorios\aplicador-de-massa\" > nul 2>&1

REM Resinas
copy "%origem%" "assets\img\produtos\resinas\resinas-ester-vinilicas\" > nul 2>&1
copy "%origem%" "assets\img\produtos\resinas\resinas-isoftalicas-npg\" > nul 2>&1
copy "%origem%" "assets\img\produtos\resinas\resina-isoftalica\" > nul 2>&1
copy "%origem%" "assets\img\produtos\resinas\resina-de-marmores\" > nul 2>&1
copy "%origem%" "assets\img\produtos\resinas\resina-ortoftalica\" > nul 2>&1
copy "%origem%" "assets\img\produtos\resinas\resina-epoxi\" > nul 2>&1

REM Gel Coats
copy "%origem%" "assets\img\produtos\gel-coats\gel-para-molde\" > nul 2>&1
copy "%origem%" "assets\img\produtos\gel-coats\gel-ester-vinilico\" > nul 2>&1
copy "%origem%" "assets\img\produtos\gel-coats\gel-coat-ortoftalico\" > nul 2>&1
copy "%origem%" "assets\img\produtos\gel-coats\gel-coat-isoftalico\" > nul 2>&1

REM Outras categorias
copy "%origem%" "assets\img\produtos\silicones\borracha-silicone-molde\" > nul 2>&1
copy "%origem%" "assets\img\produtos\material-de-nucleo\divinycell\" > nul 2>&1
copy "%origem%" "assets\img\produtos\catalisadores-aceleradores\acelerador-de-cobalto\" > nul 2>&1

echo ✓ Instruções copiadas para todas as pastas de produtos
echo.
echo Agora cada pasta de produto tem um arquivo LEIA-ME.txt
echo com instruções sobre como adicionar imagens.
echo.
pause


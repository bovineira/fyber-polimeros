@echo off
chcp 65001 > nul
echo ========================================
echo Criando pastas para imagens dos produtos
echo ========================================
echo.

REM Fibra de Vidro
mkdir "assets\img\produtos\fibra-de-vidro\tecido-peel-ply" 2>nul
mkdir "assets\img\produtos\fibra-de-vidro\tecido-pranchas-stand-up" 2>nul
mkdir "assets\img\produtos\fibra-de-vidro\tecido-multiaxial" 2>nul
mkdir "assets\img\produtos\fibra-de-vidro\manta-450" 2>nul

REM Equipamentos e Acessórios
mkdir "assets\img\produtos\equipamentos-acessorios\fita-crepe" 2>nul
mkdir "assets\img\produtos\equipamentos-acessorios\estopas" 2>nul
mkdir "assets\img\produtos\equipamentos-acessorios\mascaras" 2>nul
mkdir "assets\img\produtos\equipamentos-acessorios\rolos-de-la" 2>nul
mkdir "assets\img\produtos\equipamentos-acessorios\pinceis" 2>nul
mkdir "assets\img\produtos\equipamentos-acessorios\lixas" 2>nul
mkdir "assets\img\produtos\equipamentos-acessorios\bucha-celeron" 2>nul
mkdir "assets\img\produtos\equipamentos-acessorios\roletes-fura-bolha" 2>nul
mkdir "assets\img\produtos\equipamentos-acessorios\picador-roving" 2>nul
mkdir "assets\img\produtos\equipamentos-acessorios\aplicador-de-massa" 2>nul

REM Resinas
mkdir "assets\img\produtos\resinas\resinas-ester-vinilicas" 2>nul
mkdir "assets\img\produtos\resinas\resinas-isoftalicas-npg" 2>nul
mkdir "assets\img\produtos\resinas\resina-isoftalica" 2>nul
mkdir "assets\img\produtos\resinas\resina-de-marmores" 2>nul
mkdir "assets\img\produtos\resinas\resina-ortoftalica" 2>nul
mkdir "assets\img\produtos\resinas\resina-epoxi" 2>nul

REM Gel Coats
mkdir "assets\img\produtos\gel-coats\gel-para-molde" 2>nul
mkdir "assets\img\produtos\gel-coats\gel-ester-vinilico" 2>nul
mkdir "assets\img\produtos\gel-coats\gel-coat-ortoftalico" 2>nul
mkdir "assets\img\produtos\gel-coats\gel-coat-isoftalico" 2>nul

REM Silicones
mkdir "assets\img\produtos\silicones\borracha-silicone-molde" 2>nul

REM Material de Núcleo
mkdir "assets\img\produtos\material-de-nucleo\divinycell" 2>nul

REM Catalisadores e Aceleradores
mkdir "assets\img\produtos\catalisadores-aceleradores\acelerador-de-cobalto" 2>nul

echo.
echo ========================================
echo ✓ Pastas criadas com sucesso!
echo ========================================
echo.
echo INSTRUÇÕES:
echo.
echo 1. Coloque as imagens dos produtos nas pastas:
echo    assets\img\produtos\[categoria]\[produto]\
echo.
echo 2. Nomeie as imagens como:
echo    - 1.jpg, 2.jpg, 3.jpg, etc.
echo    - Ou use nomes descritivos: frente.jpg, lado.jpg, etc.
echo.
echo 3. Formatos suportados: .jpg, .jpeg, .png, .webp
echo.
echo 4. A primeira imagem será a imagem principal
echo    As demais aparecerão na galeria
echo.
echo ========================================
pause


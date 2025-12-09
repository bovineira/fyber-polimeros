# Script para criar estrutura de pastas para imagens dos produtos
# Executar no PowerShell: .\criar_pastas_produtos.ps1

Write-Host "Criando estrutura de pastas para imagens dos produtos..." -ForegroundColor Cyan

# Criar pasta base se não existir
$basePath = "assets\img\produtos"
if (-not (Test-Path $basePath)) {
    New-Item -ItemType Directory -Path $basePath -Force | Out-Null
}

# Lista de produtos organizados por categoria
$produtos = @(
    # Fibra de Vidro
    @{categoria="fibra-de-vidro"; slug="tecido-peel-ply"},
    @{categoria="fibra-de-vidro"; slug="tecido-pranchas-stand-up"},
    @{categoria="fibra-de-vidro"; slug="tecido-multiaxial"},
    @{categoria="fibra-de-vidro"; slug="manta-450"},
    
    # Equipamentos e Acessórios
    @{categoria="equipamentos-acessorios"; slug="fita-crepe"},
    @{categoria="equipamentos-acessorios"; slug="estopas"},
    @{categoria="equipamentos-acessorios"; slug="mascaras"},
    @{categoria="equipamentos-acessorios"; slug="rolos-de-la"},
    @{categoria="equipamentos-acessorios"; slug="pinceis"},
    @{categoria="equipamentos-acessorios"; slug="lixas"},
    @{categoria="equipamentos-acessorios"; slug="bucha-celeron"},
    @{categoria="equipamentos-acessorios"; slug="roletes-fura-bolha"},
    @{categoria="equipamentos-acessorios"; slug="picador-roving"},
    @{categoria="equipamentos-acessorios"; slug="aplicador-de-massa"},
    
    # Resinas
    @{categoria="resinas"; slug="resinas-ester-vinilicas"},
    @{categoria="resinas"; slug="resinas-isoftalicas-npg"},
    @{categoria="resinas"; slug="resina-isoftalica"},
    @{categoria="resinas"; slug="resina-de-marmores"},
    @{categoria="resinas"; slug="resina-ortoftalica"},
    @{categoria="resinas"; slug="resina-epoxi"},
    
    # Gel Coats
    @{categoria="gel-coats"; slug="gel-para-molde"},
    @{categoria="gel-coats"; slug="gel-ester-vinilico"},
    @{categoria="gel-coats"; slug="gel-coat-ortoftalico"},
    @{categoria="gel-coats"; slug="gel-coat-isoftalico"},
    
    # Silicones
    @{categoria="silicones"; slug="borracha-silicone-molde"},
    
    # Material de Núcleo
    @{categoria="material-de-nucleo"; slug="divinycell"},
    
    # Catalisadores e Aceleradores
    @{categoria="catalisadores-aceleradores"; slug="acelerador-de-cobalto"}
)

# Criar pastas para cada produto
$contador = 0
foreach ($produto in $produtos) {
    $produtoPath = "$basePath\$($produto.categoria)\$($produto.slug)"
    
    if (-not (Test-Path $produtoPath)) {
        New-Item -ItemType Directory -Path $produtoPath -Force | Out-Null
        Write-Host "[✓] Criada: $produtoPath" -ForegroundColor Green
        $contador++
    } else {
        Write-Host "[✓] Já existe: $produtoPath" -ForegroundColor Yellow
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Total de pastas criadas: $contador" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "INSTRUÇÕES:" -ForegroundColor Yellow
Write-Host "- Agora você pode colocar as imagens dos produtos nas pastas criadas" -ForegroundColor White
Write-Host "- Nomeie as imagens como: 1.jpg, 2.jpg, 3.jpg, etc." -ForegroundColor White
Write-Host "- Ou use nomes descritivos: produto-frente.jpg, produto-lado.jpg, etc." -ForegroundColor White
Write-Host "- A primeira imagem encontrada será usada como imagem principal" -ForegroundColor White
Write-Host "- As demais imagens aparecerão na galeria do produto`n" -ForegroundColor White


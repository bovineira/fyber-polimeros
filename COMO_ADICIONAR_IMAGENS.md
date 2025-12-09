# 📸 Como Adicionar Imagens aos Produtos

## 🎯 Estrutura de Pastas Criada

Cada produto agora tem sua própria pasta para imagens:

```
assets/img/produtos/
├── fibra-de-vidro/
│   ├── tecido-peel-ply/          ← Coloque as imagens aqui
│   ├── tecido-multiaxial/
│   ├── manta-450/
│   └── ...
├── resinas/
│   ├── resina-epoxi/
│   ├── resina-ortoftalica/
│   └── ...
├── gel-coats/
│   ├── gel-coat-isoftalico/
│   └── ...
└── [outras categorias]/
```

## 📝 Como Nomear as Imagens

### Opção 1: Numeração Simples (Recomendado)
```
1.jpg  ← Imagem principal (aparece primeiro)
2.jpg  ← Segunda imagem
3.jpg  ← Terceira imagem
4.jpg
...
```

### Opção 2: Nomes Descritivos
```
frente.jpg
lado.jpg
detalhe.jpg
aplicacao.jpg
embalagem.jpg
```

## 🖼️ Formatos Suportados

- ✅ `.jpg` / `.jpeg`
- ✅ `.png`
- ✅ `.webp`

## 📐 Recomendações de Tamanho

- **Imagem Principal**: 1200x900px (proporção 4:3)
- **Miniaturas**: Geradas automaticamente pelo navegador
- **Peso**: Máximo 500KB por imagem (use compressão)

## 🚀 Como Funciona

1. **Imagem Principal**: A primeira imagem encontrada (numericamente ou alfabeticamente) será exibida como imagem principal

2. **Galeria**: Se houver mais de uma imagem, miniaturas aparecerão abaixo da imagem principal

3. **Visualização em Tela Cheia**: Ao clicar na imagem principal ou nas miniaturas, abre modal com navegação

4. **Navegação**:
   - Clique nas miniaturas para trocar a imagem principal
   - Clique na imagem para abrir em tela cheia
   - Use as setas ← → para navegar no modal
   - Pressione ESC para fechar o modal

## 📋 Exemplo Prático

### Para o produto "Tecido Peel Ply":

1. Navegue até: `assets/img/produtos/fibra-de-vidro/tecido-peel-ply/`

2. Adicione suas imagens:
   ```
   1.jpg  ← Vista geral do produto
   2.jpg  ← Detalhe da textura
   3.jpg  ← Produto em uso
   4.jpg  ← Embalagem
   ```

3. Pronto! As imagens aparecerão automaticamente na página do produto

## 🔄 Regenerar Páginas (Se Necessário)

Se você fez alterações no template e quer regenerar todas as páginas:

```bash
python gerar_produtos.py
```

Para criar novas pastas de produtos:

```bash
python gerar_produtos.py --criar-pastas
```

Ou simplesmente execute:

```bash
.\criar_pastas_produtos.bat
```

## ⚠️ Importante

- **Sem imagens?** Aparecerá um placeholder com o nome do produto em gradiente azul
- **Imagens não carregam?** Verifique se o caminho e nome do arquivo estão corretos
- **Uma imagem só?** Sem problema! A galeria não aparece, só a imagem principal
- **Muitas imagens?** O sistema carrega até 10 imagens por produto

## 🎨 Dicas de Qualidade

1. **Use imagens de alta qualidade** - representam seu produto
2. **Iluminação adequada** - evite sombras duras
3. **Fundo limpo** - destaca o produto
4. **Múltiplos ângulos** - ajuda o cliente a entender melhor
5. **Contexto de uso** - mostre o produto em aplicação

## 🛠️ Troubleshooting

### Imagens não aparecem?
- Verifique se o arquivo está na pasta correta
- Confirme a extensão do arquivo (.jpg, .png, etc.)
- Verifique se o nome está correto (sem espaços ou caracteres especiais)

### Galeria não funciona?
- Verifique se há JavaScript habilitado no navegador
- Abra o console (F12) e verifique se há erros

### Imagens muito grandes/pesadas?
Use ferramentas de compressão online:
- [TinyPNG](https://tinypng.com/)
- [Compressor.io](https://compressor.io/)
- [Squoosh](https://squoosh.app/)

---

## 📞 Suporte

Se tiver dúvidas ou problemas, consulte a documentação principal no `README.md`


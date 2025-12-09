# Fyber Polímeros - Site Institucional

Site estático completo para Fyber Polímeros, pronto para upload direto em qualquer hospedagem (ex: HostGator public_html/).

## 📁 Estrutura do Projeto

```
fyber-polimeros/
├── index.html              # Página inicial
├── produtos.html           # Grid de produtos
├── produtos/               # Páginas individuais de produtos
│   ├── tecido-peel-ply.html
│   ├── resina-epoxi.html
│   └── ...
├── quem-somos.html         # Página institucional
├── contato.html            # Página de contato
├── styles.css              # Estilos globais
├── script.js               # Funcionalidades JavaScript
├── gerar_produtos.py       # Script para gerar páginas de produtos
├── criar_pastas_produtos.bat  # Script para criar pastas de imagens
├── assets/                 # Imagens e recursos
│   ├── banner-*.svg        # Banners do slideshow
│   ├── empresa.svg         # Foto da empresa
│   ├── favicon.svg         # Ícone do site
│   └── img/
│       └── produtos/       # ⭐ GALERIA DE IMAGENS DOS PRODUTOS
│           ├── fibra-de-vidro/
│           │   ├── tecido-peel-ply/
│           │   │   ├── 1.jpg       # Imagem principal
│           │   │   ├── 2.jpg       # Segunda imagem
│           │   │   └── LEIA-ME.txt # Instruções
│           │   └── ...
│           ├── resinas/
│           │   ├── resina-epoxi/
│           │   └── ...
│           └── [outras categorias]/
└── data/
    └── produtos.json       # Dados dos produtos
```

## 🚀 Como Usar

1. **Upload para Hospedagem**
   - Faça upload de toda a pasta `fyber-polimeros/` para o diretório `public_html/` da sua hospedagem
   - Ou renomeie a pasta para o nome desejado antes do upload

2. **📸 Adicionar Imagens aos Produtos** ⭐ NOVO!
   - Execute `criar_pastas_produtos.bat` para criar as pastas de imagens
   - Adicione as imagens dos produtos nas pastas: `assets/img/produtos/[categoria]/[produto]/`
   - Nomeie as imagens como: `1.jpg`, `2.jpg`, `3.jpg`, etc.
   - A primeira imagem será a principal, as demais aparecerão na galeria
   - Formatos suportados: `.jpg`, `.jpeg`, `.png`, `.webp`
   - **📖 Ver guia completo:** [COMO_ADICIONAR_IMAGENS.md](COMO_ADICIONAR_IMAGENS.md)

3. **Substituir Placeholders**
   - Substitua os arquivos `.svg` em `assets/` por imagens reais (JPG ou PNG)
   - Atualize os caminhos no HTML se necessário
   - Substitua o número do WhatsApp no link: `https://wa.me/5500000000000`
   - Atualize o telefone na página de contato

4. **Personalização**
   - Edite `gerar_produtos.py` para adicionar/remover produtos
   - Execute `python gerar_produtos.py` para regenerar as páginas
   - As páginas incluem galeria de imagens automática

## 🎨 Características

- ✅ 100% estático (sem frameworks, sem build)
- ✅ Totalmente responsivo
- ✅ Acessível (HTML semântico, foco visível, alt texts)
- ✅ Animações suaves de scroll
- ✅ Carrosséis funcionais (slideshow, benefícios, produtos)
- ✅ **Galeria de imagens por produto** ⭐ NOVO!
  - Múltiplas imagens por produto
  - Miniaturas clicáveis
  - Modal de visualização em tela cheia
  - Navegação por teclado (← → ESC)
- ✅ Todos os CTAs direcionam para WhatsApp
- ✅ Sem preços (apenas informações e contato)

## 📱 Links WhatsApp

Todos os botões principais usam o link placeholder:
```
https://wa.me/5500000000000?text=Olá,%20quero%20falar%20com%20um%20consultor%20da%20Fyber%20Polímeros.
```

**Substitua `5500000000000` pelo número real no formato: 55 + DDD + número (sem espaços ou caracteres especiais).**

## 🖼️ Sistema de Galeria de Imagens dos Produtos

### 🎯 Como Funciona

Cada produto agora tem sua própria pasta de imagens com suporte para **múltiplas imagens**:

1. **Estrutura Automática**: Execute `criar_pastas_produtos.bat` para criar todas as pastas
2. **Adicione Imagens**: Coloque imagens na pasta do produto (ex: `assets/img/produtos/resinas/resina-epoxi/`)
3. **Nomeação Simples**: Use `1.jpg`, `2.jpg`, `3.jpg` ou nomes descritivos
4. **Galeria Automática**: As imagens aparecem automaticamente na página do produto

### 📸 Funcionalidades da Galeria

- ✅ **Imagem Principal**: A primeira imagem é exibida em destaque
- ✅ **Miniaturas**: Outras imagens aparecem como miniaturas clicáveis
- ✅ **Modal em Tela Cheia**: Clique para ampliar com fundo escuro
- ✅ **Navegação**: Use setas ← → ou clique nas miniaturas
- ✅ **Teclado**: Suporte para ESC, setas direita/esquerda
- ✅ **Responsivo**: Funciona perfeitamente em mobile

### 📐 Tamanhos Recomendados

**Imagens de Produtos** (1200x900px recomendado)
- Formato: `.jpg`, `.jpeg`, `.png`, `.webp`
- Peso máximo: 500KB por imagem
- Proporção: 4:3 ou 16:9

**Banners** (1920x1080px recomendado)
- `banner-1.jpg` - Equipamentos para Fiberglass
- `banner-2.jpg` - Performance e Pontualidade
- `banner-3.jpg` - Tecnologia e Confiança
- `banner-4.jpg` - Atendimento Diferenciado

**Outras**
- `empresa.jpg` (1200x800px) - Foto da empresa
- `favicon.ico` (32x32px) - Ícone do site

### 📖 Guia Detalhado

Para instruções completas sobre como adicionar imagens, consulte: **[COMO_ADICIONAR_IMAGENS.md](COMO_ADICIONAR_IMAGENS.md)**

## 🎯 Paleta de Cores

- Azul Escuro Principal: `#0B2A5A`
- Azul Secundário: `#0E3A8A`
- Branco: `#FFFFFF`
- Cinza Claro: `#F3F4F6`
- Cinza Escuro: `#111827`
- Azul Claro: `#DBEAFE`

## 📝 Notas

- O site funciona completamente offline após o upload
- Não requer servidor ou banco de dados
- Compatível com todos os navegadores modernos
- Otimizado para performance

## 🔧 Suporte

Para dúvidas ou personalizações adicionais, consulte os arquivos HTML, CSS e JS que estão bem comentados e organizados.








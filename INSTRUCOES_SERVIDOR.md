# 🚀 INSTRUÇÕES PARA ACESSAR O SERVIDOR LOCAL

## ✅ Servidor está RODANDO na porta 8000

### Como Acessar:

1. **Abra seu navegador** (Chrome, Edge, Firefox, etc.)

2. **Digite uma destas URLs na barra de endereço:**
   - `http://localhost:8000/index.html`
   - `http://127.0.0.1:8000/index.html`
   - `http://localhost:8000/` (abre index.html automaticamente)

3. **Páginas disponíveis:**
   - **Home:** http://localhost:8000/index.html
   - **Produtos:** http://localhost:8000/produtos.html
   - **Quem Somos:** http://localhost:8000/quem-somos.html
   - **Contato:** http://localhost:8000/contato.html
   - **Teste:** http://localhost:8000/teste.html

### ⚠️ Se não aparecer nada:

1. **Tente em uma janela anônima/privada:**
   - Chrome/Edge: `Ctrl + Shift + N`
   - Firefox: `Ctrl + Shift + P`

2. **Limpe o cache do navegador:**
   - Pressione `Ctrl + Shift + Delete`
   - Selecione "Imagens e arquivos em cache"
   - Clique em "Limpar dados"

3. **Verifique o console do navegador:**
   - Pressione `F12` para abrir as Ferramentas de Desenvolvedor
   - Vá na aba "Console"
   - Veja se há erros (ignorar erros de scripts externos como traffic.js, pixel.js)

4. **Verifique a aba "Network" (Rede):**
   - Na aba "Network", recarregue a página (`Ctrl + R`)
   - Verifique se os arquivos aparecem com status 200 (verde)

### 🔧 Para Reiniciar o Servidor:

Execute no terminal:
```bash
python server.py
```

Ou use o script batch:
```bash
iniciar_servidor.bat
```

Ou use o script PowerShell:
```powershell
.\iniciar_servidor.ps1
```

### ⏹️ Para Parar o Servidor:

Pressione `Ctrl + C` no terminal onde o servidor está rodando.

---

**Status atual:** ✅ Servidor rodando na porta 8000

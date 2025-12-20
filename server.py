#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servidor HTTP simples para servir o site Fyber Polímeros
"""

import http.server
import socketserver
import os
import sys

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        """Override para mostrar logs mais claros"""
        print(f"[{self.log_date_time_string()}] {args[0]} - {args[1]}")
    
    def end_headers(self):
        """Adiciona headers CORS se necessário"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    # Mudar para o diretório do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Verificar se index.html existe
    if not os.path.exists('index.html'):
        print("ERRO: arquivo index.html nao encontrado!")
        print(f"   Diretorio atual: {os.getcwd()}")
        sys.exit(1)
    
    Handler = MyHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("=" * 60)
            print("SERVIDOR HTTP RODANDO!")
            print("=" * 60)
            print(f"URL Principal: http://localhost:{PORT}/index.html")
            print(f"Ou simplesmente: http://localhost:{PORT}/")
            print(f"Pagina de Teste: http://localhost:{PORT}/teste.html")
            print(f"Produtos: http://localhost:{PORT}/produtos.html")
            print("=" * 60)
            print(f"Diretorio servido: {os.getcwd()}")
            print("=" * 60)
            print("\nPressione Ctrl+C para parar o servidor\n")
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 10048:  # Windows: Address already in use
            print(f"ERRO: Porta {PORT} ja esta em uso!")
            print(f"   Tente parar outros servidores ou use outra porta.")
        else:
            print(f"ERRO: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nServidor interrompido pelo usuario.")
        sys.exit(0)

if __name__ == "__main__":
    main()

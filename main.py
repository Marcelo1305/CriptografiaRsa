import threading
import server
import cliente as c
import funcoes
import janela
import socket
import tkinter as tk
from tkinter import scrolledtext

# Gerar chaves
chaves = funcoes.gerar_chaves(11, 13)
chavePublica = chaves[0]
chavePrivada = chaves[1]

# Configuração de rede
host = socket.gethostname()
localIP = socket.gethostbyname(host)
localPort = 20001
bufferSize = 1024

# Criar a janela
form_janela = janela.Janela(localIP, localPort, bufferSize, chavePublica)
form_janela.entrada_ip_servidor.insert(tk.END, localIP)
form_janela.entrada_porta_servidor.insert(0, localPort)
form_janela.entrada_buffer_servidor.insert(0, bufferSize)
form_janela.entrada_chave_privada.insert(0, chavePrivada)
form_janela.entrada_ip_cliente.insert(0, localIP)
form_janela.entrada_porta_cliente.insert(0, localPort)
form_janela.entrada_buffer_cliente.insert(0, bufferSize)
form_janela.entrada_chave_publica.insert(tk.END, "".join(["[", str(chavePublica[0]), " , ", str(chavePublica[1]), "]"]))

# Criar uma thread para executar o servidor UDP
server_thread = threading.Thread(target=server.udp_server, args=(localIP, localPort, bufferSize, chavePrivada, form_janela))
server_thread.daemon = True
server_thread.start()

# Executar o loop principal da janela
form_janela.run()

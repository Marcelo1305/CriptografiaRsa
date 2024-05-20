import tkinter as tk
from tkinter import scrolledtext
import socket
import threading
import AlgoritmoRsa as funcoes
import re
import globals as gl

chaves = [[10,20],[10,20]]     #funcoes.gerar_chaves(5, 79)
chavePublica = chaves[0]
chavePrivada = chaves[1]
strChavePublica = str.encode(str(chavePublica))

def iniciar_servidor(localIP, localPort, bufferSize, text_area):
    msgFromServer = "MENSAGEM RECEBIDA PELO SERVIDOR ..."
    bytesToSend = str.encode(msgFromServer)

    # Criar um datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Definir vínculos entre o endereço e o IP
    UDPServerSocket.bind((localIP, localPort))

    print("UDP - SERVIDOR ATIVADO E ESPERANDO MENSAGEM")

    while True:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0].decode('utf-8')
        address = bytesAddressPair[1]

        print("MENSAGEM RECEBIDA:  ", message)

        # Verificar se a mensagem contem somente números
        if re.match("^\d+$", message):
            msg = funcoes.decriptografar(message, chavePrivada)
            print("="*100)
            print("MENSAGEM DESCRIPTOGRAFADA: ", msg)
            clientMsg = "MENSAGEM DO CLIENTE: {}".format(msg)
            clientIP = "IP DO CLIENTE Address:{}".format(address)
            print(clientIP)

            # Adicionar a mensagem ao text area
            text_area.insert(tk.END, clientMsg + '\n')
            text_area.insert(tk.END, clientIP + '\n')
            text_area.insert(tk.END, '='*46+ '\n')

            # Mensagem de resposta ao cliente
            UDPServerSocket.sendto(bytesToSend, address)
        else:
            if str(message) == "CHAVE":
                # ENVIA CHAVE PUBLICA PARA O CLIENTE
                UDPServerSocket.sendto(strChavePublica, address)
            else:
                msg = "Mensagem não criptografada corretamente"
                # Mensagem de resposta ao cliente
                UDPServerSocket.sendto(str.encode(msg), address)

def udp_server():
    localIP = gl.localIP
    localPort = gl.localPort
    bufferSize = gl.bufferSize
    # Criar a janela principal
    janela = tk.Tk()
    janela.title("Servidor UDP")

    # Criar o text area para exibir as mensagens recebidas
    text_area = scrolledtext.ScrolledText(janela, height=30, width=60)
    text_area.pack(padx=10, pady=10, expand=True, fill='both')

    # Criar uma thread para executar o servidor UDP
    server_thread = threading.Thread(target=iniciar_servidor, args=(localIP, localPort, bufferSize, text_area))
    server_thread.daemon = True
    server_thread.start()

    # Executar o loop principal da janela
    janela.mainloop()


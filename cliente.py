import socket
import funcoes as f
import tkinter as tk
import ast
from datetime import datetime

def udp_client(localIP, localPort, bufferSize, chavePublica, form_janela):
    msgFromClient = form_janela.entrada_mensagem.get("1.0", tk.END).strip()
    if not msgFromClient:
        return

    #Busca os parametros da janela
    localIP = form_janela.entrada_ip_cliente.get()
    localPort = int(form_janela.entrada_porta_cliente.get())
    bufferSize = int(form_janela.entrada_buffer_cliente.get())
    strChaves = form_janela.entrada_chave_publica.get()
    chavePublica = ast.literal_eval(strChaves)

    msgCripto = f.criptografar(msgFromClient, chavePublica)

    # Limpar a caixa de texto
    form_janela.entrada_mensagem.delete("1.0", tk.END)   

    # Adicionar a mensagem enviada na caixa de texto                                           
    form_janela.caixa_mensagem_enviada.tag_config('bold', font=('Helvetica', 10, 'bold'))      
    form_janela.caixa_mensagem_enviada.insert(tk.END, "Cliente Original:".ljust(27, '_'), 'bold')
    form_janela.caixa_mensagem_enviada.insert(tk.END, f"{msgFromClient}\n")
    form_janela.caixa_mensagem_enviada.insert(tk.END, "Mensagem criptografada:".ljust(25, '_'), 'bold')
    form_janela.caixa_mensagem_enviada.insert(tk.END, f"{msgCripto}\n")
    form_janela.caixa_mensagem_enviada.insert(tk.END, "IP:".ljust(26, '_'), 'bold')
    form_janela.caixa_mensagem_enviada.insert(tk.END, f"{str(localIP)}\n")
    form_janela.caixa_mensagem_enviada.insert(tk.END, ("="*80) + '\n')
    form_janela.caixa_mensagem_enviada.see(tk.END)                                                    

    print(msgFromClient)
    print("MENSAGEM CRIPTOGRAFADA:", msgCripto)

    bytesToSend = str.encode(msgCripto)
    serverAddressPort = (localIP, localPort)

    # DEFINIR UM SOCKET UDP PARA O CLIENTE
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # ENVIAR MENSAGEM PARA SERVIDOR UTILIZANDO O SOCKET UDP ATIVADO
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    msg = msgFromServer[0].decode('utf-8')

    # Obter a data atual
    data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    form_janela.retorno(f"{msg} {data_atual}")
    print(msg)

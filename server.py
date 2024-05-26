import socket
import funcoes as f
import tkinter as tk

def udp_server(localIP,localPort,bufferSize, chavePrivada, form_janela):
    msgFromServer= "MENSAGEM RECEBIDA PELO SERVIDOR ...."
    bytesToSend= str.encode(msgFromServer)

    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # DEFINIR VÍNCULOS ENTRE O ENDEREÇO E O IP
    UDPServerSocket.bind((localIP, localPort))

    print("UDP - SERVIDOR ATIVADO E ESPERANDO MENSAGEM.")

    # ESPERANDO POR MENSAGEM
    while(True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0].decode('utf-8')
        address = bytesAddressPair[1]

        message_decripto = f.decriptografar(message, chavePrivada)

        f.adicionar_arquivo("texto_criptografado.txt", message + '\n')
        f.adicionar_arquivo("texto_decriptografado.txt", message_decripto + '\n')
        
        # Adicionar a mensagem ao text area
        form_janela.caixa_mensagem_recebida.tag_config('bold', font=('Helvetica', 10, 'bold'))
        form_janela.caixa_mensagem_recebida.insert(tk.END, "Mensagem Recebida:".ljust(26, '_'), 'bold')
        form_janela.caixa_mensagem_recebida.insert(tk.END, f"{message}\n")
        form_janela.caixa_mensagem_recebida.insert(tk.END, "Mensagem Decriptografada:".ljust(27, '_'), 'bold')
        form_janela.caixa_mensagem_recebida.insert(tk.END, f"{message_decripto}\n")
        form_janela.caixa_mensagem_recebida.insert(tk.END, "IP:".ljust(28, '_'), 'bold')
        form_janela.caixa_mensagem_recebida.insert(tk.END, f"{str(address)}\n")
        form_janela.caixa_mensagem_recebida.insert(tk.END, ("="*80) + '\n')
        form_janela.caixa_mensagem_recebida.see(tk.END)

        # MENSAGEN DE RESPOSTA AO CLIENTE
        UDPServerSocket.sendto(bytesToSend, address)
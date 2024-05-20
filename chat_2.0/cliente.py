import tkinter as tk
from tkinter import scrolledtext
import socket
from datetime import datetime
import AlgoritmoRsa as funcoes
import ast

chavePublica = []
lista_chaves = []

# Função para pesquisar na lista de IPs
def pesquisar_ip(event):
    localIP = ip.get()
    ip_encontrado = next((item[1] for item in lista_chaves if localIP in item), None)
    chave.delete(0, tk.END)
    if ip_encontrado:
        chave.insert(tk.END, "".join(["[", str(ip_encontrado[0]), " , ", str(ip_encontrado[1]), "]"]))
    else:
        chave.insert(tk.END, "")

def udp_client():
    # Função para enviar mensagem para o servidor
    def enviar_mensagem():
        localIP = ip.get()
        try:
            localPort = int(porta.get())
            bufferSize = int(buffer.get())
        except ValueError:
            server_response_label.config(text="Erro: Porta e Buffer devem ser números inteiros.")
            return
        
        serverAddressPort   = (localIP, localPort)

        # Verificar se a chave publica ja foi recebida
        found = False
        for item in lista_chaves:
            if localIP in item[0]:
                found = True
                break

        if not lista_chaves or not found:
            bytesToSend= str.encode("CHAVE")
            # DEFINIR UM SOCKET UDP PARA O CLIENTE
            UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

            # ENVIAR MENSAGEM PARA SERVIDOR UTILIZANDO O SOCKET UDP ATIVADO
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)

            # RECEBE A CHAVE PUBLIC DO SERVIDOR QUANDO CONECTADO
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            msg = msgFromServer[0].decode('utf-8')
            try:
                chavePublica = ast.literal_eval(msg)
                chave.insert(tk.END, msg)
            except:
                print("="*100)
                print("Mensagem recebida: ", msg)
            print("Chave Publica: ", msg)

            # Atualizar o rótulo com a mensagem do servidor
            time = datetime.now().strftime(" - %H:%M:%S")
            server_response_label.config( text= "Chave publica recebida: " + msg + time)
            print(msg)
            lista_chaves.append([localIP,chavePublica])
        ip_encontrado = next((item[1] for item in lista_chaves if localIP in item), None)
        if ip_encontrado:
            chavePublica = ip_encontrado
        mensagem = text_area.get("1.0", "end-1c")
        text_area.delete("1.0", "end")
        msgCripto = funcoes.criptografar(mensagem, chavePublica)

        # DEFINIR UM SOCKET UDP PARA O CLIENTE
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # ENVIAR MENSAGEM PARA SERVIDOR UTILIZANDO O SOCKET UDP ATIVADO
        UDPClientSocket.sendto(str.encode(msgCripto), serverAddressPort)

        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = "MENSAGEM DO SERVIDOR {}".format(msgFromServer[0].decode('utf-8'))

        # Atualizar o rótulo com a mensagem do servidor
        time = datetime.now().strftime(" - %H:%M:%S")
        server_response_label.config(text=msg + time)
        print(msg)

    
    # region Criar a janela principal
    janela = tk.Tk()
    janela.title("Cliente UDP")

    # Configurar o grid para que os widgets possam expandir
    janela.grid_rowconfigure(1, weight=1)
    for i in range(6):
        janela.grid_columnconfigure(i, weight=1)

    # region Criar os campos de entrada ip, porta, buffer
    label1 = tk.Label(janela, text="IP:")
    label1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    global ip
    ip = tk.Entry(janela)
    ip.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    ip.bind("<KeyRelease>", pesquisar_ip)  # Chama a função de pesquisa quando uma tecla é liberada
    host = socket.gethostname()
    ip.insert(tk.END, socket.gethostbyname(host))

    label2 = tk.Label(janela, text="Porta:")
    label2.grid(row=0, column=2, padx=5, pady=5, sticky="e")
    global porta
    porta = tk.Entry(janela)
    porta.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

    label3 = tk.Label(janela, text="Buffer:")
    label3.grid(row=0, column=4, padx=5, pady=5, sticky="e")
    global buffer
    buffer = tk.Entry(janela)
    buffer.grid(row=0, column=5, padx=5, pady=5, sticky="ew")
    # endregion

    # Criar o text area para exibir as mensagens recebidas
    text_area = scrolledtext.ScrolledText(janela, height=10, width=50)
    text_area.grid(row=1, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

    label4 = tk.Label(janela, text="Chave Publica:")
    label4.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    global chave
    chave = tk.Entry(janela)
    chave.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

    # Criar o rótulo para a resposta do servidor
    server_response_label = tk.Label(janela, text="")
    server_response_label.grid(row=2, column=0, columnspan=6, pady=10)

    # Criar o botão de enviar
    btn = tk.Button(janela, text="Enviar", command=enviar_mensagem)
    btn.grid(row=4, column=0, columnspan=6, pady=5)

    # Executar o loop principal da janela
    janela.mainloop()

    # endregion 
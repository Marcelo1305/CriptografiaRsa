import tkinter as tk
from tkinter import scrolledtext
import threading
import cliente as c

class Janela:
    def __init__(self, localIP, localPort, bufferSize, chavePublica):
        self.localIP = localIP
        self.localPort = localPort
        self.bufferSize = bufferSize
        self.chavePublica = chavePublica

        # Criar a janela principal
        self.janela = tk.Tk()
        self.janela.title("Cliente-Servidor")
        self.janela.geometry("1480x700")

        # Seção do Servidor
        tk.Label(self.janela, text="Servidor").grid(row=0, column=1, pady=10)

        tk.Label(self.janela, text="IP:").grid(row=1, column=0, sticky=tk.E)
        self.entrada_ip_servidor = tk.Entry(self.janela, width=30)
        self.entrada_ip_servidor.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(self.janela, text="Porta:").grid(row=2, column=0, sticky=tk.E)
        self.entrada_porta_servidor = tk.Entry(self.janela, width=30)
        self.entrada_porta_servidor.grid(row=2, column=1, padx=5, pady=2)

        tk.Label(self.janela, text="Buffer:").grid(row=3, column=0, sticky=tk.E)
        self.entrada_buffer_servidor = tk.Entry(self.janela, width=30)
        self.entrada_buffer_servidor.grid(row=3, column=1, padx=5, pady=2)

        tk.Label(self.janela, text="Chave Privada:").grid(row=4, column=0, sticky=tk.E)
        self.entrada_chave_privada = tk.Entry(self.janela, width=30)
        self.entrada_chave_privada.grid(row=4, column=1, padx=5, pady=2)

        tk.Label(self.janela, text="Mensagem recebida:").grid(row=5, column=0, columnspan=2,padx=50, pady=5, sticky=tk.W)
        self.caixa_mensagem_recebida = scrolledtext.ScrolledText(self.janela, width=80, height=20)
        self.caixa_mensagem_recebida.grid(row=6, column=0, columnspan=2, padx=50, pady=5)

        # Seção do Cliente
        tk.Label(self.janela, text="Cliente").grid(row=0, column=4, pady=10)

        tk.Label(self.janela, text="IP:").grid(row=1, column=3, sticky=tk.E)
        self.entrada_ip_cliente = tk.Entry(self.janela, width=30)
        self.entrada_ip_cliente.grid(row=1, column=4, padx=5, pady=2)

        tk.Label(self.janela, text="Porta:").grid(row=2, column=3, sticky=tk.E)
        self.entrada_porta_cliente = tk.Entry(self.janela, width=30)
        self.entrada_porta_cliente.grid(row=2, column=4, padx=5, pady=2)

        tk.Label(self.janela, text="Buffer:").grid(row=3, column=3, sticky=tk.E)
        self.entrada_buffer_cliente = tk.Entry(self.janela, width=30)
        self.entrada_buffer_cliente.grid(row=3, column=4, padx=5, pady=2)

        tk.Label(self.janela, text="Chave Pública:").grid(row=4, column=3, sticky=tk.E)
        self.entrada_chave_publica = tk.Entry(self.janela, width=30)
        self.entrada_chave_publica.grid(row=4, column=4, padx=5, pady=2)

        tk.Label(self.janela, text="Mensagem enviada").grid(row=5, column=3, columnspan=2, pady=5, sticky=tk.W)
        self.caixa_mensagem_enviada = scrolledtext.ScrolledText(self.janela, width=80, height=20)
        self.caixa_mensagem_enviada.grid(row=6, column=3, columnspan=2, padx=5, pady=5)

        # Entrada de mensagem e botão de envio
        self.entrada_mensagem = scrolledtext.ScrolledText(self.janela, width=80, height=5)
        self.entrada_mensagem.grid(row=7, column=3, columnspan=2, padx=5, pady=5)

        # Botão que executa a função em uma nova thread
        self.botao_enviar = tk.Button(
            self.janela, 
            text="Enviar Mensagem", 
            command=self.enviar_mensagem,
            width=25, 
            height=2, 
            bg="blue", 
            fg="white"
        )
        self.botao_enviar.grid(row=8, column=4, pady=10, padx=20, sticky=tk.E)

    def enviar_mensagem(self):
        client_thread = threading.Thread(target=c.udp_client, args=(self.localIP, self.localPort, self.bufferSize, self.chavePublica, self))
        client_thread.daemon = True
        client_thread.start()

    def run(self):
        self.janela.mainloop()

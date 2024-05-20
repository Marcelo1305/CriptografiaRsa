import tkinter as tk
from tkinter import scrolledtext
import globals as gl
import server as server

def enviar_mensagem():
    mensagem = entrada_mensagem.get("1.0", tk.END).strip()
    if mensagem:
        caixa_mensagem_enviada.insert(tk.END, mensagem + "\n")
        entrada_mensagem.delete("1.0", tk.END)

# Criar a janela principal
global janela
janela = tk.Tk()
janela.title("Cliente-Servidor")

# Configurar a geometria da janela
janela.geometry("900x700")  # Aumentar o tamanho da janela

# Seção do Servidor
tk.Label(janela, text="Servidor").grid(row=0, column=1, pady=10)

tk.Label(janela, text="IP:").grid(row=1, column=0, sticky=tk.E)
entrada_ip_servidor = tk.Entry(janela, width=30)  # Aumentar a largura das entradas de texto
entrada_ip_servidor.grid(row=1, column=1, padx=5, pady=2)
entrada_ip_servidor.insert(tk.END, gl.localIP)

tk.Label(janela, text="Porta:").grid(row=2, column=0, sticky=tk.E)
entrada_porta_servidor = tk.Entry(janela, width=30)  # Aumentar a largura das entradas de texto
entrada_porta_servidor.grid(row=2, column=1, padx=5, pady=2)

tk.Label(janela, text="Buffer:").grid(row=3, column=0, sticky=tk.E)
entrada_buffer_servidor = tk.Entry(janela, width=30)  # Aumentar a largura das entradas de texto
entrada_buffer_servidor.grid(row=3, column=1, padx=5, pady=2)

tk.Label(janela, text="Chave Privada:").grid(row=4, column=0, sticky=tk.E)
entrada_chave_privada = tk.Entry(janela, width=30)  # Aumentar a largura das entradas de texto
entrada_chave_privada.grid(row=4, column=1, padx=5, pady=2)

tk.Label(janela, text="Mensagem recebida:").grid(row=5, column=0, columnspan=2, pady=5, sticky=tk.W)
caixa_mensagem_recebida = scrolledtext.ScrolledText(janela, width=50, height=20)  # Aumentar a largura e a altura
caixa_mensagem_recebida.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Seção do Cliente
tk.Label(janela, text="Cliente").grid(row=0, column=4, pady=10)

tk.Label(janela, text="IP:").grid(row=1, column=3, sticky=tk.E)
entrada_ip_cliente = tk.Entry(janela, width=30)  # Aumentar a largura das entradas de texto
entrada_ip_cliente.grid(row=1, column=4, padx=5, pady=2)

tk.Label(janela, text="Porta:").grid(row=2, column=3, sticky=tk.E)
entrada_porta_cliente = tk.Entry(janela, width=30)  # Aumentar a largura das entradas de texto
entrada_porta_cliente.grid(row=2, column=4, padx=5, pady=2)

tk.Label(janela, text="Buffer:").grid(row=3, column=3, sticky=tk.E)
entrada_buffer_cliente = tk.Entry(janela, width=30)  # Aumentar a largura das entradas de texto
entrada_buffer_cliente.grid(row=3, column=4, padx=5, pady=2)

tk.Label(janela, text="Chave Pública:").grid(row=4, column=3, sticky=tk.E)
entrada_chave_publica = tk.Entry(janela, width=30)  # Aumentar a largura das entradas de texto
entrada_chave_publica.grid(row=4, column=4, padx=5, pady=2)

tk.Label(janela, text="Mensagem enviada").grid(row=5, column=3, columnspan=2, pady=5, sticky=tk.W)
caixa_mensagem_enviada = scrolledtext.ScrolledText(janela, width=50, height=20)  # Aumentar a largura e a altura
caixa_mensagem_enviada.grid(row=6, column=3, columnspan=2, padx=5, pady=5)

# Entrada de mensagem e botão de envio
entrada_mensagem = scrolledtext.ScrolledText(janela, width=50, height=5)  # Aumentar a largura e a altura
entrada_mensagem.grid(row=7, column=3, columnspan=2, padx=5, pady=5)

botao_enviar = tk.Button(janela, text="Enviar Mensagem", command=server.udp_server, width=25, height=2, bg="blue", fg="white")
botao_enviar.grid(row=8, column=4, pady=10, sticky=tk.E)

# Iniciar o loop da interface gráfica
janela.mainloop()

import tkinter as tk
import threading
import time

# Variáveis globais
entrada_ip_servidor = None
entrada_porta_servidor = None
entrada_buffer_servidor = None

def thread_func():
    global entrada_ip_servidor
    for i in range(10):
        time.sleep(1)  # Simula algum trabalho
        janela.after(0, update_ui, i)  # Agende a atualização da UI na thread principal

def update_ui(i):
    global entrada_ip_servidor
    entrada_ip_servidor.delete(0, tk.END)  # Limpa a entrada
    entrada_ip_servidor.insert(0, str(i))  # Insere o novo valor

# Criar a janela principal
janela = tk.Tk()
janela.title("Cliente-Servidor")

# Configurar a geometria da janela
janela.geometry("900x700")  # Aumentar o tamanho da janela

# Seção do Servidor
tk.Label(janela, text="Servidor").grid(row=0, column=1, pady=10)

tk.Label(janela, text="IP:").grid(row=1, column=0, sticky=tk.E)
entrada_ip_servidor = tk.Entry(janela, width=30)  # Aumentar a largura das entradas de texto
entrada_ip_servidor.grid(row=1, column=1, padx=5, pady=2)

# Inicie a thread
threading.Thread(target=thread_func).start()

# Inicie o loop principal do Tkinter
janela.mainloop()
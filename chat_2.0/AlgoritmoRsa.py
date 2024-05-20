import os
import tkinter as tk
from tkinter import scrolledtext
from sympy import nextprime

os.system("cls")

# Variáveis globais para armazenar os valores de p, q, delta, E e n
p = 0
q = 0
delta = 0
E = 0
n = 0

# VERIFICAR SE UM NÚMERO É PRIMO
def primo(n):
    if n == 1:
        return 1
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

# GERAR NÚMEROS PRIMOS ENTRE: inicio e fim
def gerarPrimo(inicio, fim):
    aux = []
    for i in range(inicio, fim):
        if primo(i) == 1:
            aux.append(i)
    return aux

def escolherPrimos():
    global p, q, janela
    primo_inicio = int(campo_primo_inicio.get())
    primo_fim = int(campo_primo_fim.get())
    
    # Calcular p e q como números primos dentro do intervalo
    p = nextprime(primo_inicio - 1)
    q = nextprime(primo_fim - 1)
    
    # Fechar a janela
    janela.destroy()

# FORMULÁRIO PARA ESCOLHER OS NÚMEROS PRIMOS
def formEscolherPrimos():
    global campo_primo_inicio, campo_primo_fim, janela
    # Criar a janela principal
    janela = tk.Tk()
    janela.title("Servidor UDP")
    janela.geometry("500x50")

    # Configurar o grid para que os widgets possam expandir corretamente
    janela.grid_rowconfigure(1, weight=1)
    janela.grid_columnconfigure(0, weight=1)
    janela.grid_columnconfigure(1, weight=1)
    janela.grid_columnconfigure(2, weight=1)
    janela.grid_columnconfigure(3, weight=1)
    janela.grid_columnconfigure(4, weight=1)
    janela.grid_columnconfigure(5, weight=1)

    # Criar os campos de entrada e rótulos
    label_primo_inicio = tk.Label(janela, text="Primo Início:")
    label_primo_inicio.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    campo_primo_inicio = tk.Entry(janela)
    campo_primo_inicio.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    label_primo_fim = tk.Label(janela, text="Primo Fim:")
    label_primo_fim.grid(row=0, column=2, padx=5, pady=5, sticky="e")
    campo_primo_fim = tk.Entry(janela)
    campo_primo_fim.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

    # Botão de escolher primos
    btn_escolher_primos = tk.Button(janela, text="Escolher primos", command=escolherPrimos)
    btn_escolher_primos.grid(row=0, column=6, padx=5, pady=5, sticky="ew")

    # Executar o loop principal da janela
    janela.mainloop()

def escolherChave():
    global E, janelaChaves
    try:
        E = int(campo_chave.get())
    except ValueError:
        print("Erro: o valor inserido não pode ser convertido em um inteiro")
    janelaChaves.destroy()

def escolherChaves():
    global campo_chave, janelaChaves, delta, q
    janelaChaves = tk.Tk()
    janelaChaves.title("Escolher chave")
    janelaChaves.geometry("500x500")

    # Configurar o grid para que os widgets possam expandir corretamente
    janelaChaves.grid_rowconfigure(1, weight=1)
    janelaChaves.grid_columnconfigure(0, weight=1)
    janelaChaves.grid_columnconfigure(1, weight=1)
    janelaChaves.grid_columnconfigure(2, weight=1)
    janelaChaves.grid_columnconfigure(3, weight=1)
    janelaChaves.grid_columnconfigure(4, weight=1)
    janelaChaves.grid_columnconfigure(5, weight=1)

    # Criar os campos de entrada e rótulos
    label_chave = tk.Label(janelaChaves, text="Chave:")
    label_chave.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    campo_chave = tk.Entry(janelaChaves)
    campo_chave.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    # Criar o text area para exibir as mensagens recebidas
    text_area = scrolledtext.ScrolledText(janelaChaves, height=10, width=50)
    text_area.grid(row=1, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")
    text_area.insert(tk.END, gerarPrimo(q+1, delta))

    # Botão de escolher primos
    btn_escolher_chave = tk.Button(janelaChaves, text="Escolher chave", command=escolherChave)
    btn_escolher_chave.grid(row=0, column=6, padx=5, pady=5, sticky="ew")

    # Executar o loop principal da janela
    janelaChaves.mainloop()

# GERAR CHAVES PÚBLICA E PRIVADA
def gerar_chaves(pp, qq):
    global p, q, delta, E, n
    formEscolherPrimos()

    #CALCULAR N
    n = p * q

    #CALCULAR O TOCIENTE DE EULER
    delta = (p-1)*(q-1)

    # GERAÇÃO DE NÚMEROS PRIMOS
    #print(gerarPrimo(q+1,delta))

    # ESPECIFICAR E
    E = 0     #int(input("ESCOLHA UM NUMERO PRIMO:"))
    escolherChaves()

    D = 1
    flag = 100
    while flag != 1:
        D = D + 1
        flag = (E * D) % delta
        if flag == 1:
            print()
            print("CHAVE PÚBLICA: [", E, ",", n, "]")
            print("CHAVE PRIVADA: [", D, ",", n, "]")
            print()
    return [[E, n], [D, n]]

# CONVERTER TEXTO EM NÚMEROS
def textonum(texto):
    num = ""
    for i in texto:
        num = num + str(ord(i)).zfill(3)
    return num

# CONVERTER NÚMEROS EM TEXTO
def numtexto(num):
    texto = ""
    for i in range(0, len(num), 3):
        texto = texto + chr(int(num[i:i+3]))
    return texto

# CRIPTOGRAFAR
def criptografar(texto, chave):
    #Conversão do texto em caracteres númericos
    texto_num = textonum(texto)
    #Chave pública
    E = chave[0]
    n = chave[1]
    cripto = ""
    for i in range(0, len(texto_num), 3):
        #separar os caracteres do texto de 3 em 3
        ftoken = texto_num[i:i+3]

        vl = int(ftoken)
        cp = (vl ** E) % n
        cripto = cripto + str(cp).zfill(3)
    return cripto

# DECRIPTOGRAFAR
def decriptografar(cripto, chave):
    #Chave privada
    D = chave[0]
    n = chave[1]
    decripto = ""
    for vl in range(0, len(cripto), 3):
        ftoken = cripto[vl:vl+3]
        dcp = (int(ftoken) ** D) % n
        caracter = chr(dcp)
        decripto = decripto + caracter
    return decripto

# CRIPTOGRAFAR OU DECRIPTOGRAFAR ARQUIVO
def cripto_decripto_arquivo(arquivo_origem, arquivo_destino, chave, cripto):
    with open(arquivo_origem) as origem:
        with open(arquivo_destino, 'w') as destino:
            for linha in origem:
                #if(linha != "\n"):
                texto = ""
                if cripto:
                    texto = criptografar(linha.strip(), chave) + "\n"
                else:
                    texto = decriptografar(linha.strip(), chave) + "\n"
                destino.write(texto)

# LER DADOS DO ARQUIVO
def ler_arquivo(arquivo):
    with open(arquivo, encoding="utf-8") as f:
        print(f.read())

# ADICIONAR DADOS AO ARQUIVO
def adicionar_arquivo(arquivo, texto):
    with open(arquivo, 'a', encoding="utf-8") as f:
        f.write(texto)
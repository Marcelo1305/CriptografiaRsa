import os
os.system("cls")

# VERIFICAR SE UM NÚMERO É PRIMO
def primo(n):
    if (n==1):
        return 1
    for i in range(2,n):
        if ( (n % i)==0 ):
            return 0
    return 1

# GERAR NÚMEROS PRIMOS ENTRE: inicio e fim
def gerarPrimo(inicio,fim):
    aux=[]
    for i in range(inicio,fim):
        if (primo(i)==1):
            aux.append(i)
    return aux

# GERAR CHAVES PÚBLICA E PRIVADA
def gerar_chaves(p,q):

    #CALCULAR N
    n = p * q

    #CALCULAR O TOCIENTE DE EULER
    delta = (p-1)*(q-1)

    # GERAÇÃO DE NÚMEROS PRIMOS
    print(gerarPrimo(q+1,delta))

    # ESPECIFICAR E
    E=int(input("ESCOLHA UM NUMERO PRIMO:"))

    D=1
    flag=100
    while(flag!=1):
        D=D+1
        flag=(E*D)%delta
        if (flag==1):
            print()
            print("CHAVE PÚBLICA: [",E,",",n,"]")
            print("CHAVE PRIVADA: [",D,",",n,"]")
            print()
    return [[E,n],[D,n]]

# CRIPTOGRAFAR
def criptografar(texto, chavePublica):
    #Chave pública
    E = chavePublica[0]
    n = chavePublica[1]
    cripto = ""
    for i in texto:
        vl = ord(i)
        cp = (vl ** E) % n
        strcp = str(cp).zfill(3)
        cripto = cripto + strcp
    return cripto

# DECRIPTOGRAFAR
def decriptografar(cripto, chavePrivada):
    #Chave privada
    D = chavePrivada[0]
    n = chavePrivada[1]
    decripto = ""
    for vl in range(0, len(cripto), 3):
        ftoken = cripto[vl:vl+3]
        vl = int(ftoken)
        dcp = (vl ** D) % n
        caracter = chr(dcp)
        decripto = decripto + caracter
    return decripto

# LER DADOS DO ARQUIVO
def ler_arquivo(arquivo):
    with open(arquivo,encoding="utf-8") as f:
        for i in f:
            print(i.strip())
    print("\n")

# ADICIONAR DADOS AO ARQUIVO
def adicionar_arquivo(arquivo, texto):
    with open(arquivo, 'a', encoding="utf-8") as f:
        f.write(texto)
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

# CONVERTER TEXTO EM NÚMEROS
def textonum(texto):
    num = ""
    for i in texto:
        num = num + str(ord(i)).zfill(3)
    return num

# CONVERTER NÚMEROS EM TEXTO
def numtexto(num):
    texto = ""
    for i in range(0,len(num),3):
        texto = texto + chr(int(num[i:i+3]))
    return texto

# CRIPTOGRAFAR
def criptografar(texto,chave):
    #Conversão do texto em caracteres númericos
    texto_num = textonum(texto)
    #Chave pública
    E = chave[0]
    n = chave[1]
    cripto = ""
    for i in range(0,len(texto_num),3):
        #separar os caracteres do texto de 3 em 3
        ftoken = texto_num[i:i+3]

        vl = int(ftoken)
        cp = (vl**E) % n
        cripto = cripto + str(cp).zfill(3)
    return cripto

# DECRIPTOGRAFAR
def decriptografar(cripto,chave):
    #Chave privada
    D = chave[0]
    n = chave[1]
    decripto = ""
    for vl in range(0,len(cripto),3):
        ftoken = cripto[vl:vl+3]
        dcp = (int(ftoken)**D) % n
        caracter = chr(dcp)
        decripto = decripto + caracter
    return decripto

# CRIPTOGRFAR OU DECRIPTOGRAFAR ARQUIVO
def cripto_decripto_arquivo(arquivo_origem, arquivo_destino, chave, cripto):
    with open(arquivo_origem) as origem:
        with open(arquivo_destino, 'w') as destino:
            for linha in origem:
                #if(linha != "\n"):
                texto = ""
                if(cripto):
                    texto = criptografar(linha.strip(), chave) + "\n"
                else:
                    texto = decriptografar(linha.strip(), chave) + "\n"
                destino.write(texto)

# LER DADOS DO ARQUIVO
def ler_arquivo(arquivo):
    with open(arquivo,encoding="utf-8") as f:
        for i in f:
            print(i.strip())
    print("\n")
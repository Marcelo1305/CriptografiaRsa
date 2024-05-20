import socket

janela = None

# Variáveis globais para a interface gráfica do servidor
entrada_ip_servidor = None
entrada_porta_servidor = None
entrada_buffer_servidor = None
entrada_chave_privada = None
caixa_mensagem_recebida = None

# Variáveis globais para a interface gráfica do cliente
entrada_ip_cliente = None
entrada_porta_cliente = None
entrada_buffer_cliente = None
entrada_chave_publica = None
caixa_mensagem_enviada = None
entrada_msg = None

# Variáveis globais para o servidor UDP
host = socket.gethostname()
localIP = socket.gethostbyname(host)
localPort = 20001
bufferSize = 1024
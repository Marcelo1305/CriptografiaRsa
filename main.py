import threading
import server as server
import cliente as cliente
import time

localIP = "192.168.0.101"
localPort = 20001
bufferSize = 1024

# Criar e iniciar a thread para o servidor UDP
server_thread = threading.Thread(target=server.udp_server, args=(localIP, localPort, bufferSize))
server_thread.daemon = True
server_thread.start()
time.sleep(1)

# Criar e iniciar a thread para o cliente UDP
client_thread = threading.Thread(target=cliente.udp_client)
client_thread.daemon = True
client_thread.start()
time.sleep(1)

while True:
    time.sleep(10)
    pass
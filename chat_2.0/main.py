import socket
import threading
import time
import testejanela as tjanela
import globals as gl

# # Criar e iniciar a thread para o servidor UDP
# server_thread = threading.Thread(target=server.udp_server, args=(localIP, localPort, bufferSize))
# server_thread.daemon = True
# server_thread.start()
# time.sleep(1)

# # Criar e iniciar a thread para o cliente UDP
# client_thread = threading.Thread(target=cliente.udp_client)
# client_thread.daemon = True
# client_thread.start()
# time.sleep(1)

# Criar e iniciar a thread para o cliente UDP
form_thread = threading.Thread(target=tjanela)
form_thread.daemon = True
form_thread.start()
time.sleep(1)


# server_thread.join()
# client_thread.join()


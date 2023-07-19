#Observação: Executar primeiro o servidor, depois o cliente

from socket import * # Importando todas as funções (métodos) da biblioteca socket
servidor = "127.0.0.1"
porta = 43210 # Porta representada por um número inteiro entre 0 e 65535

obj_socket = socket(AF_INET, SOCK_STREAM) #Parâmetro AF_INET define o tipo de identificação
                                          #com o servidor (IP ou hostname)
                                          #O parâmetro DGRAM determina que utilizaremos o protocolo de transporte TCP
obj_socket.bind((servidor, porta))
obj_socket.listen(2)

print("Aguardando cliente... ")
while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Olah Cliente'
        con.send(msg_enviada)
        break
    con.close()

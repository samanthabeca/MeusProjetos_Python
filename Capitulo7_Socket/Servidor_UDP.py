from socket import *

servidor  = "127.0.0.1"
porta = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM) #Parâmetro DGRAM determina que utilizaremos o protocolo de transporte UDP
obj_socket.bind((servidor, porta))
print("Servidor pronto...")
while True:
    dados, origem = obj_socket.recvfrom(65535)
    print("Origem ..........: ", origem)
    print("Dados recebidos .: ", dados.decode()) #Função decode() exibe os dados bytes no formato string. OBS: Forma que também poderia ser utilizada com o protocolo TCP
    resposta = input("Digite a resposta: ")
    obj_socket.sendto(resposta.encode(), origem) # Método encode() converte de string para byte
obj_socket.close()
#Enviando dados do Python para o Arduino

import serial
conexao=""
for porta in range(10):
    try:
        conexao = serial.Serial("/dev/ttyUSB0" + str(porta), 115200)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao!="":
    acao=input("Digite:\n" +
                "<L> para Ligar\n" +
                "<D> para Desligar: ").upper()
    while acao=="L" or acao=="D":
        if acao=="L":
            conexao.write(b'1')
        else:
            conexao.write(b'0')
        acao = input("Digite:\n" +
                     "<L> para Ligar\n" +
                     "<D> para Desligar: ").upper()
    conexao.close()
    print("Conexao encerrada")
else:
    print("Sem portas disponíveis")
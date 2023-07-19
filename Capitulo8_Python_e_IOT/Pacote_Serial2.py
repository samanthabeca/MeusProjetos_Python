import serial # Classe serial
conexao = ""
for porta in range(10):
    try:
        conexao = serial.Serial("/dev/ttyUSB0" + str(porta), 115200)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass # Comando para ignorar a exceção
if conexao != "":
    conexao.close()
    print("Conexao encerrada")
else:
    print("Sem portas disponíveis")
import socket # A biblioteca socket permite a troca de pacotes entre equipamentos que estão conectados em uma mesma rede por meio dos 
# protocolos TCP e UDP

resp = "S"
while(resp == "S"):
    url = input("Digite uma url: ")
    ip = socket.gethostbyname(url)
    print("O IP referente à url informada é: ", ip)
    resp = input("Digite <s> para continuar: ").upper()
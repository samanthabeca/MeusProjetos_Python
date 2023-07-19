from Capitulo3_Funcoes.Funcoes_Arquivos import *
inventario={}

opcao=chamarMenu()
resp = "S"
while resp == "S":
    if opcao == "1":
        registrar(inventario)
        opcao = chamarMenu()
    elif opcao == "2":
        print(persistir(inventario))
        opcao = chamarMenu()
    elif opcao == "3":
        resultado = exibir()
        for linha in resultado:
            lista = linha.split(";")
            print("Data .........: ", lista[1])
            print("Descrição ....: ", lista[2])
            print("Departamento .: ", lista[3])
        opcao = chamarMenu()
    else:
        resp = "N"
        print("Programa encerrado.")
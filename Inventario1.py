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
        print(exibir())
        opcao = chamarMenu()
    else:
        resp = "N"
        print("Programa encerrado.")
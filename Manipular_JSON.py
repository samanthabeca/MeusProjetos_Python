from Capitulo3_Funcoes.Funcoes_JSON import *

arquivo = "inventario_json.json"
inventario = ler_arquivo(arquivo)
opcao = chamarMenu()
resp = "S"
while resp == "S":
    if opcao == "1":
        print(registrar(inventario, arquivo))
        opcao = chamarMenu()
    elif opcao == "2":
        exibir(arquivo)
        opcao = chamarMenu()
    else:
        resp = "N"
        print("Programa encerrado.")
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
            separacao=linha[linha.find(";")+1:-1]
            data=separacao[0:separacao.find(";")]
            separacao = separacao[separacao.find(";")+1:-1]
            descricao=separacao[0:separacao.find(";")]
            departamento=linha[linha.rfind(";")+1:-1]
            print("Data.........: ", data)
            print("Descrição....: ", descricao)
            print("Departamento.: ", departamento)
        opcao = chamarMenu()
    else:
        resp = "N"
        print("Programa encerrado.")
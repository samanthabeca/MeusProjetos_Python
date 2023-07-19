import json #biblioteca json
import os #biblioteca os

def chamarMenu():
    return input("########## Inventário Arquivo JSON ##########\n" +
                    "Digite: \n" + 
                    "<1> para registrar ativo\n"
                    "<2> para exibir ativos armazenados\n"+
                    "Opção: ").upper()
     
def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq_json:
            dicionario = json.load(arq_json)
    else:
        dicionario = {}
    return dicionario

def gravar_arquivo(dicionario, arquivo):
    with open(arquivo, "w") as arq_json:
        json.dump(dicionario, arq_json)

def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")]=[
                    input("Digite a data da última atualização: "),
                    input("Digite a descrição: "),
                    input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar: ").upper()
        gravar_arquivo(dicionario, arquivo)
    return "JSON gerado!!!!"

def exibir(arquivo):
    dicionario = ler_arquivo(arquivo)
    print("========= Exibindo Inventário JSON ========")
    for chave, dado in dicionario.items():
        print("Data.........: ", dado[0])
        print("Descrição....: ", dado[1])
        print("Departamento.: ", dado[2])
        print("=================")

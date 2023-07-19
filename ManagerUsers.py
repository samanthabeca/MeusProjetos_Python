from Capitulo3_Funcoes.Funcoes_Dicionarios import *

#Capítulo 4 sobre dicionários

usuarios = {}
opcao = exibirMenu()
resposta = "S"
while resposta == "S":
    if opcao == "I":
        inserirUsuario(usuarios)
        opcao = exibirMenu()
    elif opcao == "P":
        chave = input("Digite o login: ").upper()
        pesquisar(usuarios,chave)
        opcao = exibirMenu()
    elif opcao == "E":
        chave = input("Digite o login: ").upper()
        excluirUsuario(usuarios,chave)
        opcao = exibirMenu()
    elif opcao == "L":
        listarUsuarios(usuarios)
        opcao = exibirMenu()
    elif opcao == "S":
        print("Programa encerrado.")
        resposta = "N"
    else:
        print("Opcao inválida!")
        opcao = exibirMenu()

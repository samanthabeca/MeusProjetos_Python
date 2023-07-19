from Capitulo3_Funcoes.IdentificacaoDeFuncoes import *

#Capítulo 3 sobre listas

resposta = "S"
minhaLista = []
while resposta == "S":
    print("======= Inventário: Equipamentos - OPÇÕES =======")
    print("1-Cadastrar")
    print("2-Exibir")
    print("3-Pesquisar")
    print("4-Depreciar")
    print("5-Excluir")
    print("6-Resumir valores")
    print("7-Sair")
    opcao = int(input("Opção: "))
    if opcao == 1:
        print("Cadastrando...")
        preencherInventario(minhaLista)
    elif opcao == 2:
        print("Exibindo...")
        exibirInventario(minhaLista)
    elif opcao == 3:
        print("Pesquisando...")
        localizarPorNome(minhaLista)
    elif opcao == 4:
        print("Alterando...")
        perc = int(input("Digite o percentual da depreciação: "))
        depreciarPorNome(minhaLista, perc)     
    elif opcao == 5:
        print("Excluindo...")
        print(excluirPorSerial(minhaLista))
    elif opcao == 6:
        print("Resumindo...")
        resumirValores(minhaLista)
    elif opcao == 7:
        resposta = "N"
    else:
        opcao = int(input("Opção inválida!"))
    
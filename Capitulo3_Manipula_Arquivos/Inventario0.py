inventario = {}
print("########## INVENTÁRIO ##########")
opcao = input("Digite: \n" + 
                  "<1> Para registrar ativo\n" +
                  "<2> Para persistir em arquivo\n" +
                  "<3> Para exibir ativos armazenados\n"
                  "<4> Sair\n" +
                  "Opção: ")
resp = "S"
while resp == "S":
    if opcao == "1":
        resp2 = "S"
        while resp2 == "S":
            inventario[input("Digite o número de patrimônio: ")]=[
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
            resp2 = input("Digite <S> para continuar: ").upper()
        opcao = input("Digite: \n" + 
                  "<1> Para registrar ativo\n" +
                  "<2> Para persistir em arquivo\n" +
                  "<3> Para exibir ativos armazenados\n"
                  "<4> Sair\n" +
                  "Opção: ")
    elif opcao == "2":
        with open("inventario.csv", "a") as inv:
            for chave, valor in inventario.items():
                inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n")
            print("Persistido com sucesso!")
            opcao = input("Digite: \n" + 
                  "<1> Para registrar ativo\n" +
                  "<2> Para persistir em arquivo\n" +
                  "<3> Para exibir ativos armazenados\n"
                  "<4> Sair\n" +
                  "Opção: ")
    elif opcao == "3":
        with open("inventario.csv","r") as inv:
            print(inv.readlines())
        opcao = input("Digite: \n" + 
                  "<1> Para registrar ativo\n" +
                  "<2> Para persistir em arquivo\n" +
                  "<3> Para exibir ativos armazenados\n"
                  "<4> Sair\n" +
                  "Opção: ")
    else:
        resp = "N"
        print("Programa encerrado.")
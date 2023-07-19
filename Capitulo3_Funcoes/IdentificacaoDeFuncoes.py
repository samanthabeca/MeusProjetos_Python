def preencherInventario(lista):
    resp = "S"
    print("====== CADASTRO DE EQUIPAMENTOS ======")
    while resp == "S":
        equipamento = [input("Equipamento: "),
                       float(input("Valor: ")),
                       int(input("Número serial: ")),
                        input("Departamento: ")]
        lista.append(equipamento)
        resp = input("Digite 'S' para continuar: ").upper()
    
def exibirInventario(lista):
    print("====== LISTA DE EQUIPAMENTOS DO INVENTARIO ======")
    if len(lista) > 0:
        for elemento in lista:
            print("Nome............: ", elemento[0])
            print("Valor...........: ", elemento[1]) 
            print("Serial..........: ", elemento[2])
            print("Departamento....: ", elemento[3])
            print("=====================")
    else:
        print("Lista vazia.")

def localizarPorNome(lista):
    print("====== BUSCA DE EQUIPAMENTOS ======")
    busca = input("Digite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor..: ", elemento[1])
            print("Serial.:", elemento[2])

def depreciarPorNome(lista, porc):
    print("====== DEPRECIAÇÃO DE EQUIPAMENTOS ======")
    depreciacao = input("Digite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1 - porc / 100)
            print("Novo valor: ", elemento[1])

def excluirPorSerial(lista):
    print("====== EXCLUSÃO DE EQUIPAMENTOS ======")
    resposta2 = "S"
    while resposta2 == "S":
        serial = int(input("Digite o serial do equipamento que será excluído: "))
        for elemento in lista:
            if elemento[2] == serial:
                lista.remove(elemento)
        resposta2 = input("Deseja excluir outro equipamento? Digite 'S' para sim: ").upper()
    return "Itens excluídos."

def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    print("====== RESUMO DE VALORES DO INVENTARIO ======")
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O valor total de equipamentos é de: ", sum(valores))
    else:
        print("Lista vazia.")
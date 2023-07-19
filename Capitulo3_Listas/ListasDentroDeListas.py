inventario=[]
resposta = "S"
while resposta == "S":
    print("====== CADASTRO DE EQUIPAMENTOS ======")
    equipamento=[input("Equipamento: "),
    float(input("Valor: ")),
    int(input("Número Serial: ")),
    input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Digite 'S' para continuar: ").upper()


print("====== INVENTARIO: EQUIPAMENTOS ======")
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])
    print("=====================")

print("====== BUSCA DE EQUIPAMENTOS ======")
busca=input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca==elemento[0]:
        print("Valor..: ", elemento[1])
        print("Serial.:", elemento[2])

print("====== DEPRECIAÇÃO DE EQUIPAMENTOS ======")
depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

print("====== BAIXA DE EQUIPAMENTOS ======")
resposta2 = "S"
while resposta2 == "S":
    serial = int(input("Digite o serial do equipamento que será excluído: "))
    for elemento in inventario:
        if elemento[2] == serial:
            inventario.remove(elemento)
    resposta2 = input("Deseja excluir outro equipamento? Digite 'S' para sim: ").upper()

print("====== LISTA DE EQUIPAMENTOS DO INVENTARIO ======")
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])
    print("=====================")

valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O valor total de equipamentos é de: ", sum(valores))
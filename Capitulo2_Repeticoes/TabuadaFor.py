valor = int(input("Digite o valor para calcular a tabuada: "))
for i in range (1, 11, 1):
    res = valor * i
    print("Tabuada: " + str(valor) + " x " + str(i) + " = " + str(res))
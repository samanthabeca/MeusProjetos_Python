#Qual o total de voos internacionais que partiram do aeroporto de Logan no ano de 2014?

with open("economic-indicators.csv","r") as boston:
    totalVoos = 0
    ano = 2014
    for linha in boston.readlines()[1:-1]:
        lista = linha.split(",")
        if int(lista[0]) == ano:
            totalVoos += int(lista[3])
    print("O total de voos em 2014 é: ", totalVoos)
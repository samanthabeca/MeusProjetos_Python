"""
- Qual o total de voos internacionais que partiram do aeroporto de Logan no ano 
especificado pelo usuário?
- Quando (mês/ano) ocorreu o maior_passageiros trânsito de passageiros no aeroporto de Logan?
- Qual o total de passageiros que passaram pelo aeroporto de Logan, no ano que for
especificado pelo usuario?
- Qual o mês que possui a maior_passageiros média da diária de um hotel, com base no ano especificado
pelo usuário?
"""

with open("economic-indicators.csv","r") as boston:
    totalVoos = 0
    total_passageiros = 0
    maior_passageiros = 0
    maior_media_diaria = 0
    ano = input("Qual ano deseja pesquisar? ")
    linhas = boston.readlines()
    for linha in linhas[1:len(linhas)]: #Essa linha pode ser assim também: "for linha in linhas[1:]:" pois se deixar o campo após os dois pontos em "[1:]" vazio
        #ele percorre até o final, até a última linha    
        lista = linha.split(",")
        if lista[0] == ano:
            totalVoos = totalVoos + int(lista[3])
            total_passageiros = total_passageiros + int(lista[2])
            if float(lista[5]) > float(maior_media_diaria):
                maior_media_diaria = lista[5]
                mes_maior_diaria = lista[1]
        if int(lista[2]) > int(maior_passageiros):
            maior_passageiros = lista[2]
            ano_maior_movimento = lista[0]
            mes = lista[1]
    print("O total de voos em " + ano + " é: ", str(totalVoos)) 
    print("O mês/ano de maior movimento no aeroporto foi: ",
	 					str(mes),"/", str(ano_maior_movimento), "com " + str(maior_passageiros) + " passageiros")
    print("O total de passageiros do ano ", ano,
	 					"foi de ", str(total_passageiros))
    print("O mês do ano ", ano,
	        "com maior média para diária de hotel foi ", mes_maior_diaria)
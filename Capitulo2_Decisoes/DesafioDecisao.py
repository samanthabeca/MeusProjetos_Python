import sys
nivel = int(input("Digite o nível de acesso => (1) para Administrador, (2) para usuário ou (3) para visitante: "))

if nivel < 1 or nivel > 3:
    print("Nivel de acesso inválido")
    sys.exit('Saindo')
else:
    if (nivel != 3):
        genero = int(input("Digite o gênero (1) Feminino ou (2) Masculino: "))

if nivel == 1:
    if genero == 1:
        print("Olá administradora!")
    else:
        print("Olá administrador!")
elif nivel == 2:
    if genero == 1:
        print("Olá usuária!")
    else:
        print("Olá usuário!")
else:
    print("Olá visitante!")
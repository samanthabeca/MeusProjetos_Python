with open("pagina.html", "w") as pagina:
    pagina.write("<html><head><title>Titulo da Página</title></head>")
    pagina.write("<body><h2>Abaixo seguem alguns nomes importantes para o projeto: </h2>")
    pagina.write("<h3>")
    nome = ""
    while nome != "SAIR":
        nome = input("Digite um nome ou SAIR: ").upper()
        if nome != "SAIR":
            pagina.write("<br>" + nome)
    pagina.write("</h3></body></html>")
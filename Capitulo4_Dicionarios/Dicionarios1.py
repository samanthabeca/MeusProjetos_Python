usuarios = {} #Para listas utilizamos [], para dicionario de dados utilizamos {}
usuarios = {
    "chaves": ["Chaves Silva","17/06/2017","Recep_01"],
    "quico":["Frederico Enrico Flores","03/06/2017","Raiox_02"]
}

#Adicionando objeto no dicionario de dados "usuarios" de maneira singular (objeto por objeto) 
usuarios["florinda"]=["Florinda Flores","26/11/2017","Recep_01"]
usuarios["florinda"]=["Florinda Flores","26/11/2016","Recep_01"] #Esta linha sobrescreverá o objeto "florinda" permanecendo os dados deste último

#Exibição do conteúdo do dicionario "usuarios"
print(usuarios) #Todos os objetos do dicionario "usuarios"
print("=========================")
print("Dados: ", usuarios.get("chaves")) #Dados apenas do usuario "chaves"
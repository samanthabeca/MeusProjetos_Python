#metodo para exibicao do menu
def exibirMenu():
    opcao = input("O que deseja realizar?\n" + 
                "<I> - Inserir um usuário\n" + 
                "<P> - Pesquisar um usuário\n" +
                "<E> - Excluir um usuário\n" + 
                "<L> - Listar os usuários\n" +
                "<S> - Sair\n" +
                "Opcao: ").upper()
    return opcao

def inserirUsuario(dicionario):
    chave = input("Digite o login: ").upper()
    dicionario[chave] = [input("Digite o nome: ").upper(),
                        input("Digite a última data de acesso: "),
                        input("Digite o nome da última estação acessada: ").upper()]
    
def pesquisar(dicionario,chave):
    lista = dicionario.get(chave) #Buscando o objeto conforme a chave informada e armazenando os dados em "lista"
    if lista != None: #Se a lista não estiver vazia
        print("Nome ...........: " + lista[0])
        print("Último acesso ..: " + lista[1])
        print("Última estação .: " + lista[2])
    else:
        print("Usuário não encontrado.")

def excluirUsuario(dicionario,chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
        print("Usuario excluído")
    else:
        print("Usuário inexistente.")

def listarUsuarios(dicionario):
    print("====== LISTA DE USUÁRIOS ======")
    if dicionario != {}:
        for chave, valor in dicionario.items():
            print("Usuário......")
            print("Login: ", chave)
            print("Nome: ", valor[0])
            print("Último acesso em: ", valor[1])
            print("Estação: ", valor[2])
            print("===============")
    else:
        print("Dicionario vazio.")
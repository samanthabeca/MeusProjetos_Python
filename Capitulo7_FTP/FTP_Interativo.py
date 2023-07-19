import os
from ftplib import *

ftp_ativo = False
ftp = FTP(input("Digite o FTP que deseja se conectar (Ex: ftp.datasus.gov.br, ftp.registro.br): ")) # Ex: ftp.datasus.gov.br, ftp.registro.br, ftp.ibiblio.org

print(ftp.getwelcome())
usuario = input("Digite o usuario: ")
senha = input("Digite a senha: ")
ftp.login(usuario, senha)
print("Conexão bem-sucedida. Diretório atual: ", ftp.pwd())

menu = "1"
while menu == "1" or menu == "2" or menu == "3":
    menu = input("Escolha a opção desejada:\n" +
                "<1> Listar arquivos\n" +
                "<2> Definir um diretório\n" +
                "<3> Baixar um arquivo\n" +
                "Opção: ")
    if menu == "1":
        print("========= Listar os Arquivos =========")
        print(ftp.retrlines('LIST'))
        print("========= || =========")
    elif menu == "2":
        print("========= Definir Diretorio =========")
        diretorio = input("Digite o diretório que deseja entrar: ")
        ftp.cwd(diretorio)
        print("Diretório corrente: ", ftp.pwd())
        print("========= || =========")
    elif menu == "3":
        print("========= Baixar Arquivo =========")
        tipo = input("Digite <B> para arquivo binário ou qualquer outra letra para arquivo " +
                     "ASCII: ").upper()
        if tipo == "B":
            with open(input("Digite o nome do arquivo destino: "), 'wb') as arq:
                ftp.retrbinary('RETR ' + input("Arquivo de origem: "), arq.write)
        else:
            with open(input("Digite o nome do arquivo destino: "), 'w') as arq:
                def escreverLinha(data):
                        arq.write(data) # Leitura no arquivo de origem e escrita das linhas no arquivo de destino que foi criado localmente
                        arq.write(os.linesep) # Identificação do sistema operacional quanto ao separador de linha utilizado dentro do arquivo
                ftp.retrlines('RETR ' + input("Arquivo de origem: "), escreverLinha) # O "arq" será escrito com base nesse arquivo 
        print("Arquivo baixado com sucesso!")
        print("========= || =========")
print("Conexão encerrada!")
ftp.quit()
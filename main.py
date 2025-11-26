from  core import verificar_credenciais, add_no_dict, listar

print("\n" + "*" * 40)
print("*         Bem-vindo ao Sistema!        *")
print("* Digite 0 a qualquer momento para sair*")
print("*" * 40 + "\n")

while True: #loop do aplicativo
    print("\n============================")
    nome = input("Insira o nome: ") #variavel que recebe o nome do usuario

    if nome == '0': #condicao para verificar quando o usuario deseja sair do sistema
        print("\n============================")
        print("Lista dos usuarios cadastrados")
        print("============================\n")
        break

    idade = input("Insira a idade: ") #variavel que recebe a idade do usuario
    email = input("Insira o email: ") #variavel que recebe o email do usuario

    if verificar_credenciais(nome, idade, email): #chama função que verifica se as variaveis atendem ao requisitos do sistema
        add_no_dict(nome, idade, email) #chama função que adiciona as variaveis, apos validas, no dicionario

listar() #chama função que lista os itens no dicionario
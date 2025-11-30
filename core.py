
# DICIONÁRIO PRINCIPAL
# Ele armazena todos os usuários no formato:
# usuarios = {
#     "nome" : {"idade": X, "email": "exemplo@dominio.com"}
# }
usuarios = {}

# FUNÇÃO DE VALIDAÇÃO

def verificar_credenciais(nome, idade, email):
    """
    Valida os dados inseridos pelo usuário.
    Retorna True se forem válidos, senão retorna False.
    """

    # Nome precisa ter mais de 1 caractere
    if len(nome) <= 1:
        print("Erro: Nome deve ter mais de 1 caractere.")
        return False

    # Idade precisa ser maior que 0
    if int(idade) <= 0:
        print("Erro: Idade deve ser maior que 0.")
        return False

    # Email deve conter '@dominio' conforme requisitos
    if "@" not in email or "." not in email:
        print("Erro: Email inválido. Deve conter '@dominio'.")
        return False

    # Se passou por todas as validações:
    return True

# FUNÇÃO QUE ADICIONA O USUÁRIO AO DICIONÁRIO
def add_no_dict(nome, idade, email):
    """
    Adiciona um novo usuário ao dicionário.
    Essa função será executado quando todas as validações acimas forem aprovadas.
    """

    usuarios[nome] = {
        "idade": idade,
        "email": email
    }

    print("Usuário cadastrado com sucesso!")

# FUNÇÃO QUE LISTA TODOS OS USUÁRIOS CADASTRADOS

def listar():
    """
    Exibe todos os usuários cadastrados no sistema.
    """
    
    # Verifica se há usuários cadastrados
    if not usuarios:
        print("Nenhum usuário foi cadastrado.")
        return

    print("\n===== LISTA DE USUÁRIOS CADASTRADOS =====")

    # Percorre o dicionário e mostra cada usuário
    for nome, dados in usuarios.items():
        print(f"\nNome: {nome}")
        print(f"Idade: {dados['idade']}")
        print(f"Email: {dados['email']}")
        print("---------------------------------------")

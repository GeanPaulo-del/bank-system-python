import json

# -------------------------------
# CARREGAR USUÁRIOS
# -------------------------------
def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            return json.load(arquivo)
    except:
        return {}

# -------------------------------
# SALVAR USUÁRIOS
# -------------------------------
def salvar_usuarios():
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo)

usuarios = carregar_usuarios()
usuario_logado = None

# -------------------------------
# CADASTRAR
# -------------------------------
def cadastrar():
    usuario = input("Digite um usuário: ")
    senha = input("Digite uma senha: ")

    if usuario in usuarios:
        print("Usuário já existe!")
    else:
        usuarios[usuario] = {"senha": senha, "saldo": 0}
        salvar_usuarios()
        print("Conta criada com sucesso!")

# -------------------------------
# LOGIN
# -------------------------------
def login():
    global usuario_logado

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        usuario_logado = usuario
        print(f"Bem-vindo, {usuario}!")
    else:
        print("Usuário ou senha incorretos!")

# -------------------------------
# MENU DO BANCO
# -------------------------------
def menu_banco():
    global usuario_logado

    while True:
        print("\n1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Logout")

        opcao = input("Escolha: ")

        if opcao == "1":
            print(f"Saldo: R$ {usuarios[usuario_logado]['saldo']:.2f}")

        elif opcao == "2":
            valor = float(input("Valor para depositar: "))

            if valor <= 0:
                print("Valor inválido!")
            else:
                usuarios[usuario_logado]["saldo"] += valor
                salvar_usuarios()
                print("Depósito realizado!")

        elif opcao == "3":
            valor = float(input("Valor para sacar: "))

            if valor <= 0:
                print("Valor inválido!")
            elif valor > usuarios[usuario_logado]["saldo"]:
                print("Saldo insuficiente!")
            else:
                usuarios[usuario_logado]["saldo"] -= valor
                salvar_usuarios()
                print("Saque realizado!")

        elif opcao == "4":
            usuario_logado = None
            print("Logout realizado!")
            break

        else:
            print("Opção inválida!")

# -------------------------------
# MENU PRINCIPAL
# -------------------------------
while True:
    print("\n1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        login()
        if usuario_logado:
            menu_banco()

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
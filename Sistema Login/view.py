from controller import CadastroController, LoginController

while True:
    print('---------- MENU ----------')
    print('[1] Cadastro de usuário')
    print('[2] Login no sistema')
    print('[9] Sair')
    opcao = int(input("Opção: "))

    if opcao == 1:
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")

        resultado = CadastroController.novoCadastro(nome, email, senha)

        if resultado == 2:
            print("Nome digitado inválido.")
        elif resultado == 3:
            print("E-mail maior que 200 caractéres.")
        elif resultado == 4:
            print("Tamano da senha digitada inválida, necessário maior que 6 caractéres..")
        elif resultado == 5:
            print("E-mail informado já cadastrado no sistema.")
        elif resultado == 6:
            print("Erro interno do sistema.")
        elif resultado == 1:
            print("Cadastro realizado com sucesso.")
    elif opcao == 2:
        print('Informe os dados para login: ')
        email = input("E-mail: ")
        senha = input("Senha: ")

        resultado = LoginController.login(email, senha)

        if not resultado:
            print("Email ou senha incorretos.")
        else:
            print(resultado)

    else:
        break
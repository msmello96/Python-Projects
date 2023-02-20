import controller
import os.path

def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write("")


criarArquivos("dados/categorias.txt", "dados/clientes.txt", "dados/estoque.txt", 
"dados/fornecedores.txt", "dados/funcionarios.txt", "dados/vendas.txt")


if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar ( Categorias )\n"
                          "Digite 2 para acessar ( Estoque )\n"
                          "Digite 3 para acessar ( Fornecedores )\n"
                          "Digite 4 para acessar ( Clientes )\n"
                          "Digite 5 para acessar ( Funcionarios )\n"
                          "Digite 6 para acessar ( Vendas )\n"
                          "Digite 7 para ver os produtos mais vendidos\n"
                          "Digite 9 para sair do sistema\n"
                          "Opção: "))
        
        if local == 1:
            cat = controller.CategoriaController()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma categoria\n"
                                    "Digite 2 para remover uma categoria\n"
                                    "Digite 3 para alterar uma categoria\n"
                                    "Digite 4 para mostrar as categorias cadastradas\n"
                                    "Digite 5 para sair\n"
                                    "Opção: "))
                
                if decidir == 1:
                    categoria = input("Digite a categoria que deseja cadastrar: ")
                    cat.cadastrarCategoria(categoria)
                elif decidir == 2:
                    categoria = input("Digite a categoria que deseja remover: ")
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input("Digite a categoria que deseja alterar: ")
                    novaCategoria = input("Digite a categoria para qual deseja alterar: ")
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break
        elif local == 2:
            est = controller.EstoqueController()
            while True:
                decidir = int(input("Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para remover um produto\n"
                                    "Digite 3 para alterar um produto\n"
                                    "Digite 4 para mostrar os produto cadastrados\n"
                                    "Digite 5 para sair\n"
                                    "Opção: "))
                
                if decidir == 1:
                    produto = input("Digite o produto que deseja cadastrar: ")
                    preco = input("Digite o preco do produto: ")
                    categoria = input("Digite a categoria: ")
                    quantidade = input("Digite a quantidade: ")
                    est.cadastrarProduto(produto, preco, categoria, quantidade)
                elif decidir == 2:
                    produto = input("Digite a produto que deseja remover: ")
                    est.removerProduto(produto)
                elif decidir == 3:
                    produto = input("Digite o produto que deseja alterar: ")
                    novoProduto = input("Digite o produto para qual deseja alterar: ")
                    novoPreco = input("Digite o preço: ")
                    novaCategoria = input("Digite a categoria: ")
                    novaQuantidade = input("Digite a quantidade: ")
                    est.alterarProduto(produto, novoProduto, novoPreco, novaCategoria, novaQuantidade)
                elif decidir == 4:
                    est.mostrarEstoque()
                else:
                    break
        elif local == 3:
            forn = controller.FornecedorController()
            while True:
                decidir = int(input("Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para remover um fornecedor\n"
                                    "Digite 3 para alterar um fornecedor\n"
                                    "Digite 4 para mostrar os fornecedor cadastrados\n"
                                    "Digite 5 para sair\n"
                                    "Opção: "))
                
                if decidir == 1:
                    cnpj = input("Digite o CNPJ do fornecedor que deseja cadastrar: ")
                    nome = input("Digite o nome do fornecedor: ")
                    telefone = input("Digite o telefone: ")
                    categoria = input("Digite a categoria: ")
                    forn.cadastrarFornecedor(cnpj, nome, telefone, categoria)
                elif decidir == 2:
                    cnpj = input("Digite o CNPJ do fornecedor que deseja remover: ")
                    forn.removerFornecedor(cnpj)
                elif decidir == 3:
                    cnpj = input("Digite o CNPJ que deseja alterar: ")
                    novoCnpj = input("Digite o novo CNPJ do fornecedor:: ")
                    novoNome = input("Digite o novo nome do fornecedor: ")
                    novoTelefone = input("Digite o telefone: ")
                    novaCategoria = input("Digite a categoria: ")
                    forn.alterarFornecedor(cnpj, novoCnpj, novoNome, novoTelefone, novaCategoria)
                elif decidir == 4:
                    forn.mostrarFornecedor()
                else:
                    break
        elif local == 4:
            cli = controller.ClienteController()
            while True:
                decidir = int(input("Digite 1 para cadastrar um cliente\n"
                                    "Digite 2 para remover um cliente\n"
                                    "Digite 3 para alterar um cliente\n"
                                    "Digite 4 para mostrar os clientes cadastrados\n"
                                    "Digite 5 para sair\n"
                                    "Opção: "))
                
                if decidir == 1:
                    nome = input("Digite o nome do cliente que deseja cadastrar: ")
                    telefone = input("Digite o telefone: ")
                    cpf = input("Digite o CPF: ")
                    email = input("Digite o e-mail: ")
                    endereco = input("Digite o endereço: ")
                    cli.cadastrarCliente(nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    cpf = input("Digite o CPF do cliente que deseja remover: ")
                    cli.removerCliente(cpf)
                elif decidir == 3:
                    cpf = input("Digite o CPF que deseja alterar: ")
                    novoNome = input("Digite o nome do cliente que deseja cadastrar: ")
                    novoTelefone = input("Digite o telefone: ")
                    novoCpf = input("Digite o CPF: ")
                    novoEmail = input("Digite o e-mail: ")
                    novoEndereco = input("Digite o endereço: ")
                    cli.alterarCliente(cpf, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    cli.mostrarCliente()
                else:
                    break
        elif local == 5:
            func = controller.FuncionarioController()
            while True:
                decidir = int(input("Digite 1 para cadastrar um funcionario\n"
                                    "Digite 2 para remover um funcionario\n"
                                    "Digite 3 para alterar um funcionario\n"
                                    "Digite 4 para mostrar os funcionario cadastrados\n"
                                    "Digite 5 para sair\n"
                                    "Opção: "))
                
                if decidir == 1:
                    clt = input("Digite a CLT do funcionário que deseja cadastrar: ")
                    nome = input("Digite o nome do funcionario que deseja cadastrar: ")
                    telefone = input("Digite o telefone: ")
                    cpf = input("Digite o CPF: ")
                    email = input("Digite o e-mail: ")
                    endereco = input("Digite o endereço: ")
                    func.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    clt = input("Digite a CLT do funcionario que deseja remover: ")
                    func.removerFuncionario(clt)
                elif decidir == 3:
                    cpf = input("Digite a CLT que deseja alterar: ")
                    novaClt = input("Digite a CLT do funcionário que deseja cadastrar: ")
                    novoNome = input("Digite o nome do funcionario que deseja cadastrar: ")
                    novoTelefone = input("Digite o telefone: ")
                    novoCpf = input("Digite o CPF: ")
                    novoEmail = input("Digite o e-mail: ")
                    novoEndereco = input("Digite o endereço: ")
                    func.alterarFuncionario(cpf, novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    func.mostrarFuncionario()
                else:
                    break
        elif local == 6:
            vend = controller.VendaController()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma venda\n"
                                    "Digite 2 para mostrar as vendas\n"
                                    "Digite 3 para sair\n"
                                    "Opção: "))
                
                if decidir == 1:
                    # nomeProduto, vendedor, comprador, quantidadeVendida
                    nomeProduto = input("Digite o nome do produto que deseja vender: ")
                    vendedor = input("Digite o vendedor: ")
                    comprador = input("Digite o comprador: ")
                    quantidadeVendida = int(input("Digite a quantidade vendida: "))
                    vend.cadastrarVenda(nomeProduto, vendedor, comprador, quantidadeVendida)
                elif decidir == 2:
                    dataInicio = input("Informe a data de início: ")
                    dataFim = input("Informe a data final: ")
                    vend.mostrarVenda(dataInicio, dataFim)
                else:
                    break
        elif local == 7:
            vend = controller.VendaController()
            vend.relatorioProdutos()
        else:
            break
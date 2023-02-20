from models import *
from dao import *

class CategoriaController:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        cat = CategoriaDao.ler()

        for i in cat:
            if i.categoria == novaCategoria:
                existe = True
        
        if not existe:
            CategoriaDao.salvar(novaCategoria)
            print('Categoria salva com sucesso.')
        else:
            print('A nova categoria que deseja cadastrar já existe')

    def removerCategoria(self, categoriaRemover):
        x = CategoriaDao.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <= 0:
            print('A categoria que deseja remover não existe.')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso.')

            with open('dados/categorias.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
        
        estoque = EstoqueDao.ler()

        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, "Sem Categoria"), x.quantidade) if (x.produto.categoria == categoriaRemover) else (x), estoque))

        with open('dados/estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + 
                i.produto.categoria + "|" + str(i.quantidade)) 
                arq.writelines('\n')
    
    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = CategoriaDao.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                print('Categoria alterada com sucesso.')
                
                estoque = EstoqueDao.ler()

                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade) 
                if (x.produto.categoria == categoriaAlterar) else (x), estoque))

                with open('dados/estoque.txt', 'w') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + 
                        i.produto.categoria + "|" + str(i.quantidade)) 
                        arq.writelines('\n')
            else:
                print('A categoria para qual deseja alterar já existe.')
        else:
            print('A categoria que deseja alterar não existe.')
        
        with open('dados/categorias.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = CategoriaDao.ler()
        if len(categorias) == 0:
            print('Categorias vazia.')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')

class EstoqueController:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = EstoqueDao.ler()
        y = CategoriaDao.ler()

        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                EstoqueDao.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso.')
            else:
                print('Produto já existe no estoque.')
        else:
            print('Categoria inexistente.')

    def removerProduto(self, nome):
        x = EstoqueDao.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    print('Produto removido com sucesso.')
                    break
        else:
            print('O produto que deseja remover não existe.')

        with open('dados/estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + 
                i.produto.categoria + "|" + str(i.quantidade)) 
                arq.writelines('\n')
    
    def alterarProduto(self, nomeAlterar, noveNome, novoPreco, novaCategoria, novaQuantidade):
        x = EstoqueDao.ler()
        y = CategoriaDao.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == noveNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(noveNome, novoPreco, novaCategoria), novaQuantidade) if(x.produto.nome == nomeAlterar) else(x), x))
                    print('Produto alterado com sucesso.')
                else:
                    print('Produto já cadastrado.')
            else:
                print('O produto que deseja alterar não existe.')
            
            with open('dados/estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + 
                    i.produto.categoria + "|" + str(i.quantidade)) 
                    arq.writelines('\n')

        else:
            print('A categoria informada não existe.')

    def mostrarEstoque(self):
        estoque = EstoqueDao.ler()
        if len(estoque) == 0:
            print('Estoque vazio.')
        else:
            print('===== Prdutos =====')
            for i in estoque:
                print(f"Nome: {i.produto.nome}\n"
                      f"Preço: {i.produto.preco}\n"
                      f"Categoria: {i.produto.categoria}\n"
                      f"Quantidade: {i.quantidade}"
                      )
                print('--------------------------------')

class VendaController:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = EstoqueDao.ler()
        temp =[]
        existe = False
        quantidade = False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Vendas(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)

                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                        VendasDao.salvar(vendido)

            temp.append(Estoque(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))

        arq = open('dados/estoque.txt', 'w')
        arq.write("")

        for i in temp:
            with open('dados/estoque.txt', 'a') as arq:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')
        
        if existe == False:
            print('O Produto não existe')
            return None
        elif not quantidade:
            print('A quantidade vendida não tem contém em estoque.')
            return None
        else:
            return valorCompra

    def relatorioProdutos(self):
        vendas = VendasDao.ler()
        produtos = []

        for i in vendas:
            nome = i.itensVendidos.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))

            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)} 
                if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})
            
        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)

        print('Esses são os produtos mais vendidos: ')

        a = 1
        for i in ordenado:
            print(f"====== Produto [{a}] ======")
            print(f"Produto: {i['produto']}\n"
                    f"Quantidade: {i['quantidade']}\n")
            a += 1

    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = VendasDao.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1 and 
                                         datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas))
        cont = 1
        total = 0

        for i in vendasSelecionadas:
            print(f"====== Venda [{cont}] ======\n")
            print(f"Nome: {i.itensVendidos.nome}\n"
                  f"Categoria: {i.itensVendidos.categoria}\n"
                  f"Data: {i.data}\n"
                  f"Quantidade: {i.quantidadeVendida}\n"
                  f"Cliente: {i.comprador}\n"
                  f"Vendedor: {i.vendedor}\n")
            total += int(i.itensVendidos.preco) * int(i.quantidadeVendida)
            cont += 1
        
        print (f"Total vendido: ${total}")

class FornecedorController:
    def cadastrarFornecedor(self, cnpj, nome, telefone, categoria):
        x = FornecedorDao.ler()

        forn = list(filter(lambda x: x.cnpj == cnpj, x))

        if len(forn) == 0:
            if len(cnpj) >= 10 and len(nome) > 3:
                FornecedorDao.salvar(Fornecedor(cnpj, nome, telefone, categoria))
                print("Fornecedor cadastrado com sucesso.")
            else:
                print("Dados informados inválidos. Verifique o CNPJ ou Nome.")
        else:
            print("Fornecedor já está cadastrado.")

    def removerFornecedor(self, cnpj):
        x = FornecedorDao.ler()
        
        forn = list(filter(lambda x: x.cnpj == cnpj, x))

        if len(forn) > 0:
            for i in range(len(x)):
                if x[i].cnpj == cnpj:
                    del x[i]
                    print("CNPJ removido com sucesso")
                    break
        else:
            print("O Cnpj informado não existe cadastrado.")
        
        with open('dados/fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.cnpj + "|" + i.nome  + "|" + 
                i.telefone  + "|" + i.categoria)
                arq.writelines('\n')
    
    def alterarFornecedor(self, cnpjAlterar, novoCnpj, novoNome, novoTelefone, novoCategoria):
        x = FornecedorDao.ler()

        forn = list(filter(lambda x: x.cnpj == cnpjAlterar, x))

        if len(forn) > 0:
            x = list(map(lambda x: Fornecedor(novoCnpj, novoNome, novoTelefone, novoCategoria) if(x.cnpj == cnpjAlterar) else(x), x))
            print("CNPJ Alterado com sucesso.")
        else:
            print("O CNPJ que deseja alterar não existe.")

        with open('dados/fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.cnpj + "|" + i.nome  + "|" + 
                i.telefone  + "|" + i.categoria)
                arq.writelines('\n')

    def mostrarFornecedor(self):
        fornecedores = FornecedorDao.ler()
        x = 1

        if len(fornecedores) == 0:
            print("Lista de fornecedores vazia.")
        else:
            print("====== Fornecedores =====")
            for i in fornecedores:
                print(f'----- Fornecedor [{x}] -----\n'
                    f'CNPJ: {i.cnpj}\n'
                    f'Nome: {i.nome}\n'
                    f'Telefone: {i.telefone}\n'
                    f'Categoria: {i.categoria}')
                x += 1

class ClienteController:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = PessoaDao.ler()

        cliente = list(filter(lambda x: x.cpf == cpf, x))
        clienteEmail = list(filter(lambda x: x.email == email, x))

        if len(cpf) == 11 and len(nome) > 2:
            if len(cliente) == 0:
                if len(clienteEmail) == 0:
                    PessoaDao.salvar(Pessoas(nome, telefone, cpf, email, endereco))
                    print("Cliente cadastrado com sucesso.")
                else:
                    print("Email já cadastrado no sistema.")
            else:
                print("Cliente já está cadastrado")
        else:
            print("Dados informados incorretos.")
    
    def removerCliente(self, cpf):
        x = PessoaDao.ler()

        cliente = list(filter(lambda x: x.cpf == cpf, x))

        if len(cliente) > 0:
            for i in range(len(x)):
                if x[i].cpf == cpf:
                    del x[i]
                    print("Cliente removido com sucesso.")
                    break
        else:
            print("O CPF Informado não existe.")
        
        with open('dados/clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + 
                i.email + "|" + i.endereco)
                arq.writelines('\n')

    def alterarCliente(self, cpfAlterar, novoNome, novoTelefone, novoCPF, novoEmail, novoEndereco):
        x = PessoaDao.ler()

        cliente = list(filter(lambda x: x.cpf == cpfAlterar, x))
        clienteEmail = list(filter(lambda x: x.email == novoEmail, x))

        if len(cliente) > 0:
            if len(novoCPF) == 11 and len(novoNome) > 2:
                if len(clienteEmail) == 0:
                    x = list(map(lambda x: Pessoas(novoNome, novoTelefone, novoCPF, novoEmail, novoEndereco) if(x.cpf == cpfAlterar) else(x), x))
                    print("Cliente alterado com sucesso.")
                else:
                    print("O email informado já existe no cadastro.")
            else:
                print("As infomações passadas estão incorretas, verifique o CPF ou nome.")
        else:
            print("O CPF informado não está cadastrado.")
        
        with open('dados/clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + 
                i.email + "|" + i.endereco)
                arq.writelines('\n')

    def mostrarCliente(self):
        clientes = PessoaDao.ler()

        x = 1

        if len(clientes) == 0:
            print("Cadastro de pessoas ainda está vazio.")
        else:
            print("===== Cadastro de Clientes =====")
            for i in clientes:
                print(f'----- Cliente [{x}] -----')
                print(f'Nome: {i.nome}\n'
                    f'Telefone: {i.telefone}\n'
                    f'CPF: {i.cpf}\n'
                    f'E-mail: {i.email}\n'
                    f'Endereço: {i.endereco}'
                )
                x += 1

class FuncionarioController:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = FuncionariosDao.ler()

        func = list(filter(lambda x: x.clt == clt, x))

        if len(func) == 0:
            if len(clt) == 9 and len(cpf) == 11 and len(nome) > 2:
                FuncionariosDao.salvar(Funcionarios(clt, nome, telefone, cpf, email, endereco))
                print('Funcionario cadastrado com sucesso.')
            else:
                print('As informações informadas estão incorretas.')
        else:
            print('Funcionario já cadastrado no sistema.')

    def removerFuncionario(self, clt):
        x = FuncionariosDao.ler()

        func = list(filter(lambda x: x.clt == clt, x))

        if len(func) > 0:
            for i in range(len(x)):
                if x[i].clt == clt:
                    del x[i]
                    print('Funcionario removido com sucesso.')
                    break
        else:
            print('O numero da CLT informada não existe no sistema.')

        with open('dados/funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + 
                i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')

    def alterarFuncionario(self, cltAlterar, novoClt, novoNome, novoTelefone, novoCPF, novoEmail, novoEndereco):
        x = FuncionariosDao.ler()

        func = list(filter(lambda x: x.clt == cltAlterar, x))

        if len(func) > 0:
            if len(novoClt) == 9 and len(novoCPF) == 11 and len(novoNome) > 2:
                x = list(map(lambda x: Funcionarios(novoClt, novoNome, novoTelefone, novoCPF, novoEmail, novoEndereco) if(x.clt == cltAlterar) else(x), x))
                print('Funcionario alterado com sucesso.')
            else:
                print('As informações passadas estão incorretas, favor verificar.')
        else:
            print('A CLT informada não existe no sistema')

        
        with open('dados/funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + 
                i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')

    def mostrarFuncionario(self):
        funcionarios = FuncionariosDao.ler()

        x = 1

        if len(funcionarios) == 0:
            print("Cadastro de funcionarios ainda está vazio.")
        else:
            print("===== Cadastro de funcionarios =====")
            for i in funcionarios:
                print(f'----- Funcionario [{x}] -----')
                print(f'CLT: {i.clt}\n'
                    f'Nome: {i.nome}\n'
                    f'Telefone: {i.telefone}\n'
                    f'CPF: {i.cpf}\n'
                    f'E-mail: {i.email}\n'
                    f'Endereço: {i.endereco}'
                )
                x += 1

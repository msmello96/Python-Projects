from models import Pessoas, Funcionarios, Categoria, Produtos, Estoque, Vendas, Fornecedor

class PessoaDao:
    @classmethod
    def salvar(cls, pessoa: Pessoas):
        with open('dados/clientes.txt', 'a') as arq:
            arq.writelines(pessoa.nome + "|" + pessoa.telefone + "|" + pessoa.cpf + "|" + 
            pessoa.email + "|" + pessoa.endereco)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('dados/clientes.txt', 'r') as arq:
            cls.clientes = arq.readlines()
        
        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

        clientes = []

        for i in cls.clientes:
            clientes.append(Pessoas(i[0], i[1], i[2], i[3], i[4]))
        
        return clientes

class FuncionariosDao:
    @classmethod
    def salvar(cls, funcionario: Funcionarios):
        with open('dados/funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.clt + "|" + funcionario.nome + "|" + funcionario.telefone + "|" + 
            funcionario.cpf + "|" + funcionario.email + "|" + funcionario.endereco)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('dados/funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()
        
        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

        func = []

        for i in cls.funcionarios:
            func.append(Funcionarios(i[0], i[1], i[2], i[3], i[4], i[5]))
        
        return func        

class CategoriaDao:
    @classmethod
    def salvar(cls, categoria):
        with open('dados/categorias.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('dados/categorias.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        
        cat = []

        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat

class EstoqueDao:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('dados/estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + "|" + produto.preco + "|" + 
            produto.categoria + "|" + str(quantidade)) 
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('dados/estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
        
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2]), int(i[3])))
        return est

class VendasDao:
    @classmethod
    def salvar(cls, vendas: Vendas):
        with open('dados/vendas.txt', 'a') as arq:
            arq.writelines(vendas.itensVendidos.nome  + "|" + vendas.itensVendidos.preco + "|" + 
            vendas.itensVendidos.categoria + "|" + vendas.vendedor + "|" + vendas.comprador + "|" + 
            str(vendas.quantidadeVendida)+ "|" + vendas.data)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('dados/vendas.txt', 'r') as arq:
            cls.vendas = arq.readlines()
        
        cls.vendas = list(map(lambda x: x.replace('\n', ''), cls.vendas))
        cls.vendas = list(map(lambda x: x.split('|'), cls.vendas))

        venda = []
        for i in cls.vendas:
            venda.append(Vendas(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return venda

class FornecedorDao:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('dados/fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.cnpj + "|" + fornecedor.nome  + "|" + 
            fornecedor.telefone  + "|" + fornecedor.categoria)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('dados/fornecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()

        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))
        
        forn = []

        for i in cls.fornecedores:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
        
        return forn

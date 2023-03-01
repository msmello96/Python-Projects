from clientes import Pessoa
from produtos import Produto
from typing import List, Dict
from time import sleep
from utils import formata_float_str_moeda

produtos: List[Produto] = []
clientes: List[Pessoa] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('############################')
    print('----- Bem vindo a Loja -----')
    print('----------------------------')
    print('- Informe a opção desejada -')
    print(' 1 - Cadastrar produto')
    print(' 2 - Cadastrar cliente')
    print(' 3 - Listar Produtos')
    print(' 4 - Listar Clientes')
    print(' 5 - Ajustar estoque')
    print(' 6 - Comprar Produtos')
    print(' 7 - Visualizar Carrinho')
    print(' 8 - Fechar Pedido')
    print(' 9 - Sair do sistema')
    opcao = int(input(' Opçao desejada: '))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        cadastrar_cliente()
    elif opcao == 3:
        listar_produtos()
    elif opcao == 4:
        listar_clientes()
    elif opcao == 5:
        ajustar_estoque()
    elif opcao == 6:
        comprar_produto()
    elif opcao == 7:
        visualizar_carrinho()
    elif opcao == 8:
        fechar_pedido()
    elif opcao == 0:
        print(carrinho[0])
    elif opcao == 9:
        print('Saindo do sistema.')
        sleep(1)
        exit(0)
    else:
        print('Opção inválida. Tente novamente.')
        menu()


def cadastrar_produto() -> None:
    opcao = True
    while opcao:
        print('Digite as informações para cadastrar o produto: ')
        nome_produto: str = input('Nome do produto: ')
        tipo_produto: str = input('Qual o tipo do produto: ')
        preco_produto: float = float(input('Qual o preço do produto: '))
        quantidade_produto: int = int(input('Quantidade para cadastro: '))

        produto: Produto = validar_produto_cadastrado(nome_produto)

        if produto:
            print('Produto já está cadastrado no sistema.')
            sleep(2)
            opcao = int(input('Deseja cadastrar um novo produto? 1 - Sim | 0 - Não. \nOpção :'))
            if opcao == 1:
                cadastrar_produto()
            else:
                print('Voltando para o menu principal.')
                sleep(2)
                menu()
        else:
            cadastro: Produto = Produto(nome_produto, tipo_produto, preco_produto, quantidade_produto)
            produtos.append(cadastro)
            print('Produto cadastrado com sucesso.')

        opcao = int(input('Deseja cadastrar novo produto? 1 - Sim | 0 - Não \nOpção: '))

        if opcao == 0:
            print('Voltando para o menu inicial.')
            sleep(2)
            opcao = False
            menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos: ')
        print('-------------------------')
        for produto in produtos:
            print(produto)
            print('-------------------------')
            sleep(1)
        menu()
    else:
        print('Ainda não há produtos cadastrados.')
        sleep(1)
        menu()


def ajustar_estoque():
    opcao = int(input('Escolha a opção desejada: \n[1] Adicionar quantidade \n[2] Subtrair quantidade '
                      '\n[0] Voltar para o Menu Principal \nOpção desejada: '))
    if opcao == 1:
        add_produto: str = input('Digite o nome do produto que deseja adicionar a quantidade: ')

        produto: Produto = validar_produto_cadastrado(add_produto)

        if produto:
            produto.mostra_nome()
            produto.mostra_quantidade()
            qtd: int = int(input('Deseja adicionar quantas unidades do produto? '))
            if qtd < 0:
                print('Quantidade informada inválida, tente novamente.')
                sleep(2)
                ajustar_estoque()
            else:
                produto.adicionar_estoque(qtd)
                sleep(2)
                opcao = int(input('Deseja ajustar outro produto? \n[1] Sim \n[0] Não \nOpção: '))
                if opcao == 1:
                    ajustar_estoque()
                elif opcao == 0:
                    print('Voltando para o menu inicial.')
                    menu()
                else:
                    print('Opção inválida')
                    menu()
        else:
            print('Produto não está cadastrado.')
            sleep(2)
            ajustar_estoque()
    elif opcao == 2:
        subtrair_produto: str = input('Digite o nome do produto que deseja subtrair a quantidade: ')

        produto: Produto = validar_produto_cadastrado(subtrair_produto)

        if produto:
            produto.mostra_nome()
            produto.mostra_quantidade()
            qtd: int = int(input('Informe a quantidade que deseja subtrair: '))
            if qtd < 0:
                print('Quantidade informada inválida, tente novamente.')
                sleep(2)
                ajustar_estoque()
            else:
                produto.subtrair_estoque(qtd)
                sleep(2)
                opcao = int(input('Deseja ajustar outro produto? \n[1] Sim \n[0] Não \nOpção: '))
                if opcao == 1:
                    ajustar_estoque()
                elif opcao == 0:
                    print('Voltando para o menu inicial.')
                    menu()
                else:
                    print('Opção inválida')
                    menu()
        else:
            print('Produto não está cadastrado.')
            sleep(2)
            ajustar_estoque()
    elif opcao == 0:
        print('Voltando para o Menu Principal.')
        sleep(2)
        menu()
    else:
        print('Opcao inválida')


def validar_produto_cadastrado(nome: str) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.nome.title() == nome.title():
            p = produto
    return p


def cadastrar_cliente() -> None:
    opcao = True
    while opcao:
        print('Digite as informações para cadastro: ')
        cadastro_nome: str = input('Nome: ')
        cadastro_cpf: int = int(input('CPF: '))
        cadastro_idade: int = int(input('Idade: '))
        cadastro_email: str = input('E-mail: ')
        cadastro_endereco: str = input('Endereço: ')

        cliente: Pessoa = validar_cliente_cadastrado(cadastro_cpf)

        if cliente:
            print('Cliente já cadastrado no sistema.')
            sleep(2)
            opcao = int(input('Deseja cadastrar um novo cliente? 1 - Sim | 0 - Não. \nOpção: '))
            if opcao == 1:
                cadastrar_cliente()
            else:
                print('Voltando para o menu principal.')
                sleep(2)
                menu()
        else:
            cadastro: Pessoa = Pessoa(cadastro_nome, cadastro_cpf, cadastro_idade, cadastro_email, cadastro_endereco)
            clientes.append(cadastro)
            print('Cliente cadastrado com sucesso.')
            sleep(1)

        opcao = int(input('Deseja cadastrar novo cliente? 1 - Sim | 0 - Não \nOpção: '))

        if opcao == 0:
            print('Voltando para o menu inicial.')
            sleep(2)
            opcao = False
            menu()


def listar_clientes() -> None:
    if len(clientes) > 0:
        print('Listagem de Clientes: ')
        print('-------------------------')
        for cliente in clientes:
            print(cliente)
            print('-------------------------')
            sleep(2)
        menu()
    else:
        print('Ainda não há clientes cadastrados.')
        sleep(1)
        menu()


def validar_cliente_cadastrado(cpf: int) -> Pessoa:
    p: Pessoa = None

    for pessoa in clientes:
        if pessoa.cpf == cpf:
            p = pessoa
    return p


def comprar_produto():
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('##################### PRODUTOS DISPONIVEIS #####################')

        for produto in produtos:
            print(produto)
            print('--------------------')
            sleep(1)
        codigo: int = int(input('Código do produto desejado: '))

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        qtd_add = int(input('Digite a quantidade que deseja adicionar ao carrinho: '))
                        item[produto] = quant + qtd_add
                        print(f'O produto {produto.nome} agora possui {quant + qtd_add} unidades no carirnho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    quantidade_compra: int = int(input('Quantidade que deseja comprar do produto: '))
                    prod = {produtos: quantidade_compra}
                    print(prod)
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
            else:
                quantidade_compra: int = int(input('Quantidade que deseja comprar do produto: '))
                item = {produto: quantidade_compra}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com o código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para venda.')
        sleep(2)
        menu()


def visualizar_carrinho():
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(f'Produto: {dados[0].nome}')
                print(f'Quantidade: {dados[1]}')
                print('------------------------------')
                sleep(1)
                menu()
    else:
        print('Ainda não foram adicionados produtos no carrinho.')
        sleep(2)
        menu()


def fechar_pedido():

    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos no carrinho: ')
        for item in carrinho:
            for dados in item.items():
                print(f'Produto: {dados[0].nome}')
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                subtrair_produto = dados[0].nome
                produto: Produto = validar_produto_cadastrado(subtrair_produto)
                produto.subtrair_estoque(dados[1])
                print('#######################')
                sleep(1)
        print(f'O valor da compra é: {formata_float_str_moeda(valor_total)}')
        print('Obrigado e volte sempre!')
        print('-------------------------------')
        carrinho.clear()
        opcao = int(input('Deseja voltar ao menu inicial? 1 - Sim | 0 - Não \nOpção: '))

        if opcao == 1:
            print('Voltando para o menu inicial.')
            sleep(2)
            menu()
        sleep(2)
    else:
        print('Ainda não existem produtos no carrinho.')
        sleep(2)
        menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()

from time import sleep


class Produto:

    id = 0

    def __init__(self: object, nome: str, tipo: str, preco: float, quantidade: int) -> None:
        self.__codigo = Produto.id + 1
        self.__nome = nome
        self.__tipo = tipo
        self.__preco = preco
        self.__quantidade = quantidade
        Produto.id += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def tipo(self: object) -> str:
        return self.__tipo

    @property
    def preco(self: object) -> float:
        return self.__preco

    @property
    def quantidade(self: object) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self: object, valor: int) -> None:
        self.__quantidade = valor

    def adicionar_estoque(self: object, valor: int) -> None:
        if valor > 0:
            self.quantidade = self.quantidade + valor
            print('Adicionado no estoque com sucesso.')
        else:
            print('Erro ao efetuar inclusão no sistema. Tente novamente.')

    def subtrair_estoque(self: object, valor: int) -> None:
        if valor > 0 and self.quantidade >= valor:
            if self.quantidade >= valor:
                self.quantidade = self.quantidade - valor
                print('Subtraido no estoque com sucesso.')
            else:
                print('Não foi possível realizar a correção. Tente novamente.')
        else:
            print('Quantidade informada inválida ou maior que o estoque.')

    def mostra_nome(self):
        print('Produto selecionado: ', self.__nome)

    def mostra_quantidade(self):
        print('Quantidade em estoque: ', self.__quantidade)

    def __str__(self: object) -> str:
        sleep(1)
        return f'Código: {self.codigo} \nNome: {self.nome} \nTipo: {self.tipo} \nPreco: {self.preco}g ' \
               f'\nQuantidade: {self.quantidade}.'

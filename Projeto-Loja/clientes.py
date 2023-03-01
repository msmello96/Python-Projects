from time import sleep


class Pessoa:
    id = 0

    def __init__(self: object, nome: str, cpf: int, idade: int, email: str, endereco: str) -> None:
        self.__codigo = Pessoa.id + 1
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__email = email
        self.__endereco = endereco
        Pessoa.id += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    # @nome.setter
    # def nome(self: object, nome):
    #     self.__nome = nome

    @property
    def cpf(self: object) -> int:
        return self.__cpf

    @property
    def idade(self: object) -> int:
        return self.__idade

    # @idade.setter
    # def idade(self: object, idade):
    #     self.__idade = idade

    @property
    def email(self: object) -> str:
        return self.__email

    # @email.setter
    # def email(self:object, email):
    #     self.__email = email

    @property
    def endereco(self: object) -> str:
        return self.__endereco

    # @endereco.setter
    # def endereco(self:object, endereco):
    #     self.__endereco = endereco

    def __str__(self: object) -> str:
        sleep(1)
        print('--------------------')
        return f'\nCódigo do cadastro: {self.codigo} \nNome: {self.nome} \nCPF: {self.cpf} \nIdade: {self.idade} ' \
               f'\nE-mail: {self.email} \nEndereco: {self.endereco}'

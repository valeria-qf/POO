from cidade import Cidade
'''Para um ou mais aeroportos existirem, precisa haver uma cidade'''
class Aeroporto:

    '''Método Construtor para classe Aeroporto'''
    def __init__(self, nome: str, capacidade_decolagens: int, endereco: Cidade) -> None:
        self.__nome = nome
        self.__capacidade_decolagens = capacidade_decolagens
        self.__endereco = endereco

    def __str__(self) -> str:
        return '\nNome do Aeroporto: {} \nCapacidade de decolagens: {} \nLocalização: {}'.format(self.get_nome(), self.get_capacidade_decolagens(),self.get_endereco())

    '''getters'''
    def get_nome(self) -> str:
        return self.__nome

    def get_capacidade_decolagens(self) -> int:
        return self.__capacidade_decolagens

    def get_endereco(self) -> str:
        return self.__endereco

    '''setters'''
    def set_nome(self, other: str) -> None:
        self.__nome = other

    def set_capacidade_decolagens(self, other: int) -> None:
        self.__capacidade_decolagens = other

    def set_endereco(self, other: Cidade) -> None:
        self.__endereco = other

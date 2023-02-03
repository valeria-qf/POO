class Cidade:

    def __init__(self, nome: str, estado: str, pais: str) -> None:
        self.__nome = nome
        self.__estado = estado
        self.__pais = pais

    def __str__(self) -> str:
        return 'Cidade: {}, Estado: {}, País: {}\n'.format(self.get_nome_cidade(), self.get_estado(), self.get_pais())

    '''Métodos Getters'''
    def get_nome_cidade(self) -> str:
        return self.__nome
    
    def get_estado(self) -> str:
        return self.__estado
    
    def get_pais(self) -> str:
        return self.__pais

    '''Métodos Setters'''
    def set_nome_cidade(self, other: str) -> None:
        self.__nome = other
    
    def set_estado(self, other: str) -> None:
        self.__estado = other
    
    def set_pais(self, other: str) -> None:
        self.__pais = other

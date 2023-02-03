class Tripulante:
    def __init__(self, nome, cargo) -> None:
        self.__nome = nome
        self.__cargo = cargo

    def get_nome(self):
        return self.__nome
    
    def get_cargo(self):
        return self.__cargo

    def set_nome(self, other):
        self.__nome = other
    
    def set_cargo(self, other):
        self.__cargo = other

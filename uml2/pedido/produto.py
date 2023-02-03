class Produto:
    def __init__(self, codigo: int, valor: float, descricao: str) -> None:
        self.__codigo = codigo
        self.__valor = valor
        self.__descricao = descricao

    def get_codigo(self):
        return self.__codigo
    def get_valor(self):
        return self.__valor
    def get_descrivao(self):
        return self.__descricao

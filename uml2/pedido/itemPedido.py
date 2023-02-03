from produto import Produto
class ItemPedido:
    def __init__(self, produto: Produto, quantidade:int) -> None:
        self.__quantidade = quantidade
        self.__produto = produto

    def get_quantidade(self):
        return self.__quantidade
    def get_produto(self):
        return self.__produto
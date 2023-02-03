from itemPedido import ItemPedido

class Pedido:

    pedidos = []

    def __init__(self, valor_total: float) -> None:
        self.__valor_total = valor_total

    def adicionarItem(self, item: ItemPedido):
        self.pedidos.append(item)

    def obterTotal(self) -> float:
        self.__valor_total = 0
        for i in self.pedidos:
            qtd  = float(i.get_quantidade())
            valor = float(i.get_produto().get_valor())
            self.__valor_total += qtd * valor
        return self.__valor_total

    def get_valor_total(self):
        return self.__valor_total
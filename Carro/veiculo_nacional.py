from carro import Carro

class VeiculoNacional(Carro):
    def __init__(self, tipo, cor, placa, numero_portas, preco):
        super().__init__(tipo, cor, placa, numero_portas)
        self.__preco = preco

    def __str__(self):
        return 'Valor do {}: {}'.format(super().get_tipo() , self.__preco)
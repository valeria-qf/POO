from carro import Carro

class VeiculoImportado(Carro):
    def __init__(self, tipo, cor, placa, numero_portas, preco):
        super().__init__(tipo, cor, placa, numero_portas)
        self.__preco = preco + (preco * 0.30)

    def __str__(self):
        return 'Valor do {}: {}'.format(super().get_tipo() , self.__preco)
    

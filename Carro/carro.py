class Carro:
    def __init__(self, tipo, cor, placa, numero_portas):
        self.__tipo = tipo
        self.__cor = cor
        self.__placa = placa
        self.__numero_portas = numero_portas

    def __str__(self):
        return '\nVeículo: {} \nCor: {} \nPlaca: {} \nNumero de portas: {}\n'.format(self.__tipo, self.__cor, self.__placa, self.__numero_portas)

    def get_tipo(self):
        return self.__tipo
    def set_tipo (self, tipo):
        self.__tipo = tipo

    def get_cor(self):
        return self.__cor
    def set_cor (self, cor):
        self.__cor = cor

    def get_placa(self):
        return self.__placa
    def set_placa (self, placa):
        self.__placa = placa

    def get_numero_portas(self):
        return self.__numero_portas
    def set_placa (self, numero_portas):
        self.__numero_portas = numero_portas


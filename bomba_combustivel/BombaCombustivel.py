class BombaCombustivel:

    def __init__(self, tipo_combustivel, valor_litro, qtd_combustivel, litros_consumidos):
        self.__tipo_combustivel = tipo_combustivel
        self.__valor_litro = valor_litro
        self.__qtd_combustivel = qtd_combustivel
        self.litros_consumidos = litros_consumidos

    def abastecerPorLitro(self, litros): 
        valor = litros * self.__valor_litro

        if self.__qtd_combustivel < litros:
            print ('Não há combustivel disponível para a operação')
            print(' ')
            self.litros_consumidos = litros
            return self.litros_consumidos

        else:
            print('Tipo: {} \nLitros: {} \nValor: {}'.format(self.__tipo_combustivel, litros, valor))
            self.litros_consumidos = litros
            return self.litros_consumidos

    def abastecerPorValor(self, valor):
        litros = valor/self.__valor_litro

        if self.__qtd_combustivel < litros:
            print('Não há combustivel suficiente!')
            
        else:
            print('\nValor/l do {}: {}'.format(self.__tipo_combustivel, valor))
            self.litros_consumidos = litros
            return self.litros_consumidos

    def litros_consumo(self):
        return self.litros_consumidos
       
    def alterarValor(self,valor):
        self.__valor_litro = valor
        print('\nValor/l do {}: {}'.format(self.__tipo_combustivel, valor))

    def alterarCombustivel(self,tipo):
        self.__tipo_combustivel = tipo
        print ('{} foi alterado para {}'.format(self.__tipo_combustivel, tipo))
        
    def alterarQuantidadeCombustível(self):
        if self.litros_consumidos <= self.__qtd_combustivel:
            self.__qtd_combustivel -= self.litros_consumidos

        print('\nRestam {} litros de {}'.format(self.__qtd_combustivel, self.__tipo_combustivel))

    def get_tipo_combustivel(self):
        print('Tipo:'.format(self.__tipo_combustivel))
        return self.__tipo_combustivel

    def get_valor_litro(self):
        print('Valor'.format(self.__valor_litro))
        return self.__valor_litro

    def get_qtd_combustivel(self):
        return self.__qtd_combustivel


bomba = BombaCombustivel(tipo_combustivel = 'Gasolina Comum', qtd_combustivel = 1000, valor_litro = 5, litros_consumidos = 900)

bomba.abastecerPorLitro(2000) # - NÃO HÁ SUFICIENTE
bomba.abastecerPorLitro(200)
bomba.abastecerPorValor(100)

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if valor < self.saldo:
             self.saldo -= valor
             return True
        else:
            print('Saldo insuficiente')
            return False

    def extrato(self):
        print ('Número: {} \n saldo : {}'.format(self.numero, self.saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True

    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa

    def __str__(self):
        return "Dados da Conta: \nNúmero: {} \nTitular: {} \nSaldo: {}".format(self.numero, self.titular, self.saldo)
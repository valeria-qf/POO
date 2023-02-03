from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

class AtualizadorDeContas:

    def __init__(self, selic, saldo_total=0):
        self.selic = selic
        self.saldo_total = saldo_total

    def roda(self, conta):
        print('Saldo da Conta: {}'.format(conta.saldo))

        self.saldo_total += Conta.atualiza(self.selic)

        print('Saldo Final: {}'.format(self.saldo_total))


if __name__ == '__main__':
            
        c = Conta('123-4', 'Joao', 1000.0, 1000.0)
        cc = ContaCorrente('123-5', 'Jose', 1000.0, 1000.0)
        cp = ContaPoupanca('123-6', 'Maria', 1000.0, 1000.0)

        adc = AtualizadorDeContas(0.01)

        adc.roda(c)
        adc.roda(cc)
        adc.roda(cp)

        print(f'Saldo total: {adc.saldo_total}')
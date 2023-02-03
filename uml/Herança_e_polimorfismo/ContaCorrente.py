from Conta import Conta

class ContaCorrente(Conta):
    def atualiza(self, taxa):
       return super().atualiza(taxa * 2)


    def deposita(self, valor):
        self.saldo += valor - 0.10

    
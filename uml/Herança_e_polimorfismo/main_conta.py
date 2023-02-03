from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from AtualizadorContas import AtualizadorDeContas

conta_1 = Conta(5555, 'A', 500, 100000)

conta_corrente = ContaCorrente(58910, 'Valéria', 500, 10000)

conta_poupanca = ContaPoupanca(55894, 'Vitória', 500, 1000)

print(conta_1)

'''conta_1.atualiza(0.01)
conta_corrente.atualiza(0.01)
conta_poupanca.atualiza(0.01)

print(conta_1.saldo)
print(conta_corrente.saldo)
print(conta_poupanca.saldo)'''

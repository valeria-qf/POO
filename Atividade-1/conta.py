class Conta:
    def __init__(self, numero, titular, saldo, codigo_tipo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.codigo_tipo = codigo_tipo
        if codigo_tipo == 1 :
            self.nome_tipo = 'Conta Corrente'
        else:
            self.nome_tipo = 'Poupança'

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
            return

conta_1 = Conta((int(input('Digite o número da conta:'))), input('Digite o nome do titular:'), float(input('Digite o saldo da sua conta:')), int(input('Conta corrente (1) /  Poupança (2):')), limite = 2500)

while(True):

    operacao = int(input('int(input("Qual operação deseja realizar? \n 1 - Depositar \n 2 - Sacar \n 3 - transferir \n"))'))
    if operacao == 1 :
        conta_1.deposita(int(input('Valor do depósito:  \n')))
        break

    elif operacao == 2 :
           conta_1.saca(int(input('Valor do saque: \n')))
           break

    elif operacao == 3 :
        conta_2 =Conta((int(input('Digite o número da conta:'))), input('Digite o nome do titular:'), float(input('Digite o saldo da sua conta:')), int(input('Conta corrente (1) /  Poupança (2):')), limite = 2500)
        conta_1.transfere_para(conta_2, float(input('Valor de transferência: \n')))
        break

print('Saldo da conta {} é: {} '.format(conta_1.numero, conta_1.saldo))
print('Saldo da conta {} é: {} '.format(conta_2.numero, conta_2.saldo))


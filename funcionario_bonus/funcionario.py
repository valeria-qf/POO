class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10     

class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000

class Motorista(Funcionario):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self._senha = senha

    def get_bonificacao(self):
        return super().get_bonificacao() * 3

f1 = Funcionario('Ana', 123545, 2000)
m1 = Motorista('Francisco', 213654, 1000, 321)

print(f1.get_bonificacao())
print(m1.get_bonificacao())
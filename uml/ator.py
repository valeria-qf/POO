from pessoa import Pessoa

class Ator(Pessoa):
    class Contrato:
        def __init__(self, inicio, fim, salario):
            self.__inicio = inicio
            self.__fim = fim
            self.__salario = salario

        def get_inicio(self):
            return self.__inicio
        def set_inicio(self, inicio):
            self.__inicio = inicio

        def get_fim(self):
            return self.__fim
        def set_fim(self, fim):
            self.__fim = fim

        def get_salario(self, salario):
            return self.__salario
        def set_salario(self, salario):
            self.__salario = salario

        def __str__(self):
            return 'Inicio do contrato: {} \nFim do contrato: {} \nSalário: {}'.format(self.__inicio, self.__fim, self.__salario)

    def __init__(self, nome, sexo, data_nasc, inicio, fim, salario):
            super().__init__(nome, sexo, data_nasc)
            self.__contrato = self.Contrato(inicio, fim, salario)

    def get_contrato(self):
            return self.__contrato
    def set_contrato(self, contrato):
            self.__contrato = contrato

    def __str__(self):
            return 'Nome: {} \nSexo: {} \nData de nascimento: {} \n{}'.format(self.get_name(), self.get_sexo(), self.get_data_nasc(), self.get_contrato())
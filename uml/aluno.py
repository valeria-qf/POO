from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, sexo, data_nasc, matric):
        super().__init__(nome, sexo, data_nasc)
        self.__matric = matric

    def get_matric(self):
        return self.__matric
    def set_matric(self, matric):
        self.__matric = matric

    def __str__(self):
        return 'Nome: {} \nSexo: {} \nData de nascimento: {} \nMatricula: {}'.format(self.get_name(), self.get_sexo(), self.get_data_nasc(), self.__matric)
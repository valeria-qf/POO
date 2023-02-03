from ator import Ator

class Personagem(Ator):
    def __init__(self, nome, sexo, data_nasc, inicio, fim, salario, novela, caracterizacao):
          super().__init__(nome, sexo, data_nasc, inicio, fim, salario)
          self.__caracterizacao = caracterizacao
          self.__novela = novela
    
    def get_caracterizacao(self):
        return self.__caracterizacao
    def set_caracterizacao(self, carac):
        self.__caracterizacao = carac

    def __str__(self):
        return 'Nome: {} \nSexo: {} \nData de nascimento: {} \n{} \nCaracterização: {} \nNovela: {}'.format(self.get_name(), self.get_sexo(), self.get_data_nasc(), self.get_contrato(), self.__caracterizacao, self.__novela)
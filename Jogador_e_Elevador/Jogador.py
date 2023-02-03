#Crie uma classe para representar um jogador de futebol, com os atributos nome, posição, data de nascimento, nacionalidade, altura e peso. Crie os métodos públicos necessários para sets e gets e também um método para imprimir todos os dados do jogador. Crie um método para calcular a idade do jogador e outro método para mostrar quanto tempo falta para o jogador se aposentar. Para isso, considere que os jogadores da posição de defesa se aposentam em média aos 40 anos, os jogadores de meio-campo aos 38 e os atacantes aos 35.

import datetime

class Jogador:

    def __init__(self, nome, posiçao, datanascimento, nacionalidade, altura, peso):

        self.__nome = nome 
        self.__posiçao = posiçao
        self.__datanascimento = datanascimento
        self.__nacionalidade = nacionalidade
        self.__altura = altura
        self.__peso = peso
        self.__idade = (datetime.date.today().year) - \
    (int(self.__datanascimento.split('/')[2]))

    def Aposentar(self):
        if self.__posiçao == 'Atacante':
            if self.__idade == 35:
                print('\nO jogador está na idade para se aposentar')

            elif self.__idade > 35:
                print('\nO jogador já está aposentado ')

            else:
                print('faltam {} anos para se aposentar'.format(35 - self.__idade))

        elif self.__posiçao == 'Meio-Campo':

            if self.__idade == 38:
                print('\nO jogador está na idade para se aposentar')

            elif self.__idade > 38:
                print('\nO jogador já está aposentado ')

            else:
                print('faltam {} anos para se aposentar'.format(38 - self.__idade))
                
        elif self.__posiçao == 'Defesa':

            if self.__idade == 40:
                print('\nO jogador está na idade para se aposentar')

            elif self.__idade > 40:
                print('\nO jogador já está aposentado ')

            else:
                print('faltam {} anos para se aposentar'.format(40 - self.__idade))

    def Imprime(self):
        print(
            
            '\nNome: {} \nPosição: {} \nNascimento: {} \nNacionalidade: {} \nAltura: {} \nPeso: {} \nIdade: {}  \n'
            .format(self.__nome, self.__posiçao, self.__datanascimento, self.__nacionalidade, self.__altura, self.__peso, self.__idade))


    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_posiçao(self):
        return self.__posiçao

    def get_posiçao(self, posiçao):
        self.__posiçao = posiçao
    
    def get_datanascimento(self):
        return self.__datanascimento
    
    def set_datanascimento(self, datanascimento):
        self.__datanascimento = datanascimento
    
    def get_nacionalidade(self):
        return self.__nacionalidade
    
    def set_nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    def get_altura(self):
        return self.__altura
    
    def set_altura(self, altura):
        self.__nacionalidade = altura
    
    def get_peso(self):
        return self.__peso
    
    def set_peso(self, peso):
        self.__peso = peso

jogador = Jogador('Joao', 'Defesa' , '10/12/1990' , 'Brasileiro', 1.80, 90)
jogador.Imprime()
jogador.Aposentar()
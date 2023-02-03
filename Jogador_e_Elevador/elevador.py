# Crie uma classe Elevador para armazenar as informações de um elevador de prédio. A classe deve armazenar o andar atual (térreo = 0), total de andares no prédio (desconsiderando o térreo), capacidade do elevador e quantas pessoas estão presentes nele. A classe deve também disponibilizar os seguintes métodos:
# Inicializar: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores sempre começam no térreo e vazio);
# Entrar: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
# Sair: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
# Subir: para subir um andar (não deve subir se já estiver no último andar);
# Descer: para descer um andar (não deve descer se já estiver no térreo);
# Obs.: Encapsular todos os atributos da classe (criar os métodos set e get).

class Elevador:

    def __init__(self, total_andares, capacidade):
        self.__total_andares = total_andares
        self.__andar_atual = 0
        self.__capacidade = capacidade
        self.__pessoas = 0
        
    def Inicializar(self, total_andares, capacidade):
        self.__total_andares = total_andares
        self.__capacidade = capacidade

    def Entrar(self):
        if self.__pessoas < self.__capacidade:
            self.__pessoas += 1
            print('\nQuantidade de pessoas: {} '.format(self.__pessoas))
        else:
            print('Capacidade máxima atingida : {} pessoas'.format(self.__capacidade))
    
    def Sair(self):
        if self.__pessoas > 0:
            self.__pessoas -= 1
            print('\nQuantidade de pessoas {}'.format(self.__pessoas))
        else:
            print('Não há pessoas no elevador')
    
    def Subir(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
            print('Destino: {} andar'.format(self.__andar_atual + 1))
        else:
            print('Você está no último andar')

    def Descer(self):
        if self.__andar_atual > 0 and self.__andar_atual <= self.__total_andares:
            self.__andar_atual -= 1
        else:
            print('Você está no térreo')

    def get_total_andares(self):
        return self.__total_andares

    def set_total_andares(self, total_andares):
        self.__total_andares = total_andares

    def get_andar_atual(self):
        return self.__andar_atual

    def set_andar_atual(self, andar_atual):
        self.__andar_atual = andar_atual

    def get_capacidade(self):
        return self.__capacidade

    def set_capacidade(self, capacidade):
        self.__capacidade = capacidade

    def get_pessoas(self, pessoas):
        self.__pessoas

elevador = Elevador(int(input('Quantidade de andares: ')), int(input('Capacidade máxima do elevador: ')))

while(True):
    açao = int(input('\nQual ação voce deseja realizar? \n 1 - Subir: \n 2 - Descer: \n 3 - Entrar: \n 4 - Sair: \n\n '))
    if açao == 1:
        elevador.Subir()
        break
    if açao == 2:
        elevador.Descer()
        break
    if açao == 3:
        elevador.Entrar()
        break
    if açao == 4:
        elevador.Sair()
        break
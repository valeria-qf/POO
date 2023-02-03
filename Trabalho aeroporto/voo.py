from datetime import date
from tripulacao import Tripulante
from aeroporto import Aeroporto

class Voo:

    def __init__(self, tipo: str, codigo: int, horario: str, partida: Aeroporto, destino: Aeroporto, assentos_livres: int) -> None:
        self.__tipo = tipo
        self.__codigo = codigo
        self.__horario = horario
        self.__data = date.today()
        self.__partida = partida
        self.__destino = destino
        self.__assentos_livres = assentos_livres
        self.__tripulacao = []
        self.__reservas_voo = []

    def __str__(self) -> str:
        return '\nPartida: {} \n\nDestino:{} \n\nData: {} \nHorário: {} \nTipo: {} \nCódigo: {}  \nAssentos livres: {} \n'.format(self.__partida, self.__destino,self.__data, self.__horario, self.__tipo, self.__codigo, self.get_assentosLivres())

    def cadastrar_tripulacao(self, tripulante: Tripulante):
        self.__tripulacao.append(tripulante)

    def ver_tripulacao(self):
        print('\nTripulação do voo:\n')
        for tripulante in self.__tripulacao:
            print('Nome: {} | Cargo: {}'.format(tripulante.get_nome(), tripulante.get_cargo()))

    '''Getters'''
    def get_tipo(self) -> str:
        return self.__tipo

    def get_codigo(self) -> int:
        return self.__codigo

    def get_horario(self) -> str:
        return self.__horario

    def get_data(self):
        return self.__data
    
    def get_partida(self) -> str:
        return self.__partida
    
    def get_destino(self) -> str:
        return self.__destino

    def get_assentosLivres(self):
        return self.__assentos_livres

    def get_tripulacao(self):
        return self.__tripulacao

    def get_reservas_voo(self):
        return self.__reservas_voo

    '''Setters'''
    def set_tipo(self, other: str) -> None:
        self.__tipo = other
        
    def set_codigo(self, other: int) -> None:
        self.__codigo = other

    def set_horario(self, other) -> None:
        self.__horario = other

    def set_data(self, other) -> None:
        self.__data = other

    def set_partida(self, other: Aeroporto) -> None:
        self.__partida = other

    def set_destino(self, other: Aeroporto) -> None:
        self.__destino = other

    def set_assentosLivres(self, other) -> None:
        self.__assentos_livres = other

    def set_tripulacao(self, other: Tripulante) -> None:
        self.__tripulacao.append(other)
        
    def set_reservas_voo(self, other) -> None:
        self.__reservas_voo.append(other)
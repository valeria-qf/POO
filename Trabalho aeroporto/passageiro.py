
from iagendamento import IAgendamento
from reserva import Reserva

class Passageiro(IAgendamento):
    '''Método construtor'''
    def __init__(self, nome: str, cpf: str, email: str, contato: str) -> None:
        self.__nome = nome 
        self.__cpf = cpf
        self.__email = email
        self.__contato = contato
        self.__reserva = None
        
    '''Getters'''
    def get_nome(self) -> str:
        return self.__nome
    
    def get_cpf(self) -> str:
        return self.__cpf

    def get_email(self) -> str:
        return self.__email

    def get_contato(self) -> str:
        return self.__contato

    def get_reservas(self) -> str:
        return self.__reservas
    
    '''Setters'''
    def set_nome(self, other: str) -> None:
        self.__nome = other

    def set_cpf(self, other: str) -> None:
        self.__cpf = other

    def set_email(self, other: str) -> None:
        self.__email = other

    def set_contato(self, other: str) -> None:
        self.__contato = other

    def set_reservas(self, other: str) -> None:
        self.__reservas = other

    def __str__(self) -> str:
        return '\nNOME COMPLETO: {} \nCPF: {} \nEMAIL: {} \nTELEFONE PARA CONTATO: {}'.format(self.get_nome(), self.get_cpf(), self.get_email(), self.get_contato())

    def pagar_reserva(self):
            self.__reserva.set_status('\nPagamento efetuado!\n')
            print(self.__reserva.get_status())

    def criar_reserva(self, codigo, passageiro, voo):
        self.__reserva = Reserva(codigo, passageiro, voo)
        print('\nReserva confirmada!\n')

    def cancelar_reserva(self):
        self.__reserva.set_status('\nReserva cancelada!\n')
        print(self.__reserva.get_status())
    

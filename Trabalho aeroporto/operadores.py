from iagendamento import IAgendamento
from reserva import Reserva
from passageiro import Passageiro

class Operadores(IAgendamento):

    def criar_reserva(self, codigo, passageiro: Passageiro, voo):
        passageiro.__reserva = Reserva(codigo, passageiro, voo)
        print('\nReserva confirmada!\n')
        
    def cancelar_reserva(self, passageiro: Passageiro):
        passageiro.__reserva.set_status('\nReserva cancelada!\n')
        print(passageiro.__reserva.get_status())

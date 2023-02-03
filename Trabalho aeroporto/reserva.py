from voo import Voo
class Reserva:
    
    def __init__(self, codigo: int, passageiro, voo: Voo, status: str = 'Pagamento Pendente') -> None:
        self.__codigo = codigo
        self.__passageiro = passageiro
        self.__voo = voo
        self.__status = status

    def get_codigo(self):
        return self.__codigo
    
    def get_passageiro(self):
        return self.__passageiro
    
    def get_voo(self):
        return self.__voo

    def get_status(self):
        return self.__status

    def set_passageiro(self, other) -> None:
        self.__passageiro = other
    
    def get_voo(self, other: Voo):
        self.__voo = other
    
    def set_status(self, other):
        self.__status = other
    
    def __str__(self):
            return 'Reserva Confirmada'
    

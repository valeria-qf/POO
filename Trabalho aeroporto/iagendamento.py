from abc import ABC, abstractmethod

class IAgendamento(ABC):

    @abstractmethod
    def criar_reserva(self):
        pass 
    
    @abstractmethod
    def cancelar_reserva(self):
        pass
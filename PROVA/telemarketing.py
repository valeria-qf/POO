from person import Person
from nuisance import Nuisance

class Telemarketing(Person, Nuisance):
    
    def giveSalesPitch(self):
        return '{} pressiona os outros a comprar as coisas'.format(self.get_name())

    def annoy(self):
        return '{} irrita ao dar um discurso de vendas'.format(self.get_name())
from cidade import Cidade
from aeroporto import Aeroporto
from tripulacao import Tripulante
from voo import Voo
from passageiro import Passageiro
from operadores import Operadores


lista_passageiros = []
lista_aeroportos = []
lista_voos = []

serrinha = Cidade('Serrinha dos Pintos', 'Rio Grande do Norte', 'Brasil')
natal = Cidade('Natal', 'Rio Grande do Norte', 'Brasil')

airport1 = Aeroporto('Air-Interior', 10, serrinha)
airport2 = Aeroporto('Air-Exterior', 10, natal)

joana = Tripulante('joana', 'aeromoça')
manoel = Tripulante('manoel', 'piloto')
carla = Tripulante('Carla', 'copiloto')


voo1 = Voo(tipo = 'Nacional', destino = airport1, partida = airport2, assentos_livres = 10, codigo = 111, horario = '10:30')
voo2 = Voo(tipo = 'Nacional', destino = airport2, partida = airport1, assentos_livres = 400, codigo = 112, horario = '23:30')
print(voo1)

voo1.cadastrar_tripulacao(joana)
voo1.cadastrar_tripulacao(carla)
voo1.cadastrar_tripulacao(manoel)
voo1.ver_tripulacao()

passageiro1 = Passageiro('valeria', '111.222.333-44', 'valeria@gmail.com', '(84) 9 9999-9999')
passageiro2 = Passageiro('Eduardo', '111.222.333-55', 'eduardo@gmail.com', '(84) 9 9999-8888')
passageiro3 = Passageiro('Duda', '111.222.333-66', 'duda@gmail.com', '(84) 9 9999-7777')

lista_passageiros.append(passageiro1)
lista_passageiros.append(passageiro2)

operador = Operadores()

print('-'*30)
operador.criar_reserva(111, passageiro2, voo2)
operador.cancelar_reserva(passageiro2)
print('-'*30)

passageiro1.criar_reserva(111, passageiro1, voo1)
passageiro1.pagar_reserva()
passageiro1.cancelar_reserva()

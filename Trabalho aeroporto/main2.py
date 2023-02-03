from cidade import Cidade
from aeroporto import Aeroporto
from tripulacao import Tripulante
from voo import Voo
from passageiro import Passageiro
from operadores import Operadores

lista_passageiros = []
lista_aeroportos = []
lista_voos = []
operadores = []

operador = Operadores()
operadores.append(operador)

serrinha = Cidade('Serrinha dos Pintos', 'Rio Grande do Norte', 'Brasil')
natal = Cidade('Natal', 'Rio Grande do Norte', 'Brasil')

airport1 = Aeroporto('Air-Interior', 10, serrinha)
lista_aeroportos.append(airport1)
airport2 = Aeroporto('Air-Exterior', 10, natal)
lista_aeroportos.append(airport2)

joana = Tripulante('joana', 'aeromoça')
manoel = Tripulante('manoel', 'piloto')
carla = Tripulante('Carla', 'copiloto')


voo1 = Voo(tipo = 'Nacional', destino = airport1, partida = airport2, assentos_livres = 10, codigo = 111, horario = '10:30')
lista_voos.append(voo1)

voo1.cadastrar_tripulacao(joana)
voo1.cadastrar_tripulacao(manoel)
voo1.cadastrar_tripulacao(carla)

passageiro1 = Passageiro('Demetrios', '111.222.333-44', 'demetrios@gmail.com', '(84) 9 9999-9999')
lista_passageiros.append(passageiro1)

def print_sitema_reserva():
    print('-'*30,'VOCE ENTROU NO SISTEMA DE RESERVAS DE VOO','-'*30)

def digite():
    print('-'*30, "DIGITE A OPERAÇÃO DESEJADA " , '-'*30)

def executar_aeroporto():
    digite()
    print("\n1.Criar Aeroporto \n2.Ver todos aeroportos \n3.Sair")
    opcao = int(input())

    if opcao == 1:
        cidade = Cidade(nome=input('Nome da cidade: '), estado=input('Estado da cidade: '), pais=input('País da cidade: '))
        nome = input('Nome do Aeroporto: ')
        capacidade = input('Capacidade de decolagens: ')
        aeroporto = Aeroporto(nome, capacidade, cidade)
        lista_aeroportos.append(aeroporto)
    
    if opcao == 2:
        print('\nAEROPORTOS')
        for i in range(len(lista_aeroportos)):
            print(lista_aeroportos[i])

def executar_voo():
    digite()
    print("\n1.Criar Voo \n2.Ver todos os voos \n3.Ver tripulação \n4.Sair")
    opcao = int(input())

    if opcao == 1:
        voo = Voo(tipo=input('Informe o tipo do voo: '), codigo=input('Digite o código do voo: '), horario=input('Horário: '), partida=airport1, destino=airport2, assentos_livres=input('Assentos: '))
        lista_voos.append(voo)

    if opcao == 2:
        print('\nVOOS')
        for i in range(len(lista_voos)):
            print(lista_voos[i])

    if opcao == 3:
        voo1.ver_tripulacao()

def executar_passageiro():
    digite()
    print("\n1.Cadastrar Passageiro \n2.Criar reserva de voo \n3.Pagar reserva \n4.Cancelar reserva \n5.Ver listas de passageiros \n6.Sair")
    opcao = int(input())

    if opcao == 1:
        passageiro = Passageiro(nome=input('DIgite o nome completo: '), cpf=input('Informe o CPF: '), email=input('Email: '), contato=input('Telefone: '))
        lista_passageiros.append(passageiro)

    if opcao == 2:
        print_sitema_reserva()
        passageiro1.criar_reserva(codigo=voo1.get_codigo(), passageiro=passageiro1, voo=voo1)
        '''
        reserva = Reserva(codigo=voo1.get_codigo(), passageiro=passageiro1, voo=voo1)
        print('Reserva Confirmada!')
        return reserva"
        '''
        
    if opcao == 3:
        print_sitema_reserva()
        passageiro1.pagar_reserva()

    if opcao == 4:
        print_sitema_reserva()
        passageiro1.cancelar_reserva()

    if opcao == 5:
        print('\nPASSAGEIROS\n')
        for i in range(len(lista_passageiros)):
            print('PASSAGEIRO {}.{}\n\n'.format(i, lista_passageiros[i]))

def executar_operador():
    digite()
    print('\n1.Criar reserva \n2.Cancelar reserva \n3.Sair')

    opcao = int(input())

    if opcao == 1:
        print_sitema_reserva()
        operador.criar_reserva(codigo=voo1.get_codigo(), passageiro=passageiro1, voo=voo1)
        
    if opcao == 2:
        print_sitema_reserva()
        operador.cancelar_reserva(passageiro=passageiro1)
        
while True:
    digite()
    print("\n1.Aeroporto\n2.Voo\n3.Passageiro\n4.Operador\n5.Sair")
    option = int(input())
    if option == 1:
        executar_aeroporto()
    if option == 2:
        executar_voo()
    if option == 3:
        executar_passageiro()
    if option == 4:
        executar_operador()
    if option >= 5 or option < 1:
        break

from carro import Carro
from veiculo_importado import VeiculoImportado
from veiculo_nacional import VeiculoNacional
'''
porsche = Carro(tipo = 'Porsche', cor = 'Cinza', placa = 'MHZ-4345', numero_portas = '2')
ferrari = Carro(tipo = 'Ferrari', cor = 'Vermelho', placa = 'JKL-0001', numero_portas = '4')

porsche2 = VeiculoNacional(tipo = 'Porsche', cor = 'Cinza', placa = 'MHZ-4345', numero_portas = '2', preco = 100000)

ferrari2 = VeiculoImportado(tipo = 'Ferrari', cor = 'Vermelho', placa = 'JKL-0001', numero_portas = '4', preco = 100000)
print(porsche2)
print(ferrari2)'''

listaVeiculos = []

while(True):
    
    acao = int(input('Digite 1 para cadastrar um carro \nDigite 2 para cancelar a operação:\n'))
    if acao == 1:
        a = Carro(tipo = str(input('\nDigite o tipo do veículo: ')), cor = str(input('\nDigite a cor: ')), placa = str(input('\nDigite o número da placa: ')), numero_portas = str(input('\nDigite o número de portas: ')))
        listaVeiculos.append(a)

    else:
        print('Finish!')
        break

for i in (listaVeiculos):
    print(i)
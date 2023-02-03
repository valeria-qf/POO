from data import Data

'''chamada da funçao Data na variável data1 sem inserir nenhum dado'''
data1= Data()
'''print da data'''
print((data1))
'''Teste da função que indica se o ano é ou não bissexto'''
data1.bissexto()
'''Chamada da função Avança_data que irá avançar 1 dia na data'''
data1.Avanca_data()
print(data1)

data2 = Data(10, 11, 1)
print(data2)

data3 = data1 + data2
data4 = data1 + 365
print ('Soma de datas: ', data3)
print('Soma com um inteiro: ', data4)
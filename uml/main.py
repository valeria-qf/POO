from pessoa import Pessoa
from date import Date
from aluno import Aluno
from ator import Ator
from personagem import Personagem

datanasc = Date(20, 10, 2000)
pessoa = Pessoa('Ana', 'Feminino', datanasc)
print(pessoa)

print('\n----------------------------\n')

datanasc2 = Date(9, 4, 2004)
pessoa2 = Aluno('Valéria', 'Feminino', datanasc2, 20221094040025)
print(pessoa2)

print('\n----------------------------\n')

datanasc3 = Date(5, 12, 1984)
data_inicio = Date(11, 10, 2019)
data_fim = Date(11, 10, 2022)
ator = Ator('joao', 'masculino', datanasc3, data_inicio, data_fim, 15000)
print(ator)

print('\n----------------------------\n')

datanasc4 = Date(20, 1, 1960)
data_inicio2 = Date(11, 10, 2022)
data_fim2 = Date(11, 10, 2026)
personagem = Personagem('maria', 'feminino', datanasc4, data_inicio2, data_fim2, 10000, 'Maria do bairro', 'Maria do bairro')
print(personagem)
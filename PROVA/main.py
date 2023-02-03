from person import Person
from friend import Friend
from hobby import Hobby

print('\n---------------------------\n')

ana = Person(name ='Ana', age = 20)
print(ana)

bia = Friend(name ='Bia', age = 20, hobby = Hobby.games)
print(bia)
print(bia.chill())

listfriends = []
valeria = Friend('Valeria', 18, 'games')
print(valeria.play(listfriends))

listfriends = ['Henrique']
print(valeria.play(listfriends))

listfriends = ['Ana', 'Marcos']
print(valeria.play(listfriends))

print('\n---------------------------\n')

# ---------------------------

from telemarketing import Telemarketing
peter = Telemarketing(name ='Peter', age = 25)
print(peter)
print(peter.giveSalesPitch())
print(peter.annoy())

print('\n---------------------------\n')

#----------------------------
from butterfly import Butterfly

morpho = Butterfly(species ='Morpho', colors = ['azul'])
print(morpho)
morpho2 = Butterfly( species ='Morpho', colors = [])
print(morpho2)

print('\n---------------------------\n')

#----------------------------
from nuisance import Nuisance
from mosquito import Mosquito

Nuisance.register(Mosquito)
mosquito = Mosquito("Muriçoca")
print(mosquito.annoy())
print(mosquito.buzz())

print('\n---------------------------\n')

#----------------------------

amg1 = Friend('Iara', 19, 'sports')
amg2 = Friend('Iara', 18, 'sports')

if amg1.__eq__(amg2):
    print('Amigos(as) iguais')
else:
    print('Amigos(as) diferentes')
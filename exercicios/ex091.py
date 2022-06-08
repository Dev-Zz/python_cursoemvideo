'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.'''

from distutils.dir_util import remove_tree
from random import randint
from time import sleep
from operator import itemgetter


print('='*50)
jogadores = {'Jogador1' : randint(1,6),
             'Jogador2' : randint(1,6),
             'Jogador3' : randint(1,6),
             'Jogador4' : randint(1,6)}
ranking = {}
for j, m in jogadores.items():
    sleep(0.5)
    print(f'O {j} tirou: {m} no dado.')
print('='*50)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for n, o in enumerate (ranking):
    sleep(0.5)
    print(f'{n+1}º Lugar = {o[0]} com {o[1]}')
print('='*50)
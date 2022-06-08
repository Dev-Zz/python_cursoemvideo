'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.'''

from distutils.dir_util import remove_tree
from random import randint
from time import sleep
from operator import itemgetter

print('='*50)
jogo = {'Jogador (1)': randint(1,6),
        'Jogador (2)': randint(1,6),
        'Jogador (3)': randint(1,6),
        'Jogador (4)': randint(1,6),}
ranking = []
for j, d in jogo.items():
    sleep(0.5)
    print(f'O {j} tirou = {d} no dado.')
print('='*50)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, r in enumerate(ranking):
    sleep(0.5)
    print(f'{i+1}º = {r[0]} com {r[1]}')
print('='*50)
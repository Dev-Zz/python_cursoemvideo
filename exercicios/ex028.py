'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre
0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
pessoa = int(input('Qual o número que você acha que o computador pensou entre 1 e 5? '))
pc = randint(0, 5)
if pessoa == pc:
    print('Nossa!! Você acertou!!')
else:
    print('Que pena você errou.')
print('O número é: {}'.format(pc))

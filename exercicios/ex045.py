'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint


print('\n')
print('-='*20)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

jogador = int(input('''Suas opções:

[0] - Pedra
[1] - Papel
[2] - Tesoura

Qual a sua escolha? '''))

print('-='*20)
print('O Computador escolheu {}'.format(itens[computador]))
print('O Jogador escolheu {}'.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print('Deu EMPATE')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador Vence')
    else:
        print('Jogada Inválida')
elif computador == 1:
    if jogador == 0: 
        print('Computador Vence')
    elif jogador == 1:
        print('Deu EMPATE')
    elif jogador == 2:
        print('Jogador Vence') 
    else:
        print('Jogada Inválida')    
elif computador == 2:
    if jogador == 0:
        print('Jogador Vence')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Deu EMPATE')
    else:
        print('Jogada Inválida')    
print('-='*20)
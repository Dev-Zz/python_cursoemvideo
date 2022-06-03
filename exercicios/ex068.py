'''
Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
'''

from random import randint

jogador_venceu = 0
while True:
    escolha_pc = 0
    print('='*100)
    escolha_jogador = int(input('''Você é:

    [1]PAR
    [2]IMPAR
    
QUAL A OPÇÃO QUE VOCÊ ESCOLHE? '''))
    print('='*100)
    jogador = int(input('Qual seu palpite de 1 - 5(EQUIVALENTE AOS NÚMEROS DE UMA MÃO): '))
    print('='*100)
    pc = randint(0, 5)
    resultado = jogador + pc

    if escolha_jogador == 1:
        escolha_pc = escolha_pc + 2
        if (resultado%2) == 0:
            jogador_venceu = jogador_venceu + 1
            print('Jogador GANHOU!')
        if escolha_pc == 2:
            if (resultado%2) != 0:
                print('Jogador PERDEU!')
                break    
    elif escolha_jogador == 2:
        escolha_pc = escolha_pc + 1
        if (resultado%2) != 0:
            jogador_venceu = jogador_venceu + 1
            print('Jogador GANHOU!')
        if escolha_pc == 1:
            if (resultado%2) == 0:
                print('Jogador PERDEU!')
                break  
print('='*100)  
print('O JOGO ACABOU!') 
print('='*100)
print(f'O jogador venceu {jogador_venceu} vezes')
print('='*100)
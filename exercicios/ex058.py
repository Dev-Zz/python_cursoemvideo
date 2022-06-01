'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.
'''


from random import randint

pessoa = int(input('O computador irá pensar em um número de 0 a 10, qual você acha que ele pensou? '))
pc = randint(0, 10)
palpites = 1

if pessoa == pc:
    print('Você acertou!')
else:
    while pessoa != pc:
        pessoa = int(input('Você errou tente novamente, Qual número você acha que o computador pensou? '))
        palpites = palpites + 1
print('Você acertou! O número que o computador pensou foi {} e você tentou {} vezes!'.format(pc, palpites))
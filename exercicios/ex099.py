'''Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep


def maior(*num):
    cont = maior = 0
    print('-'*30)
    print('Analisando os valores... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    sleep(0.5)
    print(f'\nForam informados {cont} valores ao todo!')
    print(f'O maior valor informado foi {maior}!')

#Programa Principal
maior(5,6,8,9,1,2,3,5,6)
maior(3,2,3,8)
maior(1,2,5)
maior(1)
maior()

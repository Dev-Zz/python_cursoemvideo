'''Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

from time import sleep


def contador(inicio, fim, passo):
    print('-' * 50)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont += passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont -= passo
        print('FIM')
    print('-' * 50)


i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))

contador(0, 10, 1)
contador(10, 0, 1)
contador(i, f, p)
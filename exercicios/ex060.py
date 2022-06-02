'''
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

from math import factorial

num = int(input('Digite o número para calcular seu FATORIAL: '))
fat = factorial(num)

print('O fatorial de {} é igual a {}'.format(num, fat))
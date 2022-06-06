'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, 
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('-'*100)
print (f' Cinco números gerados de forma aleatória: {n}')
print(f' O maior número é: {max(n)}')
print(f' O menor numero é: {min(n)}')
print('-'*100)
'''
Crie um programa que leia um número inteiro e mostre na tela se ele é
PAR ou ÍMPAR.
'''
print('='*85)
n = int(input('Digite um número inteiro: '))
p = n/2
if p == int(p):
    print('O número que você digitou é PAR!')
else:
    print('O número que você digitou é IMPAR!')
print('='*85)

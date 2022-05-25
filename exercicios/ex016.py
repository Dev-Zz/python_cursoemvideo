'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
a sua porção Inteira.

Ex: Digite um número: 6.127
O número 6.127 tem a parte Inteira 6.
'''

numero_float = float(input('Digite um número: '))
numero_int = int(numero_float)
print('O número convertido é o: {}'.format(numero_int))

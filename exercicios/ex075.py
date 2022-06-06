'''
Desenvolva um programa que leia quatro valores pelo teclado e 
guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

n = (
    int(input('Digite um número: ')), #1
    int(input('Digite um número: ')), #2
    int(input('Digite um número: ')), #3
    int(input('Digite um número: '))) #4

print('-'*80)
print(f'Você digitou os valores: {n}')
print(f'Você digitou o valor NOVE {n.count(9)} vezes!')
print(f'O valor TRÊS apareceu na posição: {n. index(3)+1}')
print('Os números PARES são:', end=' ')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')


'''Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.'''

lista = []
lista2 = []
lista3 = []
print('='*50)
for n in range(1,8):
    lista.append(int(input(f'Qual o {n}º valor? ')))
    if n % 2 == 0:
        lista2.append(n)
    elif n % 2 == 1:
        lista3.append(n)
print(f'\nLISTA: {sorted(lista)}.')
print(f'\nValores PARES: {sorted(lista2)}.')
print(f'\nValores IMPARES: {sorted(lista3)}.')
print('='*50)
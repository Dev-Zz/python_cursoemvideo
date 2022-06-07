'''Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.'''


lista = [[], []]
valor = 0
print('='*50)
for n in range(1,8):
    valor = (int(input(f'Qual o {n}º valor? ')))
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 == 1:
        lista[1].append(valor)
print(f'\nValores PARES: {sorted(lista[0])}.')
print(f'Valores IMPARES: {sorted(lista[1])}.')
print('='*50)
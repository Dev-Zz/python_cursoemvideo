'''
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
cont = 0
print('-'*80)
while True:
    lista.append(int(input('Digite um número: ')))
    cont = cont + 1
    continua = str(input('Quer digitar outro VALOR[S/N]? ')).upper()
    if continua == 'N':
        break
print('-'*80)
if 5 in lista:
    print('O valor 5 foi DIGITADO!')
else:
    print('O valor 5 não foi DIGITADO!')
print(f'Foram digitados {cont} números!')
print(f'A lista ordenada de forma decrescente é: {sorted(lista, reverse=True)}')


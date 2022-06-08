'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
cont = 0
val5 = 0
vez = 0
while True:
    print('-'*25)
    núm = int(input('Digite um número: '))
    if núm == 5:
        val5 += 1
    lista.append(núm)
    cont += 1
    resp = str(input('Quer continuar[S/N]: ')).upper()
    if resp == 'N':
        break
print()
print('='*70)
print(f'Foram DIGITADOS {cont} números.')
print(f'A lista de valores de forma crescente é: {sorted(lista)}.')
if val5 > 0 and val5 <= 1:
    vez = 'vez'
else:
    vez = 'vezes'
if val5 > 0:
    print(f'O valor 5 foi digitado: {val5} {vez}.')
print('='*70)

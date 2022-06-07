'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''


dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Qual o seu nome? ')))
    dados.append(float(input('Qual o seu peso? ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continua = str(input('Quer continuar[S/N]? ')).upper()
    if continua == 'N':
        break
print(f'\nForam cadastradas {len(pessoas)} pessoas')
print(f'O Maior peso é: {maior:.2f}KG e o Menor peso é: KG{menor:.2f}KG.')
print('\nFIM DO PROGRAMA')


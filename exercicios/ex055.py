'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

Como resolver?
1- Crie um input do tipo float;
2- Crie um for para pedir o input 5x;
3- Crie uma variavel do tipo lista com os 5 valores;
4- Organize os valores dentro da lista do maior para o menor;
5- Pegue o primeiro e o ultimo valor;
'''

peso = []
for c in range (1, 6):
    pessoas = float(input('Qual o peso da {}º pessoa? '.format(c)))
    peso.append(pessoas)
    peso = sorted(peso)
print('O MAIOR peso é: {} e o MENOR peso é: {}'.format(peso[-1], peso[0]))
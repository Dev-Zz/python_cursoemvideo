'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado
e as suas respectivas posições na lista. 
'''

lista = []
for l in range(0, 5):
    print('-'*40)
    lista.append(int(input('Qual o valor quer colocar na lista: ')))
lista = sorted(lista)
print('-'*40)
print(f'Valores da lista: {lista}')
print(f'Maior valor: {lista[-1]}')
print(f'Menor valor: {lista[0]}')
print('-'*40)

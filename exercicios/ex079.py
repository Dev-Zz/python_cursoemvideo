'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente.
'''

lista = []
for l in range (1, 10):
    if l not in lista:
        lista.append(int(input('Digite um valor: ')))
    else:
        print('Esse número já existe!')
print(lista)
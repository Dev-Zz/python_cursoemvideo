'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente.
'''

lista = []
print('-'*60)
for valor in range (0, 10):
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    else:
        print('O valor já foi digitado, ele não será ADICIONADO a LISTA.')
print('-'*60)
print(f' o valor da lista é: {sorted(lista)}')
print('-'*60)
'''
Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

num = 0
listanum = []
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    listanum.append(num)
    tamanho_lista = len(listanum)
listanum.pop(-1)
soma = 0
for num in listanum:
    soma = soma + num
print('Foram digitados {} números e a SOMA entre eles desconsiderando a FLAG foi {}'.format(tamanho_lista, soma))
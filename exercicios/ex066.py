'''
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''

num = 0
cont = 0
lista_num = []
while num != 999:
    num = int(input('Digite um número inteiro [Caso queira parar digite 999]: '))
    cont += 1
    lista_num.append(num)
lista_num.pop(-1)
soma = 0
for num in lista_num:
    soma = soma + num
print('A SOMA é: {}, foram DIGITADOS: {}'.format(soma, cont-1))

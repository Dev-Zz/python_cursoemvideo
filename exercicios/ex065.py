'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

val = 0
resposta = ''
somaval = 0
cont = 0
lista_val = []

print('-'*50)
while resposta != 'N':
    val = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar [S/N]: ')).upper().strip()
    cont = cont + 1
    somaval = somaval + val
    lista_val.append(val)
media = somaval / cont
lista_val = sorted(lista_val)
maior = lista_val[-1]
menor = lista_val[0]
print('A MÉDIA é: {}, o MAIOR é: {}, o MENOR é: {}'.format(media, maior, menor))


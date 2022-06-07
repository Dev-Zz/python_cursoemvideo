'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

valor_5 = 0
num = []
while True:
    for valor in num:
        num = int(input('Digite um valor: '))
        continua = str(input('Deseja continuar[S/N]? ')).upper()
        if continua == 'N':
            break
print(len(num))
print(sorted(num, reverse=True))
print('Foram digitados o valor cinco {valor_5} vezes.')
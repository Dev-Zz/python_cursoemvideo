'''
Escreva um programa em Python que leia um número inteiro qualquer e 
peça para o usuário escolher qual será a base de conversão: 1 para binário, 
2 para octal e 3 para hexadecimal.
'''

num = int(input('Escreva um número inteiro: '))

escolha = float(input('''Qual será a base de conversão?
(1)-Para Binário
(2)-Para Octal
(3)-Para Hexadecimal

Qual sua escolha: '''))

if escolha == 1:
    binario = bin(num)
    print('O número {} convertido em Binário é: {}'.format(num, binario))
elif escolha == 2:
    octal = oct(num)
    print('O número {} convertido em Octal é: {}'.format(num, octal))
elif escolha == 3:
    hexadecimal = hex(num)
    print('O número {} convertido em Hexadecimal é: {}'.format(num, hexadecimal))



'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

val1 = float(input('Primeiro VALOR: '))
val2 = float(input('Segundo VALOR: '))
menu = 0

while menu != 5:
    menu = int(input('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA

    QUAL A OPÇÃO: '''))
    if menu == 1:
        resultado = val1 + val2
        print('O resultado da SOMA é: {}'.format(resultado))
    if menu == 2:
        resultado = val1 * val2
        print('O resultado da MULTIPLICAÇÃO é: {}'.format(resultado))
    if menu == 3:
        resultado = val1, val2
        maior = max(resultado)
        print('O MAIOR valor é: {}'.format(maior))
    if menu == 4:
        val1 = float(input('Primeiro VALOR: '))
        val2 = float(input('Segundo VALOR: '))
    if menu == 5:
        print('FIM DO PROGRAMA!')      
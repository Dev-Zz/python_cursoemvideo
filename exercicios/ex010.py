'''
Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos Dólares ela pode comprar.
Considere US$1,00 = R$3,27
'''

real = float(input('Quantos reais você tem na carteira? R$'))
dolar = real / 3.27

print('Você pode comprar US${:.2f}'.format(dolar))

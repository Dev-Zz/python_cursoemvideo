'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
'''


r1 = float(input('Valor de R1: '))
r2 = float(input('Valor de R2: '))
r3 = float(input('Valor de R3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Parabens você consegue formar um triangulo!')
else:
    print('Não é possivel formar um triangulo com esses valores!')    
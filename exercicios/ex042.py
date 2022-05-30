'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''


r1 = float(input('Valor de R1: '))
r2 = float(input('Valor de R2: '))
r3 = float(input('Valor de R3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Parabens você consegue formar um triangulo!')
    if r1 == r2 == r3:
        print('Seu triangulo é EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('Seu triangulo é ESCALENO!')
    else:
        print('Seu triangulo é ISÓSCELES')
else:
    print('Não é possivel formar um triangulo com esses valores!')
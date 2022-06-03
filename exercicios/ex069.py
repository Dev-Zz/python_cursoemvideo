'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''

cont = 1
idade_maior = 0
quant_masc = 0
quant_fem_menor_20 = 0
while True:
    print('='*100)
    idade = int(input(f'Qual a IDADE da {cont}º pessoa? '))
    sexo = str(input(f'Qual o SEXO da {cont}º pessoa[F/M]? ')).upper()
    cont = cont + 1
    if idade > 18:
        idade_maior = idade_maior + 1
    if sexo == 'M':
        quant_masc = quant_masc + 1
    if sexo == 'F' and idade < 20:
        quant_fem_menor_20 = quant_fem_menor_20 + 1
    continuar = str(input('Quer continuar[S/N]? ')).upper()
    if continuar == 'N':
        break
    print('='*100)
print('='*100)    
print(f'{idade_maior} PESSOAS TEM MAIS DE 20 ANOS.')
print(f'{quant_masc} PESSOAS DO SEXO MASCULINO FORAM CADASTRADAS.')
print(f'{quant_fem_menor_20} MULHERES TEM MENOS DE 20 ANOS.')
print('='*100)    
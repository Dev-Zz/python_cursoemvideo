'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento.
'''

salario = float(input('Qual o seu salário? R$'))
salario_aumento = salario + (salario * 0.15)
print('Seu novo salário é de R${}'.format(salario_aumento))

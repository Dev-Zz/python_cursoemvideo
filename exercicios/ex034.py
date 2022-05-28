'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Qual o seu salário? R$'))
if salario <= 1.250:
    salario = salario + (salario * 0.15)
    print('O seu salário irá aumentar para: R${:.2f}'.format(salario))
if salario > 1.250:
    salario = salario + (salario * 0.10)
    print('O seu salário irá aumentar para: R${:.2f}'.format(salario))
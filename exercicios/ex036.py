'''
ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. 
O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
CALCULE O VALOR DAS PRESTAÇÕES MENSAIS, SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO
EMPRESTIMO SERÁ NEGADO.
'''

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))* 0.3
anos = int(input('Em quantos anos você irá pagar? '))*12
prestacao = casa / anos

if prestacao > salario:
    print('Infelizmente você não pode comprar essa casa.')
else:
    print('Parabens você consegue comprar essa casa.')


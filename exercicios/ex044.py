'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

print('\n')
print('-='*40)
preco1 = float(input('Qual o preço do produto? '))
print('-='*40)
forma_de_pagamento = int(input('''
(1) - Dinheiro/Cheque
(2) - Cartão à vista
(3) - Cartão de Crédito Parcelado em 2x
(4) - Cartão de Crédito Parcelado em 3x ou mais.

Escolha qual a opção: '''))

if forma_de_pagamento == 1:
    preco1 = preco1 - (preco1*0.10)
    print('-='*40)
    print('O valor ficará: R${:.2f}.'.format(preco1))
elif forma_de_pagamento == 2:
    preco1 = preco1 - (preco1*0.05)
    print('-='*40) 
    print('O valor ficará: R${:.2f}.'.format(preco1))    
elif forma_de_pagamento == 3:
    print('-='*40) 
    print('O valor ficará: R${:.2f}.'.format(preco1))
elif forma_de_pagamento == 4:
    preco1 = preco1 + (preco1*0.2)
    print('-='*40)
    print('O valor ficará: R${:.2f}.'.format(preco1))
print('-='*40)    
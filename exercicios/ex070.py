'''
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. 
No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''

total = total_mais_mil = 0
while True: 
    print('-'*50)
    produto = str(input('Nome do PRODUTO: ')).upper()
    preço = float(input('PREÇO: '))
    total += preço
    if preço > 1000:
        total_mais_mil +=1
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer CONTINUAR[S/N]: ')).strip().upper()
        print('-'*50)
    if resp == 'N':
        break
print('-'*50)    
print('A COMPRA ACABOU')
print(f'O TOTAL da compra foi: {total:.2f}')
print(f'{total_mais_mil} produtos custam mais de R$1000.00 ')

print('-'*50)  


#if preço > 1000:
#    quant_produto_mais_mil = quant_produto_mais_mil + 1



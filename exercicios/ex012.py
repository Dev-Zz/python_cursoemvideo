'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.
'''

preco = float(input('Qual o preço do produto? R$'))
desconto = preco * 0.05
preco_desconto = preco - desconto

print('O preço do produto é de R${}, porém com desconto ficará no valor de R${}'
.format(preco, preco_desconto)
)

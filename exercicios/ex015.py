'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

print('='*100)
km = float(input('Quantos KM você andou? '))
dia = int(input('Quatos dias você ficou com o carro? '))
preco_dia = dia * 60
preco_km = km * 0.15
preco_final = preco_dia + preco_km

print('Você andou {}KM e ficou {} dia(s) com o carro, então você deve pagar: R${}'
.format(km, dia, preco_final)
)
print('='*100)

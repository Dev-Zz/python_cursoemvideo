'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
R$7,00 por cada Km acima do limite.
'''
print('='*85)
velocidade = int(input('Qual a velocidade do carro? '))
excedente = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi multado por excesso de velocidade, a multa vai lhe custar: R${:.2f}'.format(float(excedente)))
print('='*85)

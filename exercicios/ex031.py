'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule
o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
parta viagens mais longas.
'''
print('='*85)
distancia = int(input('Qual a distancia da viagem em KM? '))
if distancia <= 200:
    c1 = distancia * 0.5
    print('O valor da passagem é: R${}'.format(c1))
else:
    c2 = distancia * 0.45
    print('O valor da passagem é: R${}'.format(c2))
print('='*85)

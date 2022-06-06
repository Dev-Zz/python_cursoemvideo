'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus 
respectivos preços, na sequência. No final, mostre uma listagem de preços, 
organizando os dados em forma tabular.
'''

listagem = ('Caderno', 'R$15,00'
            'Lapis', 'R$1,00'
            'Caneta', 'R$3,50')

for pos in range(0, len(listagem)):
    if pos%2 == 0:
        print()
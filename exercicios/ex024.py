'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com
o nome SANTO
'''

cidade = input('Qual o nome da sua cidade? ')
cidadelista = cidade.split()
cidadelista1 = cidadelista[0]
result = 'Santo' in cidadelista1
print('A sua cidade começa com Santo? {}'.format(result))

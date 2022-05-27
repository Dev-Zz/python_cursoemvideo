'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"
no nome.
'''

nome = input('Qual o seu nome completo? ')
result = 'Silva' in nome
print('Você tem Silva no nome? {}'.format(result))

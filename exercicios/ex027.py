'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente.

Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.
'''

nome = str(input('Qual o seu nome completo? ')).split()
print('Seu primeiro nome é: {}, seu ultimo nome é: {}'.format(nome[0], nome[-1]))

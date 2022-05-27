'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

nome = input('Qual seu nome completo? ')
print('Todas as letras MAIUSCULAS do seu nome: {}'.format(nome.upper()))
print('Todas as letras MINUSCULAS do seu nome: {}'.format(nome.lower()))
nomesp = nome.split()
nomespjoin = ''.join(nomesp)
print('A quantidade de letras do seu nome sem considerar espaços é: {}'.format(len(nomespjoin)))
primeironome = len(nomesp[0])
print('A quantidade de letras do seu primeiro nome é: {}'.format(primeironome))

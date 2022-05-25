'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo
na tela o nome do escolhido.
'''
import random

print('='*50)
al1 = input('Primeiro Aluno: ')
al2 = input('Segundo Aluno: ')
al3 = input('Terceiro Aluno: ')
al4 = input('Quarto Aluno: ')
lista = [al1, al2, al3, al4]
r = random.choice(lista)
print('O aluno escolhodo é: {}'.format(r))
print('='*50)

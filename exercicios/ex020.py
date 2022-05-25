'''
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e
mostre a ordem sorteada.
'''
import random

print('='*50)
al1 = input('Primeiro Aluno: ')
al2 = input('Segundo Aluno: ')
al3 = input('Terceiro Aluno: ')
al4 = input('Quarto Aluno: ')
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('A ordem de apresentação sera:\n')
print(lista)
print('='*50)

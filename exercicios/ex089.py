'''Crie um programa que leia nome e duas notas de vários alunos e guarde 
tudo em uma lista composta. No final, mostre um boletim contendo a média 
de cada um e permita que o usuário possa mostrar as notas de cada 
aluno individualmente.'''


from time import sleep


ficha = []
print('='*50)
while True:
    nome = str(input('NOME: '))
    not1 = int(input('NOTA 1: '))
    not2 = int(input('NOTA 2: '))
    media = (not1 + not2)/2
    ficha.append([nome, [not1, not2], media])
    continua = str(input('Quer CONTINUAR[S/N]? ')).upper()
    print('='*50)
    if continua == 'N':
        break
print()
print('A MÉDIA DE CADA UM FOI: ')
for i, a in enumerate(ficha):
    sleep(0.5)
    print(f'{a[0]}: {a[2]}')

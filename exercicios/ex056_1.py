'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

idadetotal = 0
mediaidadetotal = 0
homemmaisvelho = 0
nomedomaisvelho = ''
mulhermenor20 = 0

for p in range (1, 5):
    print('-'*50)
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO[M/F]: '))
    idadetotal = idade + idadetotal
    if p == 1 and sexo in 'Mm':
        homemmaisvelho = idade
        nomedomaisvelho = nome
    if sexo in 'Mm' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomedomaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhermenor20 = mulhermenor20 +1
mediaidadetotal = idadetotal / p
print('-'*50)
print('A média da IDADE é: {}'.format(mediaidadetotal))
print('A IDADE do homem mais velho é: {}'.format(nomedomaisvelho))
print('Existem {} mulheres com MENOS de 20 anos'.format(mulhermenor20))
print('-'*50)
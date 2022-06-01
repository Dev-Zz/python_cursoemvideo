'''
Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''


sexo = ''
sexo = str(input('Digite o seu SEXO [M/F]: ')).upper()
while 'M' != sexo and 'F' !=sexo:
    sexo = str(input('Dados INVALIDOS! Digite o seu SEXO [M/F]: ')).upper()
if sexo == 'M':
    print('Entendi, seu SEXO é MASCULINO!')
if sexo == 'F':
    print('Entendi, seu SEXO é FEMININO!')

'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date


ano_atual = date.today().year
ano_nascimento = int(input('Qual o ANO em que você nasceu? '))
idade = ano_atual - ano_nascimento

if idade < 18:
    falta = 18 - idade
    print('Você ainda não tem idade para se alistar. Ainda falta {} anos.'.format(falta))
elif idade == 18:
    print('Chegou a hora de você se alistar!')
elif idade > 18:
    passou = idade - 18
    print('Você já é maior de 18 anos, passou {} anos do seu ano de alistamento.'.format(passou))


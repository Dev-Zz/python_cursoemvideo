'''
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

Como resolver?

1- Criar o input com a frase;
2- Colocar um for solicitanco o input 7x;
3- Importar o modulo date do datetime;
4- Criar a logica para que salve valores nas variaveis de maior de idade e menor de idade;
5- Mostrar na tela quantos maiores e quantos menores;
'''


from datetime import date

maior = 0
menor = 0
data_atual = date.today().year
print('\n')
print('-='*50)
for ano in range (1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(ano)))
    idade = data_atual - ano
    if idade >= 18:
        maior = maior +1
    elif idade < 18:
        menor = menor +1
print('-='*50)
print('O total de {} pessoas é maior de idade e o total de {} pessoas é menor de idade.'.format(maior, menor))


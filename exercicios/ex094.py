'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada 
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

from time import sleep


dados = {}
dados_lista = []
idade = []
dados_f = []
acima_da_média = []

print('='*80)
while True:
    dados.clear()
    dados['nome'] = str(input('NOME: '))
    while True:
        dados['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite M ou F.')
    if dados['sexo'] == 'F':
        dados_f.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    if dados['idade'] > 0:
        idade.append(dados['idade'])
    dados_lista.append(dados.copy())
    if dados['idade'] > media:
        acima_da_média.append(dados['nome'])
    while True:
        resp = str(input('Quer continuar[S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    print('='*80)
    if resp == 'N':
        break
media = sum(idade) / len(idade)
print(f'A média das idades cadastradas é: {media:.2f}')
print('-'*80)
for i, v in enumerate(dados_f):
    sleep(0.5)
    print(f'A {i+1}º mulher cadastrada foi a {v}')
print('-'*80)
for i, v in enumerate(acima_da_média):
    sleep(0.5)
    print(f'Pessoa: {v} está acima da média de idade.')
print('-'*80)


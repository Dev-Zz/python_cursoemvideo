'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dados = {}
dados_lista = []
print('='*80)
while True:
    dados.clear()
    dados['nome'] = str(input('NOME: '))
    while True:
        dados['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite M ou F.')
    dados['idade'] = int(input('Idade: '))
    dados_lista.append(dados.copy())
    while True:
        resp = str(input('Quer continuar[S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('='*80)
for i, v in enumerate (dados_lista):
    print(f'{i+1} = {v}')
print('='*80)    

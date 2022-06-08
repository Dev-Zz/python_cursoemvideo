'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''


from datetime import date, datetime


dados = {}
dados['nome'] = str(input('NOME: '))
nascimento = int(input('Ano de NASCIMENTO: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Número de sua CARTEIRA DE TRABALHO[0 Caso não tenha.]: '))
if dados['ctps'] == 0:
    del(dados['ctps'])
else:
    dados['ano contratação'] = int(input('Ano de CONTRATAÇÃO: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano contratação'] + 35) - datetime.now().year)
for i, v in dados.items():
    print(f'{i} = {v}')
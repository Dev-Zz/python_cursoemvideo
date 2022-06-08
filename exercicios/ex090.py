'''Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''

alunos = {}
alunos['nome'] = str(input('Qual o NOME do aluno? '))
alunos['media'] = float(input('Qual a MÉDIA do aluno? '))
if alunos['media'] >= 7:
    alunos['situação'] = 'APROVADO'
elif alunos['media'] < 7 and alunos['media'] > 3:
    alunos['situação'] = 'RECUPERAÇÃO'
elif alunos ['media'] <= 3:
    alunos['situação'] = 'REPROVADO'
print()
print(f'O ALUNO: {alunos["nome"]} teve MÉDIA: {alunos["media"]} e sua SITUAÇÃO é: {alunos["situação"]}.')

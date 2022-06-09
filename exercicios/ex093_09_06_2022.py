'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, 
incluindo o total de gols feitos durante o campeonato.'''


from time import sleep


dados = {}
dados_gols = []
print('='*80)
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas o {dados["nome"]} jogou? '))
print('='*80)
for g in range (0, partidas):
    dados_partidas = int(input(f'Quantos gols {dados["nome"]} fez na {g+1}º partida? '))
    dados_gols.append(dados_partidas)
dados['gols'] = dados_gols
total_gols = sum(dados_gols)
dados['total'] = total_gols
print('='*80)
for i, v in dados.items():
   sleep(0.5)
   print(f'{i} = {v}')
print('='*80)
for k, v in enumerate (dados['gols']):
    sleep(0.5)
    print(f'Na {k+1}º partida o {dados["nome"]} fez {v} gols!')
print('='*80)

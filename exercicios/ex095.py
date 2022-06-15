'''Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''


from time import sleep

dados = {}
print('='*80)
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o {dados["nome"]} jogou? '))
gols_partida = []
gols_partida1 = []
for v in range(0, partidas):
    gols_partida1 = gols_partida.append(int(input(f'   Quantos gols na {v+1}ª partida: ')))
dados['gols'] = gols_partida
soma_gols = sum(gols_partida)
dados['total'] = soma_gols
print('='*80)
print(dados)
print('='*80)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('='*80)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(dados['gols']):
    sleep(0.5)
    print(f'    => Na {i+1}ª partida, fez {v} gols.')
print('='*80)
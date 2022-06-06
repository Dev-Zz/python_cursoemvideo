'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Bragantino.
'''

times = ('Corinthians', 'Palmeiras', 'Atlético-MG', 'Coritiba', 'América-MG',
'São Paulo', 'Internacional', 'Athletico-PR', 'Santos', 'Botafogo', 'Flamento', 'Fluminense',
'Avaí', 'Bragantino', 'Ceará SC', 'Juventude', 'Goiás', 'Cuiabá', 'Atlético-GO',
'Fortaleza')
print('-'*100)
print(f'Os cinco primeiros sao: {times[0:5]}')
print(f'Os lanternas do campeonato são: {times[16:20]}')
print('O Bragantino está em {}º no campeonato. '.format(times.index('Bragantino')))
print('-'*100)
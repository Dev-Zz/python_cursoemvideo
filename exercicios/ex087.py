'''Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
        valor_coluna_3 = (matriz[0][2] + matriz[1][2] + matriz[2][2])
print('-='*30)
for l in range(0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
print('-='*30)
print(f'\nA soma dos PARES é: {sum(pares)}')
print(f'A soma da TERCEIRA coluna é: {valor_coluna_3}')
print(f'O MAIOR valor da segunda linha é: {max(matriz[1])}')
print('-='*30)

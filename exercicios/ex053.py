'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
'''


frase = str(input('Fale uma frase com no minímo 4 palavras: ')).strip().upper().split()
frase_junta = ''.join(frase)
ao_contrario = str(frase_junta[::-1]).strip().upper().split()

if ao_contrario == [frase_junta]:
    print('ESSA FRASE É UM PALÍNDROMO!')
else:
    print('ESSA FRASE NÃO É UM PALÍNDROMO!')


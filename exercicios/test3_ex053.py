'''
Tentando ler uma string de trás pra frente usando SLICE.
'''


frase = str(input('Fale uma frase com no minímo 4 palavras: ')).strip().upper().split()
frase_junta = ''.join(frase)
ao_contrario = frase_junta[::-1]

print(ao_contrario)
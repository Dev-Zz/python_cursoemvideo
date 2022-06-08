''' Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores 
pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
lista_par = []
lista_impar = []
while True:
    print('-'*50)
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
    if numeros % 2 == 0:
        lista_par.append(numeros)
    elif numeros % 2 == 1:
        lista_impar.append(numeros)
    resp = str(input('Quer digitar outro número[S/N]? ')).upper()
    if resp == 'N':
        break
print('-'*50)
print()
print(f'LISTA TOTAL: {lista}')
print(f'LISTA PAR: {lista_par}')
print(f'LISTA IMPAR: {lista_impar}')
print('-'*50)
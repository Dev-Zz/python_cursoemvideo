''' Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores 
pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''


lista1 = []
lista2 = []
lista3 = []

print('='*70)
while True:
    valor = int(input('Digite um NÚMERO: '))
    lista1.append(valor)
    continua = str(input('Quer digitar outro NÚMERO[S/N]? ')).upper()
    print('-'*70)
    if valor % 2 == 0:
        lista2.append(valor)
    elif valor % 2 == 1:
        lista3.append(valor)
    if continua == 'N':
        break
print(f'A lista com todos os números digitados é: {lista1}')
print(f'Os valores pares são: {lista2}')
print(f'Os valores impares são: {lista3}')
print('='*70)
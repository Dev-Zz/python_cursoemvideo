'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

Como resolver?

- Crie uma logica para pedir 4 Inputs 4x;
'''


somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomedohomemmaior = ''
totmulher20 = 0
for p in range (1, 3):
    print('-'*50)
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'mM':
        maioridadehomem = idade
        nomedohomemmaior = nome
    if sexo in 'mM' and idade > maioridadehomem:
        maioridadehomem = idade
        nomedohomemmaior = nome
    if sexo in 'fF' and idade < 20:
        totmulher20 = totmulher20 + 1   
mediaidade = somaidade / p
print('-'*50)
print('A MÉDIA das idades é {:.2f} anos'.format(mediaidade))
print('O NOME do Homem mais VELHO é: {}'.format(nomedohomemmaior))
print('A quantidade de MULHERES com MENOS de 20 anos é: {}'.format(totmulher20))
print('-'*50)

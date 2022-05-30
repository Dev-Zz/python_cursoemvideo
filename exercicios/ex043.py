'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''


peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / altura**2

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc <= 24.9:
    print('Você está no seu peso ideal.')
elif imc >= 25 and imc <= 29.9:
    print('Você está no sobrepeso.')
elif imc >= 30 and imc <= 39.9:
    print('Você está obeso.')
elif imc > 40:
    print('Você esta em Obesidade Mórbida.')
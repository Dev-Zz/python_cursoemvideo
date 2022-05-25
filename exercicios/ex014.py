'''
Escreva um programa que converta uma temperatura digitando em
graus Celsius e converta para graus Fahrenheit.
'''

print('='*100)
c = float(input('Qual a temperatura atual em °C? ' ))
f = (c*9/5)+32
print('='*100)
print('A temperatura atual é de {}°C e corresponde a {}°F'.format(c, f))
print('='*100)

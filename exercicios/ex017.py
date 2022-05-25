'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

print('*'*50)
val1 = (float(input('Qual o cateto oposto? ')))**2
val2 = (float(input('Qual o cateto adjacente? ')))**2
hipotenusa = (val1+val2) ** (1/2)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))
print('*'*50)

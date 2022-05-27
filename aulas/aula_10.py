n1 = float(input('Qual a nota do primeiro bimestre? '))
n2 = float(input('Qual a nota do segundo bimestre? '))
m = (n1+n2)/2
print('A sua média é de: {:.1f}'.format(m))
if m >= 6.0:
    print('Parabens você passou de ano!!')
else:
    print('Que pena você está de recuperação!')

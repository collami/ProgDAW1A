# -*- coding: cp1252 -*-
a=input('Introduce un n�mero:')
b=0
for i in range(2,a):
    c=a%i
    if c==0:
        b=b+1
if b==0:
    print 'El n�mero',a,'es primo'
else:
    print 'El n�mero',a,'no es primo'

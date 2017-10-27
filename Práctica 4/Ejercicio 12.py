# -*- coding: cp1252 -*-
a=input('Introduce un número:')
b=0
for i in range(2,a):
    c=a%i
    if c==0:
        b=b+1
if b==0:
    print 'El número',a,'es primo'
else:
    print 'El número',a,'no es primo'

# -*- coding: cp1252 -*-
print 'Dibujando un tri�ngulo equil�tero dando su altura'
a=input('Introduce la altura del tr�ngulo:')
a=abs(a)
for i in range(a):
    b=(i*2)+1
    print' '*a,'*'*b
    a=a-1



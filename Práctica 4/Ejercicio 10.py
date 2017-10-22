# -*- coding: cp1252 -*-
print 'Dibujando un triángulo equilátero dando su altura'
a=input('Introduce la altura del trángulo:')
a=abs(a)
for i in range(a):
    b=(i*2)+1
    print' '*a,'*'*b
    a=a-1



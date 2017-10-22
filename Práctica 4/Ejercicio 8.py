# -*- coding: cp1252 -*-
print 'Dibujando un triángulo dando su altura'
a=input('Introduce la altura del trángulo:')
a=abs(a)
for i in range(a):
    for j in range(i+1):
        print '*',
    print
for i in range(a-1,0,-1):
    for j in range(i):
        print '*',
    print

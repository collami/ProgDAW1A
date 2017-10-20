# -*- coding: cp1252 -*-
print 'Dibujando un rectángulo dando su base y altura'
b=input('Introduce la base del rectángulo:')
b=abs(b)
a=input('Introduce la altura del rectángulo:')
a=abs(a)
for i in range(a):
    for j in range(b):
        print '*',
    print

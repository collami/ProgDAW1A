# -*- coding: cp1252 -*-
print 'Dibujando un rect�ngulo dando su base y altura'
b=input('Introduce la base del rect�ngulo:')
b=abs(b)
a=input('Introduce la altura del rect�ngulo:')
a=abs(a)
for i in range(a):
    for j in range(b):
        print '*',
    print

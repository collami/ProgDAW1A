# -*- coding: cp1252 -*-
print 'Programa utilizando �nicamente bucles FOR'
print 'Dibujando un rect�ngulo dando su base y altura'
b=input('Introduce la base del rect�ngulo:')
b=abs(b)
a=input('Introduce la altura del rect�ngulo:')
a=abs(a)
for i in range(1):
    for j in range(b):
        print'*',
    print
for i in range(a-2):
    for j in range(1):
        print'*',
    for k in range(b-2):
        print ' ',
    for m in range(1):
        print'*',
    print
for i in range(1):
    for j in range(b):
        print'*',


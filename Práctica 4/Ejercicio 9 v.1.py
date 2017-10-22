# -*- coding: cp1252 -*-
print 'Programa utilizando únicamente bucles FOR'
print 'Dibujando un rectángulo dando su base y altura'
b=input('Introduce la base del rectángulo:')
b=abs(b)
a=input('Introduce la altura del rectángulo:')
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


# -*- coding: cp1252 -*-
print 'Dibujando un triángulo dando su altura'
a=input('Introduce la altura del trángulo:')
a=abs(a)
b=a*2
for i in range(a-1,0,-1):
    for j in range(i):
        print i,
    for k in range(1,b,+2):
        for l in range(b):
            print b,
    print


# -*- coding: cp1252 -*-
print 'Programa utilizando combinaci�n de bucles FOR y condiciones IF'
print 'Dibujando un rect�ngulo dando su base y altura'
b=input('Introduce la base del rect�ngulo:')
b=abs(b)
a=input('Introduce la altura del rect�ngulo:')
a=abs(a)
for i in range(a):
    for j in range(b):
        if  i==0 or i==a-1:
            print '*',
        else:
            if j==0 or j==b-1:
                print '*',
            else:
                print ' ',
    print

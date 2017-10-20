# -*- coding: cp1252 -*-
print 'Sumatorio de un rango'
n1=int (input('Introduce el primer valor:'))
n2=int (input('Introduce el segundo valor:'))
j=0
for i in range(n1,n2+1):
    j=j+i
print 'El sumatorio de',n1,'hasta',n2,'es:',j,

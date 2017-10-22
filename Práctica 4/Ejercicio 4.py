# -*- coding: cp1252 -*-
print 'Cálculo del factorial de un número dado'
a=int(input('Introduce un número entero positivo:'))
a=abs(a)
j=1
for i in range(a,1,-1):
    j=j*i
print 'El factorial de',a,'es:',j,
   

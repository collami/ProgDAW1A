# -*- coding: cp1252 -*-
print 'C�lculo del factorial de un n�mero dado'
a=int(input('Introduce un n�mero entero positivo:'))
a=abs(a)
j=1
for i in range(a,1,-1):
    j=j*i
print 'El factorial de',a,'es:',j,
   

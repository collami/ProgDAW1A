# -*- coding: cp1252 -*-
print'Calculando divisores de un n�mero'
a=int(raw_input('Dime un n�mero:'))
lista=[]
c=0
for i in range(1,(a+1)):
    b=a%i
    if b==0:
        lista.append(i)
        c=c+1
print a,'tiene',c,'divisores:',lista

# -*- coding: cp1252 -*-
print'Calculando divisores de un número'
a=int(raw_input('Dime un número:'))
lista=[]
c=0
for i in range(1,(a+1)):
    b=a%i
    if b==0:
        lista.append(i)
        c=c+1
print a,'tiene',c,'divisores:',lista

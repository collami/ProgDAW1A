# -*- coding: cp1252 -*-
print 'Guardando n�meros en una lista'
print 'Dando un l�mite, guarda los valores introducidos hasta que su sumatorio supere el l�mite'
print 'Introduce el valor l�mite:',
l=float(raw_input())
print 'Introduce un valor:',
a=float(raw_input())
lista=[]
while a<=l:
    lista.append(a)
    l=l-a
    print 'Introduce otro valor:',
    a=float(raw_input())   
print lista

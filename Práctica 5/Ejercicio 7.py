# -*- coding: cp1252 -*-
print 'Guardando números en una lista'
print 'Dando un límite, guarda los valores introducidos hasta que su sumatorio supere el límite'
print 'Introduce el valor límite:',
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

# -*- coding: cp1252 -*-
print 'Guardando n�meros en una lista'
print 'Dando un l�mite, guarda los valores introducidos hasta que su sumatorio supere el l�mite'
print 'Introduce el valor l�mite:',
f=float(raw_input())
print 'Introduce un valor:',
a=float(raw_input())
lista=[]
while a>f:
    print a,'es demasiado grande.Introduce otro valor:',
    a=float(raw_input())
lista.append(a)
f=f-a
while f>0:
    print 'Introduce un valor:',
    a=float(raw_input())
    while a>f:
        print a,'es demasiado grande.Introduce otro valor:',
        a=float(raw_input())
    lista.append(a)
    f=f-a
print lista

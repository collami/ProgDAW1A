# -*- coding: cp1252 -*-
print 'Guardando números en una lista'
print 'Dando un límite, guarda los valores introducidos hasta que su sumatorio supere el límite'
print 'Introduce el valor límite:',
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

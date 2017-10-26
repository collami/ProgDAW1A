# -*- coding: cp1252 -*-
print 'Guardando números en una lista'
print 'Para salir del programa y visualizar la lista escribe un número mayor al último introducido'
print 'Introduce un número:',
a=float(raw_input())
list=[a]
print 'Introduce un número mayor que',a,':',
b=float(raw_input())
while a<b:
    list.append(b)
    a=b
    print 'Introduce un número mayor que',a,':',
    b=float(raw_input())
print list

# -*- coding: cp1252 -*-
print 'Guardando n�meros en una lista'
print 'Para salir del programa y visualizar la lista escribe un n�mero mayor al �ltimo introducido'
print 'Introduce un n�mero:',
a=float(raw_input())
list=[a]
print 'Introduce un n�mero mayor que',a,':',
b=float(raw_input())
while a<b:
    list.append(b)
    a=b
    print 'Introduce un n�mero mayor que',a,':',
    b=float(raw_input())
print list

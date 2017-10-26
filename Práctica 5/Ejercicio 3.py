# -*- coding: cp1252 -*-
print 'Guardando notas en una lista'
print 'Para salir del programa y visualizar la lista escribe un número menor de 0 o mayor a 10'
list=[]
a=float(input('Introduce una nota:'))
while a>=0 and a<=10:
    list.append (a)
    a=float(input('Introduce una nota:'))
print list

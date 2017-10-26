# -*- coding: cp1252 -*-
print 'Guardando números en una lista'
print 'Para salir del programa y visualizar la lista escribe un número menor a 0 o mayor a 10'
print 'Introduce un número:',
a=float(raw_input())
list=[a]
print 'Introduce un número mayor que',a,':',
b=float(raw_input())
while a>=b:
    print b,'no es mayor que',a,'.Introduce otro número:',
    b=float(raw_input())
list.append(b)
print list

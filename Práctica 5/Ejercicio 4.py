# -*- coding: cp1252 -*-
print 'Guardando n�meros en una lista'
print 'Para salir del programa y visualizar la lista escribe un n�mero menor a 0 o mayor a 10'
print 'Introduce un n�mero:',
a=float(raw_input())
list=[a]
print 'Introduce un n�mero mayor que',a,':',
b=float(raw_input())
while a>=b:
    print b,'no es mayor que',a,'.Introduce otro n�mero:',
    b=float(raw_input())
list.append(b)
print list

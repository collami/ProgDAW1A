# -*- coding: cp1252 -*-
print 'Guardando números en una lista'
print 'Para salir del programa y visualizar la lista escribe un número no comprendido entre el mímino y el máximo introducidos'
print 'Introduce un número:',
min=float(raw_input())
print 'Introduce un número mayor que',min,':',
max=float(raw_input())
while min>=max:
    print max,'No es mayor que',min,'Introduce un número mayor que',min,':',
    max=float(raw_input())
print 'Ecribe un número entre',min,'y',max,':',
a=float(raw_input())
lista=[]
while a>=min and a<=max:
    lista.append(a)
    print 'Ecribe un número entre',min,'y',max,':',
    a=float(raw_input())
print 'Los valores comprendidos entre',min,'y',max,'que has escrito son:',lista

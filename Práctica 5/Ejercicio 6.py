# -*- coding: cp1252 -*-
print 'Guardando n�meros en una lista'
print 'Para salir del programa y visualizar la lista escribe un n�mero no comprendido entre el m�mino y el m�ximo introducidos'
print 'Introduce un n�mero:',
min=float(raw_input())
print 'Introduce un n�mero mayor que',min,':',
max=float(raw_input())
while min>=max:
    print max,'No es mayor que',min,'Introduce un n�mero mayor que',min,':',
    max=float(raw_input())
print 'Ecribe un n�mero entre',min,'y',max,':',
a=float(raw_input())
lista=[]
while a>=min and a<=max:
    lista.append(a)
    print 'Ecribe un n�mero entre',min,'y',max,':',
    a=float(raw_input())
print 'Los valores comprendidos entre',min,'y',max,'que has escrito son:',lista

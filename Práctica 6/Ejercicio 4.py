# -*- coding: cp1252 -*-
a=int(raw_input('Dime cuántas palabras tiene la lista:'))
lista=[]
for i in range(a):
    print'Dime la palabra',i+1,':',
    b=raw_input()
    lista.append(b)
print 'La lista creada es:',lista
c=raw_input('Dime la palabra que quieres eliminar de la lista:')
for i in range(len(lista)-1,-1,-1):
    if lista[i]==c:
        del lista[i]
print 'La lista es ahora',lista

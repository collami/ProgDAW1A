# -*- coding: cp1252 -*-
a=int(raw_input('Dime cuántas palabras tiene la lista:'))
lista=[]
for i in range(a):
    print'Dime la palabra',i+1,':',
    b=raw_input()
    lista.append(b)
print 'La lista creada es:',lista
c=raw_input('Sustituir la palabra:')
d=raw_input('Por la palabra:')
for i in range(len(lista)):
    if lista[i]==c:
        lista[i]=d
print 'La lista es ahora',lista

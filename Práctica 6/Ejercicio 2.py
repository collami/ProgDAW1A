# -*- coding: cp1252 -*-
a=int(raw_input('Dime cuántas palabras tiene la lista:'))
lista=[]
for i in range(a):
    print'Dime la palabra',i+1,':',
    b=raw_input()
    lista.append(b)
print 'La lista creada es:',lista
c=raw_input('Dime la palabra de la lista que quieres que busque:')
d=0
for i in range(len(lista)):
    if lista[i]==c:
        d=d+1
print 'La palabra',c,'aparece',d,'veces en la lista'

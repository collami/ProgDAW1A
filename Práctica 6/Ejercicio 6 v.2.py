# -*- coding: cp1252 -*-
a=int(raw_input('Dime cuántas palabras tiene la lista:'))
lista=[]
for i in range(a):
    print'Dime la palabra',i+1,':',
    b=raw_input()
    lista.append(b)
print 'La lista creada es:',lista
lista.reverse()
print 'La lista inversa es:',lista

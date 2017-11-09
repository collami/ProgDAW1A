# -*- coding: cp1252 -*-
a=int(raw_input('Dime cuántas palabras tiene la lista:'))
lista1=[]
lista2=[]
for i in range(a):
    print'Dime la palabra',i+1,':',
    b=raw_input()
    lista1.append(b)
print 'La lista creada es:',lista1
for i in lista1:
    if not i in lista2:
        lista2.append(i)
print'La lista sin repeticiones es:',lista2

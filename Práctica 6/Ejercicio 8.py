# -*- coding: cp1252 -*-
a=int(raw_input('Dime cu�ntas palabras tiene la lista:'))
lista=[]
for i in range(a):
    print'Dime la palabra',i+1,':',
    b=raw_input()
    lista.append(b)
print 'La lista creada es:',lista
lista.sort(cmp=None, key=None, reverse=False)
print 'La lista ordenada es:',lista

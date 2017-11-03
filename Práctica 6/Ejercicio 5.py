# -*- coding: cp1252 -*-
a=int(raw_input('Dime cuántas palabras tiene la lista:'))
lista1=[]
lista2=[]
for i in range(a):
    print'Dime la palabra',i+1,':',
    b=raw_input()
    lista1.append(b)
print 'La lista creada es:',lista1
c=int(raw_input('Dime cuántas palabras tiene la lista de palabras a eliminar:'))
for i in range(c):
    print'Dime la palabra',i+1,':',
    d=raw_input()
    lista2.append(d)
print 'La lista de palabras a eliminar es:',lista2
for i in range(len(lista1)-1,-1,-1):
    for j in range(len(lista2)):
        if lista1[i]==lista2[j]:
            del lista1[i]
print 'La lista es ahora',lista1

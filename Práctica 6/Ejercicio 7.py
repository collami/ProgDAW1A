# -*- coding: cp1252 -*-
lista1=[]
lista2=[]
lista3=[]
lista4=[]
lista5=[]
lista6=[]
a=int(raw_input('Dime cuántas palabras tiene la primera lista:'))
for i in range(a):
    print'Dime la palabra',i+1,':',
    b=raw_input()
    lista1.append(b)
print 'La primera lista es:',lista1
c=int(raw_input('Dime cuántas palabras tiene la segunda lista:'))
for i in range(c):
    print'Dime la palabra',i+1,':',
    d=raw_input()
    lista2.append(d)
print 'La segunga lista es:',lista2
for i in range(len(lista1)):
    if lista1[i] in lista2:
        lista3.append(lista1[i])
print 'Palabras que aparecen en las dos listas:',lista3
for i in range(len(lista1)):
    if lista1[i] in lista2:
        lista4=lista4
    else:
        lista4.append(lista1[i])
print 'Palabras que sólo aparecen en la primera lista:',lista4
for i in range(len(lista2)):
    if lista2[i] in lista1:
        lista5=lista5
    else:
        lista5.append(lista2[i])
print 'Palabras que sólo aparecen en la segunda lista:',lista5
lista6=(lista3+lista4+lista5)
print 'Todas las palabras:',lista6

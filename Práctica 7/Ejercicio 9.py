# -*- coding: cp1252 -*-
a=raw_input('Introduce una palabra de al menos 3 letras:')
m=len(a)
while m<3:
    a=raw_input('La palabra introducida, no tiene al menos 3 letras.Introduce otra palabra:')
    m=len(a)
b=raw_input('Introduce la segunda palabra de al menos 3 letras:')
n=len(b)
while n<3:
    b=raw_input('La palabra introducida, no tiene al menos 3 letras.Introduce otra palabra:')
    n=len(b)
def riman(x,y):
    c=0
    for i in range (-1,-4,-1):
        if x[i]==y[i]:
            c=c+1
    if c==3:
        print 'Las palabras riman'
    elif c==2:
        print 'Las palabras riman un poco'
    else:
        print 'Las palabras no riman'
riman(a,b)

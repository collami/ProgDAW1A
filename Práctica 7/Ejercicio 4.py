# -*- coding: cp1252 -*-
a=raw_input('Introduce una frase:')
def textsubs(x):
    y=''
    for i in range (len(x)):
        if x[i]==' ':
            y=y+'*'
        else:
            y=y+x[i]
    return y
print textsubs(a)

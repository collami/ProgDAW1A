# -*- coding: cp1252 -*-
a=raw_input('Introduce una frase:')
b=raw_input('Introduce una vocal:')
def sustituirvocal(x,y):
    w=''
    a='aeiou'
    for i in range (len(x)):
        if x[i] in a:
            w=w+y
        else:
            w=w+x[i]
    return w
print 'La frase es ahora:',sustituirvocal(a,b)

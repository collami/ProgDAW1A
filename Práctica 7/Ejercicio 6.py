# -*- coding: cp1252 -*-
a=raw_input('Introduce un nombre:')
b=raw_input('Introduce un carácter:')
def comprobarcar(x,y):
    c=0
    c=x.count(y)
    if c>0:
        return 'El carácter está dentro del nombre'
    else:
        return 'El carácter no está dentro del nombre'
print comprobarcar(a,b)

# -*- coding: cp1252 -*-
a=raw_input('Introduce un nombre:')
b=raw_input('Introduce un car�cter:')
def comprobarcar(x,y):
    c=0
    c=x.count(y)
    if c>0:
        return 'El car�cter est� dentro del nombre'
    else:
        return 'El car�cter no est� dentro del nombre'
print comprobarcar(a,b)

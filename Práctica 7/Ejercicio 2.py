# -*- coding: cp1252 -*-
a=raw_input('Introduce tu nombre:')
b=raw_input('Introduce tu primer apellido:')
c=raw_input('Introduce tu segundo apellido:')
def concatext(x,y,z):
    a=x+' '+y+' '+z
    return a
print concatext(a,b,c)

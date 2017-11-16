# -*- coding: cp1252 -*-
a=raw_input('Introduce una frase:')
def eliminarblanco(x):
    y=''
    for i in range (len(x)):
        if x[i]<>' ':
            y=y+x[i]
    return y
print eliminarblanco(a)

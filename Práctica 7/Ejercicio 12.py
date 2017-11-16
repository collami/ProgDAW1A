# -*- coding: cp1252 -*-
a=raw_input('Introduce un texto. Cada palabra debe estar separada pou un espacio en blanco:')
def contarpal(x):
    c=0
    for i in range(len(x)):
        if x[i]==' ':
            c=c+1
    return 'El número de palabras en el texto es:',c+1
print contarpal(a)

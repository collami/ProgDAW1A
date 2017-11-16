# -*- coding: cp1252 -*-
a=raw_input('Introduce un texto:')
def contarpal(x):
    c=0
    for i in range(len(x)):
        if x[i]==' 'or x[i]=='.' or x[i]==',' or x[i]==';' or x[i]==':':
            if x[i-1]<>' ' and x[i-1]<>'.' and x[i-1]<>',' and x[i-1]<>';' and x[i-1]<>':':
                c=c+1
    return 'El número de palabras en el texto es:',c+1
print contarpal(a)

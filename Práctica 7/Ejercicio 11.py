# -*- coding: cp1252 -*-
a=raw_input('Introduce una palabra o número:')
def capipali(x):
    y=''
    z=''
    for i in range(len(x)):
        if x[i]<>' ':
            y=y+x[i]
    for i in range(len(y)-1,-1,-1):
            z=z+y[i]
    c=0
    for i in range(len(y)/2):
        if y[i]==z[i]:
            c=c+1
    if c==len(y)/2:
        return 'es capicúa o palíndroma'
    else:
        return 'no es capicúa o palíndroma'
print capipali(a)

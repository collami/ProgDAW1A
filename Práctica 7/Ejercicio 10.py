# -*- coding: cp1252 -*-
a=raw_input('Introduce una palabra o número:')
def capipali(x):
    y=''
    for i in range(len(x)-1,-1,-1):
        y=y+x[i]
    c=0
    for i in range(len(x)/2):
        if x[i]==y[i]:
            c=c+1
    if c==len(x)/2:
        return 'es capicúa o palíndroma'
    else:
        return 'no es capicúa o palíndroma'
print capipali(a)

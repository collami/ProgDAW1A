# -*- coding: cp1252 -*-
a=raw_input('Introduce una frase:')
def contarvocal(x):
    c=0
    voc='aeiou'
    for i in range (len(voc)):
        if voc[i] in x:
            c=x.count(voc[i])
        print 'La vocal',voc[i],'aparece',c,'veces.'
        c=0
contarvocal(a)

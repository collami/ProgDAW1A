print 'Introduce una frase'
a=raw_input()
print 'Introduce una vocal'
b=raw_input()
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

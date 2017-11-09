print 'Introduce un nombre'
a=raw_input()
print 'Introduce un caracter'
b=raw_input()
def comprobar(x,y):
    w=0
    w=x.count(y)
    if w>0:
        return 'El caracter esta dentro del nombre'
    else:
        return 'El caracter no esta dentro del nombre'
print comprobar(a,b)

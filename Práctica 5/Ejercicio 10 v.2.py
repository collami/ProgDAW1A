lista1=[]
lista2=[]
c=0
a=raw_input('Introduce un nombre:')
while a!='':
    lista1.append(a)
    c=c+1
    b=float(input('Introduce una nota:'))
    while b>=0 and b<=10:
        lista1.append(b)
        c=c+1
        b=float(input('Introduce una nota:'))
    a=raw_input('Introduce un nombre:')
print 'Los alumnos  y sus notas son:'
for i in range(c):
    print lista1[i]
    c=c-1
                  

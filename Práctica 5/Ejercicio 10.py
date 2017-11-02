lista1=[]
lista2=[]
a=raw_input('Introduce un nombre:')
while a!='':
    lista1.append(a)
    b=float(input('Introduce una nota'))
    while b>=0 and b<=10:
        lista1.append(b)
        b=float(input('Introduce una nota'))
    lista2.append(lista1)
    lista1=[]
    a=raw_input('Introduce un nombre:')   
print lista2
                  

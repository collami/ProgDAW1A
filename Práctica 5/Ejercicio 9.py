lista1=[]
lista2=[]
c=0
a=raw_input('Introduce un nombre:')
while a!='':
    lista1.append(a)
    b=input('Introduce un n�mero de tel�fono')
    lista1.append(b)
    lista2.append(lista1)
    c=c+1
    lista1=[]
    a=raw_input('Introduce un nombre:')
print 'Los nombres y tel�fonos son:'
for i in range(c):
    print lista2[i]
                  

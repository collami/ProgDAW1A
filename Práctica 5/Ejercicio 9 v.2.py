lista1=[]
lista2=[]
c=0
a=raw_input('Introduce un nombre:')
while a!='':
    lista1.append(a)
    c=c+1
    b=input('Introduce un n�mero de tel�fono:')
    lista1.append(b)
    c=c+1
    a=raw_input('Introduce un nombre:')
print 'Los nombres y tel�fonos son:'
for i in range(0,c,+2):
    print lista1[i],':',lista1[i+1]
    c=c-1

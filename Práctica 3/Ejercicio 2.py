print 'N�meros pares e impares de un rango'

n_ini=int (input('Introduce el valor inicial del rango:'))
                 
n_fin=int (input('Introduce el valor final del rango:'))
                 
for i in range(n_ini,n_fin+1):
    if  i%2==0:
        print 'El n�mero,',i,'es par'
    else:
        print 'El n�mero,',i,'es impar'         
                 

# -*- coding: cp1252 -*-
print 'Adivinando un número dentro de un rango'
import random
import time
random.seed(time.time())
minim = int(raw_input("Establece el valor mínimo: "))
maxim = int(raw_input("Establece el valor máximo: "))
secret = random.randint(minim, maxim)
c=0
print'Intenta adivinar un número entre',minim,'y',maxim
a=int(raw_input("Introduce el número que crees que he pensado: "))
c=c+1
while a<>secret:
    if a<secret:
        print'Demasiado pequeño',
    else:
        print'Demasiado grande.',
    a=int(raw_input('Introduce otro número: '))
    c=c+1
print'Correcto!Lo has intentado',c,'veces'

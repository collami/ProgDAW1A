# -*- coding: cp1252 -*-
print 'Adivinando un n�mero dentro de un rango'
import random
import time
random.seed(time.time())
minim = int(raw_input("Establece el valor m�nimo: "))
maxim = int(raw_input("Establece el valor m�ximo: "))
secret = random.randint(minim, maxim)
c=0
print'Intenta adivinar un n�mero entre',minim,'y',maxim
a=int(raw_input("Introduce el n�mero que crees que he pensado: "))
c=c+1
while a<>secret:
    if a<secret:
        print'Demasiado peque�o',
    else:
        print'Demasiado grande.',
    a=int(raw_input('Introduce otro n�mero: '))
    c=c+1
print'Correcto!Lo has intentado',c,'veces'

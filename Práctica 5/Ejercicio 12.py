# -*- coding: cp1252 -*-
print 'Adivinando un n�mero dentro de un rango'
minim = int(raw_input("Establece el valor m�nimo: "))
maxim = int(raw_input("Establece el valor m�ximo: "))
print'Piensa un n�mero entre',minim,'y',maxim,'a ver si lo puedo adivinar'
a=(maxim-minim)/2
print'Es',a,':',
b=raw_input()
while b<>'igual':
    if b=='mayor':
        minim=a
        a=a+((maxim-a)/2)
    elif b=='menor':
        maxim=a
        a=a-((a-minim)/2)
    print'Es',a,':',
    b=raw_input()
print'Gracias por jugar conmigo'

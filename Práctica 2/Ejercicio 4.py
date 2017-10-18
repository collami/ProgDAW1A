print 'Mostrando el tipo de dato seleccionado'

print '1-Pyton'
print '2-(6.0, software, 452.6)'
print '3-458'
print '4-65.21458'

dato1='Pyton'
dato2=(6.0, 'software', 452.6)
dato3=458
dato4=65.21458

S=(input('Introduce el número del dato del que quieres cononcer su tipo:'))

if S==1:
    print 'El tipo de dato seleccionado es del tipo:' ,type(dato1),
elif S==2:
     print 'El tipo de dato seleccionado es del tipo:' ,type(dato2),
elif S==3:
     print 'El tipo de dato seleccionado es del tipo:' ,type(dato3),
elif S==4:
     print 'El tipo de dato seleccionado es del tipo:' ,type(dato4),
else:
     print 'El número seleccionado no está en la lista'



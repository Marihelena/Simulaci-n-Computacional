veces = int (raw_input("Ingresa el numero de veces a generar ")) #Se ingresan los datos respectivos
a = int (raw_input("ingrese la constante multiplicativa "))
semilla= int (raw_input("Ingrese la semilla "))
c = int (raw_input("Ingrese la constante aditiva "))
mod = int (raw_input("Ingrese el modulo "))
 
print 'n   Xo   (aXo + c) modm   Xn + 1    Numero  '
 
for i in range (veces): #desde i hasta el numero que se quiere generar
    i += 1
    xn = ((a*semilla)+c)%mod    #Formula general
    div = xn/mod                #Formula general
    z = float((xn+.0) / (mod+.0))
    print "%d   %d    (%d  +  %d)/%d     %d        %f  "%(i, semilla, div, xn, mod, xn, z)
    semilla = xn                #Xn+1 se convierte en la semilla
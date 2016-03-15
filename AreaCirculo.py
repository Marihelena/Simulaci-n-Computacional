import math
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

val=int(input("Ingrese la cantidad de puntos a generar: "))
def randux(num):
    semilla=13
    arreglox=[]
    for i in range(0,num):
        xn=(17*semilla+73)%127
        div=float(xn)/127
        semilla=xn
        arreglox.append(div)
    return arreglox

def randuy(num):
    semilla=11
    arregloy=[]
    for i in range(0,num):
        xn=(41*semilla+29)%269
        div=float(xn)/269
        semilla=xn
        arregloy.append(div)
    return arregloy

arreglox=randux(val)
arregloy=randuy(val)


N=val
x=0
plt.ion()
axi=plt.gca()

for i in range(val):
    arreglox[i]=(12)*arreglox[i]-6
    
for j in range(val):
    arregloy[j]=(12)*arregloy[j]-6

for i in range(val):
    if(5**2>=((arreglox[i]*arreglox[i])+(arregloy[i]*arregloy[i]))):
        z=1/(N*100)
        z=z+z
        x=x+1
        axi.plot(arreglox[i],arregloy[i],'b.')
    else:
        axi.plot(arreglox[i],arregloy[i],'r.')
    if i%120==0:
        plt.draw()
areaEstimada=x*z
print "Area Teorica del circulo:",math.pi*25,",", areaEstimada,"," ,x
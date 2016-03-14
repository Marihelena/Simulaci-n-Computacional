if __name__ == "__main__":
    xo=str(input("Ingrese el valor de la semilla: "))
    n=int(len(xo)/2)
    if len(xo)%2==0: #Si el modulo 2 del tamaño de la semilla es cero entonces...
        veces=int(input("Ingrese la cantidad de numeros a generar: "))
        for i in range(veces):
            d=len(xo)
            zero=""
            xo=int(xo)
            xo2=xo*xo
            y=str(xo2)
            for j in range((4*n)-len(y)):
                zero+="0"
            y=zero+y
            
            xo=str(xo)
            y2=y[int((2*d)/4):int((2*d*3)/4)] #Se escoge la mitad del numero total
            print 'x =',y2
            out=y2
            xo=out
            i=i+1
    else:
        print("Intente de nuevo con un numero de cifras par")
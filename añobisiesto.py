p1 = input ("¿Desea saber si un año en bisiesto?")

#Si dice que si, que siga, y si dice que no que se termine el programa

if p1.lower() == "si":
    p2 = int(input("Ingrese un año entre 1900 y 2199..."))
    if p2/4 == p2//4:
        print ("Este año es bisiesto") 
    elif p2/4 == p2//4 and p2/100 == p2//100 and p2/400 == p2//400:
        print ("Este año es bisiesto") 
    elif p2/4 == p2//4 and p2/100 == p2//100:
        print ("Este año no es bisiesto")
    else:
        print ("Este año no es bisiesto")
    quit()
else:
    print ("Entonces hoy no puedo ayudarte...")
quit()
        
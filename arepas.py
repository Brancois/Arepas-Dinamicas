name = input ("Introducir nombre...")
print ("Hola " + name + ", yo soy arepabot, una receta dinamica de arepas.")

Q1 = int(input("Cuantas arepas deseea cocinar?"))

#Se multiplica la repuesta de Q1 con la cantidad de ingredientes

harina = (1/3 * Q1)
print ("Necesitaras, " + str(harina) + " tazas de harina")

agua = (1/4 * Q1)
print ("Necesitaras, " + str(agua) + " tazas de agua")

sal = (1/64 * Q1)
print ("Necesitaras, " + str(sal) + " tazas de sal")

aceite = (1/32 * Q1)
print ("Necesitaras, " + str(aceite) + " tazas de aceite")

despedida = ("Espero que disfrute de sus deliciosas arepas :)")
print (despedida)
#Escribir un programa que pida al usuario un número entero
#y muestre por pantalla un triángulo rectángulo que tenga
#tantas líneas como el número introducido, como el triángulo de más abajo.
Numero = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, Numero+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
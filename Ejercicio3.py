#Escribir un programa que pida al usuario
#un número entero y muestre por pantalla
#si es par o impar.
Numero = int(input("Dame un numero sin comas--> "))
if Numero % 2 == 0:
    print("Si, el " + str(Numero) + " es par")
else:
    print("Si, el " + str(Numero) + " es impar")
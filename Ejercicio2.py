#Escribir un programa que pida al usuario dos números
#y muestre por pantalla su división. Si el divisor es
#cero el programa debe mostrar un error.
numero1 = float(input("Introduce el numero de arriba: "))
numero2 = float(input("Introduce el numero de abajo: "))
if numero2 == 0:
    print("Venga pringau que no puedes dividir por 0 y lo sabes")
else:
    print(numero1/numero2)
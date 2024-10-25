#Escribir un programa que almacene la cadena de caracteres
#contraseña en una variable, pregunte al usuario por la
#contraseña e imprima por pantalla si la contraseña introducida
#por el usuario coincide con la guardada en la
#variable sin tener en cuenta mayúsculas y minúsculas.
Contraseña = "Mercedes45"
ctr = input("¿Cual es tu contraseña? ")
if Contraseña == ctr.lower():
    print("Correcto")
else:
    print("Incorrecto")
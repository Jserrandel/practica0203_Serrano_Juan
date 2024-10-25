#Escribir un programa en el que se pregunte al usuario
#por una frase y una letra, y muestre por pantalla el
#número de veces que aparece la letra en la frase.
frase = input("Dime una frazesita: ")
letra = input("Una letra que haya en la frase: ")
contardor = 0
for i in frase:
    if i == letra:
        contardor += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contardor, frase))
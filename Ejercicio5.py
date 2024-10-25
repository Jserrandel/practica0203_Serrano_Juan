#Los alumnos de Hogwarts se han dividido en dos casas,
#Gryffindor y Slytherin, de acuerdo al sexo y el nombre.
#Gryffindor está formado por las mujeres con un nombre
#anterior a la M y los hombres con un nombre posterior
#a la N y Slytheryn por el resto. Escribir un programa
#que pregunte al usuario su nombre y sexo, y muestre
#por pantalla el grupo que le corresponde.
name = input("¿Como te llamas? Si, ya se que deberiamos saberlo, pero al mundo magico no le ha ido muy bien ultimamente: ")
gender = input("¿Cuál es tu genero (M o H)? Estoy un poco ciego vale: ")
if gender == "M":
    if name.lower() < "m":
        group = "Gryfindor"
    else:
        group = "Slytherin"
else:
    if name.lower() > "n":
        group = "Gryfindor"
    else:
        group = "Slytherin"
print("Tu grupo es " + group)
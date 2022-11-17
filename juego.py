def menu():
    print ("Adivina el numero")
    print ("Nivel aficionado")
    print ("Nivel profesional")
    print ("Nivel clase mundial")
    print ("Nivel leyenda")
    dificultad = input ("Elige la dificultad: ")
    print (dificultad)
    if dificultad == "Nivel aficionado":
        juego(0,100)
    elif dificultad == "Nivel profesional":
        juego(0,1000)
    elif dificultad == "Nivel clase mundial":
        juego(0,1000000)
    elif dificultad == "Nivel leyenda":
        juego (0,1000000000000)
    else:
            return menu()
def numerorandom(minimo, maximo):
    import random
    numerorandom = random.randint(minimo, maximo)
    return numerorandom
def juego(minimo, maximo):
    nrandom = numerorandom(minimo, maximo)
    numero = int(input("Escribe un numero entre", minimo, "y", maximo, ": "))

menu ()

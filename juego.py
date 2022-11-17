def menu():
    print ("Adivina el numero")
    print ("Nivel aficionado")
    print ("Nivel profesional")
    print ("Nivel clase mundial")
    print ("Nivel leyenda")
    dificultad = input ("Elige la dificultad: ")
    print (dificultad)
    if dificultad == "Nivel aficionado":
        juego(0,100, nrandom = numerorandom(0,100))
    elif dificultad == "Nivel profesional":
        juego(0,1000,  nrandom = numerorandom(0,1000))
    elif dificultad == "Nivel clase mundial":
        juego(0,1000000,  nrandom = numerorandom(0,1000000))
    elif dificultad == "Nivel leyenda":
        juego (0,1000000000000,  nrandom = numerorandom(0,1000000000000))
    else:
            return menu()
def numerorandom(minimo, maximo):
    import random
    nrandom = random.randint(minimo, maximo)
    return nrandom
def juego(minimo, maximo, nrandom,):
    facilitarnos = 0
    numero = input("Elige un numero entre " + str(minimo) + " y " + str(maximo) + ": ")
    numero = int(numero)
    print(numero)
    while True:
        if numero == nrandom:
            print("Has conseguido alzarte con la victoria")
            facilitarnos+=1
        elif numero > nrandom:
            print("El numero es menor")
            facilitarnos+=1
            if facilitarnos == 4:
                preguntafacilitarnos (minimo, maximo, nrandom)
        elif numero < nrandom:
            print("El numero es mayor")
            facilitarnos+=1
            if facilitarnos == 4:
                preguntafacilitarnos(minimo, maximo, nrandom) 
        else:
            return juego(minimo, maximo, nrandom)
def preguntafacilitarnos(minimo, maximo, nrandom): 
    respuesta = input("Quieres ayuda?")
    print(respuesta)
    if respuesta == "Si":
        print("El numero esta entre", minimo + 1)
    elif respuesta == "No":
        print("No tiene ayuda")
        return juego()
    else:
        return preguntafacilitarnos()


menu()
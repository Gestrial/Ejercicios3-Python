def alturaM():
    a = float(input("Ingresa tu altura en metros: "))
    return a


def alturaCM():
    a = int(input("Ingresa tu altura en centimetros: "))
    return a


def peso1():
    a = float(input("Ingresa tu peso en kg: "))
    return a


def genero1():
    genero2 = input("Ingresa tu genero, M para masculino o F para femenino: ")
    gender = 0
    if genero2.upper() == "M":
        gender = 10.8
    return gender


def genero2():
    genero2 = input("Ingresa tu genero, M para masculino o F para femenino: ")
    gender = -161
    if genero2.upper() == "M":
        gender = 5
    return gender


def edad():
    age = int(input("Ingrese su edad: "))
    return age


def choose():
    while True:
        opcion = int(input("Elija que desea calcular segun su numero: \n1)IMC\n2)GC\n3)TMB\n4)TMB_AF\n5)CA\n"))
        if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
            return opcion
        else:
            print("Ingrese una opcion correcta porfavor.")

def ejercitarse():
    while True:
        a = input("Cuanto ejercicio realiza por semana:\n A) Poco. \nB) Ligero. \nC) Moderado. \nD) Deportista \nE) Atleta \n[A/B/C/D/E]? : ")
        if a.upper() == "A" or a.upper() == "B" or a.upper() == "C" or a.upper() == "D" or a.upper() == "E":
            return a.upper()
        else:
            print("Ingrese una opcion correcta porfavor.")


def selector():
    while True:
        rr = input("Que desea hacer:\nA) Reducir calorías. \nB) Aumentar gasto calórico. \nRespuesta: ")
        if rr.upper() == "A" or rr.upper() == "B":
            return rr.upper()
        else:
            print("Ingrese una opcion correcta porfavor.")
        
            
def pregunta():
    while True:
        a = input("Desea calcular algo mas ? S/N ")
        if a.upper() == "S" or a.upper() == "N":
            return a.upper()
        else:
            print("Ingresa una opcion correcta porfavor.")
            continue

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
    if genero2 == "M":
        gender = 10.8
    return gender

def genero2():
    genero2 = input("Ingresa tu genero, M para masculino o F para femenino: ")
    gender = -161
    if genero2 == "M":
        gender = 10.8
    else:
        gender = 5
    return gender


def edad():
    age = int(input("Ingrese su edad: "))
    return age
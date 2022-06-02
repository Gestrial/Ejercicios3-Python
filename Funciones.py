from Inputs import alturaCM, edad, genero1, genero2, peso1

#FUNCIONES DE CALCULO

def imc(a,b):
    return a / (b * b)

def gc(a,b,c):
    d = 1.2 * a + 0.23 * b - 5.4 - c
    return d

def tmb(a,b,c,d):
    return (10*a) + (6.25*b) - (5*c) + d


def tmba(a,b):
    return a*b

def adelgazando(a,b,c,d):
    f = a * b
    f2 = a * d
    if c == "-":
        g = a - f
        g2 = a - f2
        return print(f"Se recomienda que se consuma entre {g2} y {g} calorias al dia.")
    else:
        return print(f"Se recomiendo que se consuma entre {f} y {f2} calorias al dia.")

def tasaMB2():
    peso = peso1()
    altura = alturaCM()
    edad1 = edad()
    gender = genero2()
    tmb2 = tmb(peso,altura,edad1,gender)
    return tmb2

def tasaMB3():
    peso = peso1()
    altura = alturaCM()
    edad1 = edad()
    gender = genero1()
    tmb2 = tmb(peso,altura,edad1,gender)
    return tmb2

    
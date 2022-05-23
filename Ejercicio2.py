
from Funciones import imc,gc


def porcentajeGC():
        peso = float(input("Ingresa tu peso: "))
        altura = float(input("Ingresa tu altura: "))
        edad = int(input("ingresa tu edad: "))
        generoReal = "A"
        while True:
            genero = input("ingresa M para masculino o F para femenino")
            if "M" == genero or genero == "F":
                generoReal = genero
                break
            else:
                print("Ingresa un genero correcto.")
        gender = 0
        if generoReal == "M":
            gender = 10.8
        imc2 = imc(peso,altura)
        gct = gc(imc2,edad,gender)
        return gct

 
print(f"El porcentaje de grasa corporal es: {porcentajeGC()}")
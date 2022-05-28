from Funciones import imc,gc
from Inputs import alturaM, edad, genero1, peso1


def porcentajeGC():
        peso = peso1()
        altura = alturaM()
        edad2 = edad()
        gender = genero1()
        imc2 = imc(peso,altura)
        gct = gc(imc2,edad2,gender)
        print(f"El porcentaje de grasa corporal es: {gct}")
        return gct

 

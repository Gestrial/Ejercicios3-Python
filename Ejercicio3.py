"""
 Tasa metabólica basal - TMB
La tasa metabólica basal es el mínimo de calorías necesarias para vivir, es decir el número
de calorías que un ser humano quema al día estando en reposo. Estas calorías son
utilizadas por el cuerpo para llevar a cabo funciones básicas como: bombear la sangre,
hacer digestión, respirar, mantener el cerebro funcionando, etc. La TMB se calcula a través
de la siguiente fórmula:
TMB = (10*peso (kg)) + (6.25*altura(cm)) - (5*edad(años)) + valor_genero
Donde valor_genero es un valor que depende del género de la persona: en caso de ser
masculino, el valor es 5, mientas que es -161 en caso de ser femenino.
"""

from Funciones import tmb


def tasaMB():
        peso = float(input("Ingresa tu peso: "))
        altura = int(input("Ingresa tu altura en centimetros: "))
        edad = int(input("ingresa tu edad: "))
        generoReal = ""
        while True:
            genero = input("ingresa M para masculino o F para femenino")
            if "M" == genero or genero == "F":
                generoReal = genero
                break
            else:
                print("Ingresa un genero correcto.")
        gender = -161
        if generoReal == "M":
            gender = 5
        tmb2 = tmb(peso,altura,edad,gender)
        return tmb2
        

print(f"La tasa metabólica basal es de: {tasaMB()} ")
        
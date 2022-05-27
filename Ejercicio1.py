from Funciones import imc
from Inputs import alturaM, peso1

def indiceMC():
        peso = peso1()
        altura = alturaM()
        imc2 = imc(peso,altura)
        peso = " "
        if imc2 < 16:
            return print(f"Su imc es de: {imc2}, Delgadez severa")
        elif 16 > imc2 and imc2 < 16.99:
            return print(f"Su imc es de: {imc2}, Delgadez moderada")
        elif 17 > imc2 and imc2 < 18.49:
            return print(f"Su imc es de: {imc2}, Delgadez aceptable")
        elif 18.5 > imc2 and imc2 < 24.99:
            return print(f"Su imc es de: {imc2}, Peso normal")
        elif 25 > imc2 and imc2 < 29.99:
            return print(f"Su imc es de: {imc2}, Sobrepeso")
        elif 30 > imc2 and imc2 < 34.99:
            return print(f"Su imc es de: {imc2}, Obesidad tipo I")
        elif 35 > imc2 and imc2 < 39.99:
            return print(f"Su imc es de: {imc2}, Obesidad tipo II")
        elif 40 > imc2 and imc2 < 49.99:
            return print(f"Su imc es de: {imc2}, Obesidad tipo III o mórbida")
        else:
            return print(f"Su imc es de: {imc2}, Obesidad tipo IV o extrema")

indiceMC()
    
        

        
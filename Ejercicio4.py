from Funciones import tasaMB2, tmba
from Inputs import ejercitarse

# EJECUTAR DESDE MAIN

def tmb_():
        tmb = tasaMB2()
        ejercicio = ejercitarse()
        actividad = -1
        if ejercicio == "A":
            actividad = 1.2
        elif ejercicio == "B":
            actividad = 1.375
        elif ejercicio == "C":
            actividad = 1.55
        elif ejercicio == "D":
            actividad = 1.725
        elif ejercicio == "E":
            actividad = 1.9
        tmb_2 = tmba(tmb,actividad)
        print(f"Actividad fisica de: {tmb_2} ")
        return tmb_2

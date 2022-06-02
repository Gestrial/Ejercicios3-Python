"""
Tasa metabólica basal según actividad física
Dado que las personas realizamos actividad física en el día, el consumo de calorías diarias
(el cual denominaremos TMB_(actividad_fisica) ) es mayor al TMB. Para poder calcularlo
es necesario multiplicar el TMB por un valor que depende de la actividad física semanal
que realiza cada persona:
TMB_(actividad_fisica) = TMB * valor_actividad
Donde valor_actividad es un valor que depende de la actividad física que lleva a cabo la
persona semanalmente y toma los siguientes valores:
 1.2: poco o ningún ejercicio
 1.375: ejercicio ligero (1 a 3 días a la semana)
 1.55: ejercicio moderado (3 a 5 días a la semana)
 1.72: deportista (6 -7 días a la semana)
 1.9: atleta (entrenamientos mañana y tarde.
"""

from Funciones import tasaMB2, tmba


def tmb_():
        tmb = tasaMB2()
        ejercicio = input("Cuanto ejercicio realiza por semana:\n A) Poco. \nB) Ligero. \nC) Moderado. \nD) Deportista \nE) Atleta \n[A/B/C/D/E]? : ")
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

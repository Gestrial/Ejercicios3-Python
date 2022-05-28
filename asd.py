
print("--------------------------VALORES--------------------------------")
print("-----------------------------------------------------------------")
print("--------------IMC = INDICE DE MASA CORPORAL----------------------")
print("--------------GC = PORCENTAJE DE GRASA CORPORAL------------------")
print("--------------TMB = TASA METABOLICA BASAL------------------------")
print("--------------TMB_AF = TASA METABOLICA SEGUN ACTIVIDAD FISICA----")
print("--------------CA = CALORIAS DIARIAS PARA ADELGAZAR---------------")
print("-----------------------------------------------------------------")

from Inputs import asd


def main():
    while True:
        opcion2 = asd()
        if opcion2 == 1:
            from Ejercicio1 import indiceMC
            indiceMC()
        elif opcion2 == 2:
            from Ejercicio2 import porcentajeGC
            porcentajeGC()
        elif opcion2 == 3:
            from Ejercicio3 import tasaMB
            tasaMB()
        elif opcion2 == 4:
            from Ejercicio4 import tmb_
            tmb_()
        elif opcion2 == 5:
            from Ejercicio5 import adelgazar
            adelgazar()

        opcion3 = input("Desea calcular algo mas ? S/N ")
        if opcion3 == "N":
            break
        elif opcion3 == "S":
            continue

main()




    

       

        


        
        


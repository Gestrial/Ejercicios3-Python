from Funciones import adelgazando,tasaMB2
from Inputs import selector

# EJECUTAR DESDE MAIN

def adelgazar():
    a = tasaMB2()
    opcion = selector()
    valor = ""
    valor2 = ""
    symbol = ""
    if opcion == "A":
        valor = 0.15
        valor2 = 0.20
        symbol = "-"
    elif opcion == "B":
        valor = 0.80
        valor2 = 0.85
        symbol = "+"
    b = adelgazando(a,valor,symbol,valor2)
    return b


        

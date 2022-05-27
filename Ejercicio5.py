"""
Cálculo de las calorías diarias para adelgazar
En general, si las personas desean adelgazar deben reducir las calorías que ingieren a
diario y/o deben aumentar el gasto calórico haciendo más deporte. Si se escoge la primera
opción, se recomienda que las personas ingieran a diario entre un 15% a 20% menos
calorías de las que arroja la TMB. Lo anterior sugiere que una persona que desee
adelgazar debe consumir entre 80% y 85% de las calorías que representa la TMB.
"""

from Funciones import adelgazando,tasaMB2

def adelgazar():
    a = tasaMB2()
    opcion = input("Que desea hacer:\nA) Reducir calorías. \nB) Aumentar gasto calórico. \nRespuesta: ")
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

adelgazar()
        

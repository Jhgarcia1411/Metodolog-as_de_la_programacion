"""
Utilizamos while para ejecutar un codigo cuando sea verdadera 


Estructra:

While condition: 
     #Bloque de codigo a ejecutar
"""


#Ejemplo basico con un while
#Verificar si un numero esta en un rango espesifico
#Rango espesifico 10 y entre 20

while True: #while loop infinito
    number = (input("ingrese un numero entre 10 y 20"))

    if number < 20 and number > 10:
        print("el numero esta dentro del rango")
    else:
        print("El numero esta fuera de rango")



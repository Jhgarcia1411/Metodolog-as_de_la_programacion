"""
Vamos a realizar un programa que sume numeros hasta que el 
usuario escriba la palabra "salir"

El programa tambien debe decirme cuantos numeros ingreso 
el usuario, cual fue el minimo y cual fue el maximo.

"""

sum_numbers = 0.0
counter = 0
minimum = None
maximum = None


while True:
    print("ingresa la palabra 'salir' para termiar")
    user_input =  input("ingresa una cantidad (MXN): ")

    #Centinel
    if user_input == 'salir'
        break

    try:
        quantity = float(user_input)
    except ValueError:
        print('cantidad no valida')
        continue
    except KeyboardInterrupt:
        break

    counter += 1
    sum_numbers = sum_numbers + quantity

    if minimum is None or quantity < minimum:
        minimum = quantity

    if maximum is None or quantity < maximum:
        maximum = quantity



















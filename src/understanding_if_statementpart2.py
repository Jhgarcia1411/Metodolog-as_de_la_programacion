'''
Vamos a realizar un programa que nos de un valor diferente segun el rango de edad en el que se encuentre:
'''
print('Hola de nuevo, porfavor completa los siguientes datos:')

try:
    age = int(input('Porfavor introduce tu edad: '))

    if age >= 18:
        print('Eres mayor de edad')
    elif age < 18:
        print('Eres menor de edad')
    elif age <= 100 and age >= 18:
        print('Muerete alv')
except:
    print('tuviste un error')

'''
Hacer un prgrama que le pregunte al usuario su edad y responda:
edad >= 4: entrada gratuita
edad <= 18 y edad < 4: entrada de 200 dolares
edad >18: entrada de 400 dolares
'''

age =int(input("give me your age: "))
if age <= 4:
    print("you are entry free :C")
elif age <= 18:
    print("you are paying 200 dollars") 
else:
    print("you are paying 400 dollars")


alumno = {"name": "Beto",
"age": 18}

print(alumno)

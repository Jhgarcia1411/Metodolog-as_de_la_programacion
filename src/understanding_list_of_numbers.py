"""
Las listas tambien pueden almacenar numeros y de hecho son ideales para hacerlo.
Python ofrece varias maneras de trabajar con listas de numeros, incluyendo ordenamiento,

Por ejemplo, range() genera una lista de numeros en un rango especifico.
"""

#Por ejemplo, usando range() generamos una lista de numeros del 0 al 9

numbers = list(range(10))  # Genera una lista de numeros del 0 al 9
print(numbers)  # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(numbers))  # Salida: <class 'list'>


#Podemos hacer lo mismo con un for loop

print("Numeros del 0 al 9:")
for num in range(10):
    print(num)
    
print("Numeros del 1 al 4:")
for num in range(1, 5):
    print(num)

numbers_1_to_4 = list(range(1, 5))  # Genera una lista de numeros del 1 al 4
print(numbers_1_to_4)  # Salida: [1, 2, 3, 4]


print("Numeros impares del 1 al 9:")
for num in range(1, 10, 2): #imprime numeros impares del 1 al 9
    print(num)
odd_numbers = list(range(1, 10, 2))
print(odd_numbers)  # Salida: [1, 3, 5, 7, 9]

print("Numeros pares:")
for num in range(2, 10, 2): #imprime numeros pares del 2 al 8
    print(num)
even_numbers = list(range(2, 10, 2))
print(even_numbers)  # Salida: [2, 4, 6, 8]

#En conclusion podemos crear caulquier lista de numeros usando range() y list()

print("\n Primeros 10 numeros al cuadrado:  ")
squared_numbers = []
for value in range(1, 11):
    squared = value ** 2
    squared_numbers.append(squared)
print(squared_numbers)  # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#Metodos build-in para trabajar con listas de numeros
print("\n Metodos built-in para listas de numeros:")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("lista de digitos:", digits)
print("minimo:", min(digits))  # Salida: 0
print("maximo:", max(digits))  # Salida: 9
print("suma de todos los digitos:", sum(digits))    # Salida: 45


list_comp = [num ** 2 for num in range(10)]
print(list_comp)
# Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
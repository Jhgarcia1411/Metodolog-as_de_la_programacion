

"""
.sort(): Ordena los elementos de una lista en orden alfabetico o numerico.
ordenamiento permanente de la lista, es decir, ordena la lista permanentemente.

"""
#Metodo sort() 

cars = ['bmw','audi','ford','kia']
print(cars) #Salida: ['bmw','audi','ford','kia']
cars.sort()
print(cars) #Salida: ['audi','bmw','ford','kia']

#Metodo sort() con reverse=True

cars = ['bmw','audi','ford','kia']
print(cars) #Salida: ['bmw','audi','ford','kia']
cars.sort(reverse=True)
print(cars) #Salida: ['audi','bmw','ford','kia']

"""
Metodo reverse(): invierte el orden de los elementos en la lista.
ordenamiento permanente de la lista, es decir, invierte la lista permanentemente.
"""

#Metodo reverse()

motocycles = ['honda','yamaha','suzuki']
print(motocycles) #Salida: ['honda','yamaha','suzuki
motocycles.reverse()
print(motocycles) #Salida: ['suzuki','yamaha','honda


"""Metodo len(): devuelve la cantidad de elementos en una lista.
metodo built-in len() que se puede usar con cualquier tipo de lista.
"""

#Metodo len()

cars = ['bmw','audi','ford','kia']
print("\n metodo built-in len()")
print(len(cars)) 

"""
Metodo built-in
    sorted(): ordena temporalmente los elementos de una lista en orden alfabetico o numerico.
    no altera la lista original, solo devuelve una nueva lista ordenada.
"""

favorite_students = ['alice','bob','charlie','david']
print(favorite_students)
print("lista temporal:", sorted(favorite_students, reverse=True)) #Salida: ['david','charlie','bob','alice']
print("lista original:", favorite_students)
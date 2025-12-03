# List comprehension 
"""
Es una list comprehension convina for y la creacion de nuevos elementos
en una sola linea de codigo y tambien agrega elementos en una sola linea de codigo sin utilizar append 
"""

squares = [value ** 2 for value in range(1, 10)]
print(squares)

#Numeros pares con el range
even_umbers_0_100_range = list(range(0,101,2))
print(even_umbers_0_100_range)

#Numeros pares con list comprehension
evens_list_compre = [value for value in range(0,100) if value%2 == 0]
print(evens_list_compre)
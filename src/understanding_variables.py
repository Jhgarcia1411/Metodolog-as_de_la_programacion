message = "this is a variable"
another_message = "this is another variable"

print(message)
print(another_message)

print(massege, another_message, message, message)
print(nother_message, message)  # Intentional typo to demonstrate error handling

charly_message = "hola soy cjarly y estoy aprendiendo python"
print(charly_message)

"""
traceback: el interprete de python no puede encontrar la variable 'massege' ni 'nother_message' ni 'charly_mesage' porque están mal escritas.

ejemplo
traceback:

Traceback (most recent call last):
  File "C:\Users\hp\projects\Metodolog-as_de_la_programacion\src\understanding_variables.py", line 7, in <module>
    print(massege, another_message, message, message)
          ^^^^^^^
NameError: name 'massege' is not defined. Did you mean: 'message'?

nameError: significa que debemos establecer el valor de una variable antes de usar o cometimos un error al ingresar el nombre de la variable.
"""
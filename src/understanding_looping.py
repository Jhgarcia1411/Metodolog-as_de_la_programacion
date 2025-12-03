"""
for iterable:
    actions
    (se separa cuatro espacios)
    El bucle for itera sobre una secuencia (como una lista, tupla o cadena) y ejecuta un bloque de codigo para cada elemento en la secuencia. 

"""

#Metodo for

transformers = ['optimus prime', 'bumblebee',  'ironhide', 'ratchet',  'sideswipe', 'wheeljack', 'jazz', 'ultra magnus']

for transformer in transformers:
     print(transformer)
     print(transformer.upper())
     print(f"{transformer.title()} Autobots roll out")
     print("\n")
    

"""
Identacion: python utiliza la identacion para determinar cuando una linea de codigo esta
conectada a la linea de codigo a la linea de codigo anterior.

Basicamente se utilizan 4 espacios en blanco para obligarnos a escribir
codigo ordenado y legible.
"""
#no olvidemos identar (donde se necesita)
#Ejemplo
decepticons = ['megatron', 'starscream', 'soundwave', 'shockwave', 'thrust']
for decepticon in decepticons:
     print(decepticon)
     print(f"{decepticon.title()} Decepticons rise up!")
     print("\n")


#Error de sintaxis por falta de identacion
"""
El error de sintaxis ocurre cuando no se agregan los dos puntos (:)
o cuando no se escibe debidamente la identacion.
"""

#Simple dictionary

alien_0 = {'color': 'green', 'points': 4}

#The simple dictionary

alien_1 = {'color': 'yellow'}

#Accesing values in a dictionary

print(alien_1['color'])
print(alien_0['points'])

#Empty dictionary
alien_2 ={}

#Modifying values in a dictionary

alien_2 = {'color': 'yellow'}
alien_2['color'] = 'blue'

#Adding new key-value pairs
alien_2['x_position'] = 12
alien_2['y_position'] = 19

print(alien_2)

#Dictionary to store similar objects
favorite_lenguajes = {
    'jen': 'python',
    'sarah': 'c++',
    'edward': 'rubi',
    'phill': 'python',
}

#
for key, value in favorite_lenguajes.items():
    print(f"{key.title()}'s favorite \
lenguaje is {value.title()}.")

for key in favorite_lenguajes.keys():
    print(key)

for value in favorite_lenguajes.values():
    print(value)

#Nestings en diccionarios

## Listas de diccionarios
covenant_grunt = {
    "color": "orange",
    "weapon": "plasma gun",
    "healt": 2
}

covenant_elite = {
    "color": "blue",
    "weapon": "plasma sword",
    "healt": 7
}

covenant_jackal = {
    "color": "grey",
    "weapon": "plasma grande",
    "healt": 5
}

covenants = [
    covenant_grunt,
    covenant_elite,
    covenant_jackal
]

for covenant in covenants:
    print("/n", covenant)
    for key, value in covenant.items():
        print(f"{key}:{value}")

## Listas en diccionarios








## Diccionarios en diccionarios



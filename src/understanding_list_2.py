#SLICING
players = ["cr7", 'messi', 'Travis', 'chicharito', 'corona']
print(players[0:3])
# Slice es trabajar con un grupo especifico de elementos de una lista
print(players[1:4])
print(players[:4])
print(players[2:])

print("Aqui vienen los mejores jugadores del grupo: ")
    
for player in players[0:3]:
    print(player)

#Copiar una lista
my_food = ['pizza', 'hamburguesa', 'gorditas']

#copy_of_food = my_food forma erronea

copy_of_food = my_food[:]
copy_of_food_2 = my_food.copy()
copy_of_food_3 = list(my_food)

#Modificando elementos

cars = ["mbw", 'porch', 'masa', 'totoya', 'ford']
cars[0] ="BMW"
cars[1] ="Porshe"
cars[2] ="Masda"
cars[3] ="Toyota"
cars[4] ="Ford"
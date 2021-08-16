# Las tuplas nos permiten generar un dato semejante a las listas, pero que NO PUEDEN CAMBIAR
# Las tuplas son mas rapidas que las listas (esto lo dice el profesor, no me consta)

x = (1, 2, 3)
print(x)
print(type(x))

print('******************************************')

print('Aquí podemos ver que operaciones podemos hacer con un dato tipo TUPLE')

print(dir(x))


print('******************************************')

print('Si dentro de la tupla, definimos un solo dato, se le considera, como dato del tipo que ingresas, la tupla tiene que tener mas de un elemento o insertas un dato dentro de la tupla, seguido de una coma')

ejemplo = (1)
print(ejemplo)
print(type(ejemplo))

print('Aqui aqui podemos ver como si se declara una tupla con un elemento')

ejemplo02 = (1,)
print(ejemplo02)
print(type(ejemplo02))


print('******************************************')

variable02 = (1, 2, 3, 4, 5, 6)

print(variable02)

# Aquí estiy inprimiento el lugar numero cuatro de la tupla, el resultado es el numero "5", porque recuerda que la cuenta siempre parte en cero.
print(variable02[4])


print('******************************************')

# del ejemplo02 #Aquí estoy eliminando la tupla

# print(ejemplo02) #Aquí pido imprimir la tupla, pero va a dar un error porque la he eliminado, luego vamos a comentar esta linea.


print('******************************************')

# Aquí estoy definiendo una variable, con un diccionario de Tuplas, entonces, en el diccionario, puedo definir mas de una variable, pero recordemos que tienen que ser del mismo tipo.

locations = {
    (35.12323, 39.4211): "Tokyo",
    (98.5646, 78.49865): "New York"
}

print(locations)

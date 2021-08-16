# El tipo de dato set, es una coleccion de datos desordenada y que no tiene un indice.

colors = {'Red', 'Green', 'Blue'}

print(type(colors))

print('Aquí vemos que Python nos indica que el tipo de dato es SET - print(type(colors))')

print('******************************************')

print(dir(colors))

print('Aquí vemos todas las operaciones permitidas con el dato de tipo SET')


print('******************************************')

print('Red' in colors)

print('Aquí estamos preguntando si el dato RED, se encuentra en el set, nos responde un boolean')

print('******************************************')

colors.add('Violet')

print(colors)

print('Aquí le indicamos a la variable de tipo set, que agrege el color violeta')
print('Fijarse que lo agrega al principio, porque el tipo de dato set, no tiene indices')


print('******************************************')

colors.remove('Red')
print(colors)

print('Aquí le indicamos que elimine de colors, a Red.')

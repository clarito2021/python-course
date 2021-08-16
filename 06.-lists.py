#Recordemos como son las listas
print ('Recordemos como se ve una lista')

listademo=[1,'hola', 10.5, 'kkpura']

print (listademo)
print (type(listademo))

print ('******************************************')

print ('Estas son las operaciones que tenemos disponibles con los datos typo lista o LIST')
print (dir(listademo))

print ('******************************************')

print ('Puedo crear varios tipos de lista, por ejemplo, ahora voy a crear una lista que tiene varios tipos de dato e incluso tambien tiene una lista definida entre corchetes y la lista que defini en el parametro anterior.')

listademo02 = [5, 0.5, 'rojo', [1, 5, 8, 0.7], listademo]
print (listademo02)

colors = ['red', 'green', 'blue']

print ('******************************************')

numbers_list = list((1, 2, 3, 4, 5, 6))
print (numbers_list)
print (type (numbers_list))


listarango = list(range(1,11))
print (listarango)


print ('******************************************')

print (type (listarango))

print (len(listarango))

print(colors[2])
print(colors[-2])

print ('green' in colors)
print ('4' in colors)


print ('******************************************')

print (colors)
colors[1]='Aqui he cambiado el dato de la lista!!!!'
print (colors)

print ('******************************************')


#colors.append(('violeta', 'amarillo patito'))
colors.extend (['Negro','Negro de mierda'])

#colors.insert (1, 'color insertado aquí')
#colors.insert(len(colors), 'Color insertado al final')
#print (colors)
#colors.pop()
#colors.pop()
#colors.pop()

colors.remove ('Negro')

print (colors)

#colors.clear

colors.sort()

print (colors)

colors.sort(reverse=True)

print (colors)


print(colors.index('blue'))
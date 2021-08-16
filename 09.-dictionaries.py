# El diccionario es un tipo de dato que agrupa muchos datos.

product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "first_name": "Ryan",
    "last_name": "Kirk"
}


print(product)
print(person)


print('******************************************')

print('Aquí podemos ver cuales son las operaciones permitidas con las variables tipo dictionary')

print(dir(product))

print('******************************************')

print(person.keys())
print(person.items())
print(person.__contains__('Reyes'))

print('******************************************')

print('Aquí estamos definiendo e imprimiendo en pantalla una lista de diccionarios.')

productos = [
    {"name": 'book', "price": '10.99'},
    {"name": 'laptop', "price": '1570.99'}
]

print(productos)

print('******************************************')

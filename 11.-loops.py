foods = ['apples', 'bread', 'cheese', 'milk',
         'graves', 'vine', 'cereal', 'banana']

print('******************************************')


print("Aquí vemos la salida si imprimimos los indices especificados uno por uno")

print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])

print('******************************************')


print("Acá, vemos el mismo resultado en pantall, pero usando el comando for")

for food in foods:
    print(food)

print('******************************************')

print("Acá, le damos una condición para que mientras se esté ejecutando el for, si encuentra la condición que solicitamos, entonces, imprime lo que solicitamos")


for food in foods:
    if food == "cheese":
        print("You have to buy cheeese...")
    print(food)

print('******************************************')

print("Acá, si encuentra la palabra cheese, ejecuta un break y no se ve nada en pantalla")


for food in foods:
    if food == "cheese":
        print("You have to buy cheeese...")
    break


print('******************************************')
print("Acá, también ejecutamos un break, sin embargo, le damos el comando imprir, por lo tanto, tentemos un input,")

for food in foods:
    if food == "cheese":
        break
print("encontramos queso en la lista, asi que imprimimos QUESO")
print('******************************************')


for food in foods:
    if food == "cheese":
        continue
    print(food)


print('******************************************')

for number in range(1, 10):
    print(number)

print('******************************************')

for letter in "Hello":
    print(letter)


print('******************************************')

count = 4
while count <= 10:
    print(count)
    count = count + 1

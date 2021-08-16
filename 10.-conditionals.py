
# Aqupi es importante conocer algunos operadores de comparación
# 3 > 2 retornará TRUE
# 3 < 2 retornará FALSE
# 3 == 3 retornará TRUE
# 3 == 4 retornará FALSE

x = 40
y = 80

if x < 30:
    print("x is less than 30")
else:
    print("40 no es menor que 30")

print('******************************************')


color = "blue"

if color == "red":
    print("the color is red")
elif color == "blue":
    print("the color is blue")
else:
    print("any color")

print('******************************************')

name = "Jhon"
lastname = "Carter"

if name == "Jhon":
    if lastname == "Carter":
        print("You are Jhon Carter")
    else:
        print("You are not Jhon")
else:
    print("You are not Jhon2")


print('******************************************')

print('Ejemplo con las variables name y lastname')

name = "Ryan"
lastname = "Carter"

if name == "Jhon":
    if lastname == "Carter":
        print("You are Jhon Carter")
    else:
        print("You are not Jhon")
else:
    print("You are not Jhon2")


print('******************************************')

print('Otro Ejemplo pero con X que en este caso, tiene el valor 40:')
print(' ')

if x > 2 and x <= 10:
    print("x is greater than two and less than or equal to ten", "x es igual a", x)
elif x == 40:
    print("La condición no se cumple, solo imprimimos el valor de X:", x)


print('******************************************')

print('Otro Ejemplo pero con X y Y que en este caso, tiene el valor 40:')
print(' ')

if x > 2 and y == 80:
    print("la condición x mayor a dos e y igual a ochenta, se cumple")

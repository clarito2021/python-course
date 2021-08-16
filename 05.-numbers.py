entero = 10
flotante = 10.5

print (10)
print (10.5)
print (type(10))
print (type(10.5))

print ('******************************************')
print ('Aqui podemos ver que funciones hay asociadas a una variable de tipo NUMERO ENTERO')
print ('******************************************')

print (dir(entero))

print ('')

print ('******************************************')
print ('Aqui podemos ver que funciones hay asociadas a una variable de tipo NUMERO FLOAT')
print ('******************************************')

print (dir(flotante))
print (flotante.hex)
print ('******************************************')
print ('')
print (1 + 1) #suma de dos enteros
print (3 - 1) #resta de dos enteros
print (3 - 10) #resta de dos enteros que entrega un numero negativo
print (5 * 1.9) #multiplicacion de un entero por un flot, resultado un float
print (3 * 2) #multilpicacion de dos enteros
print (3 / 2) #division de dos enteros que da como resultado un flot
print (1 + 1.8) # suma de un entero, mas un flotante, integer + float, resultado un float
print (2 ** 3) #con esta operacion, estamos elevando dos al cubo
print (2 ** 100) #estamos elevandos dos a la centecima potencia, el resultado seria 1267650600228229401496703205376
print (3 // 2) #esta operacion se llama operador de modulo, solo devuelve la parte entera de una division entre numeros, es decir, la division entre 3/2, da como resultado 1.5, con este operador, solo obtenemos la parte entera
print (10 % 3) #esta es una operacion de porcenaje, que se comporta como la operacion anterior, pero no es lo mismo, por eso es importante conocer la operacion anterior llamada operacion de modulo
print (20 - 10 / 5 * 3 ** 2) #en este segmento, vemos el resultado de una tabla de precedencia, en donde ponemos una operacion compleja, pero el interprete, siguiendo las reglas matematicas basicas, resuelve las operaciones en orden de importancia
         #en este caso, se resolvera la exponenciacion tres al cuadrado, luego resolvemos las multiplicaciones o divisiones, en este caso el cinco por el resultado de la exponenciacion tres al cuadrado
         #lueego el resultado de la division, luego el de la multiplicacion y luego las sumas y restas, debe dar como resultado el numero dos.

print ((20 - 10) / (5 * 3 ** 2)) #sin embargo, al aplicar parentesis, le estamos diciendo al interprete de Python, que operacion es mas importante, lo que este en el parentesis, es lo que se ejecutara primero, el resultado cambia.
print (20 - 10 / (5 * 3 ** 2)) #sin embargo, al aplicar parentesis, le estamos diciendo al interprete de Python, que operacion es mas importante, lo que este en el parentesis, es lo que se ejecutara primero, el resultado cambia.

print ('******************************************')
print ('Aqui pondremos un pequeno programa para revisar que podemos hacer con los numeros')
print ('******************************************')

age = input ("Insert your age: ") #la funcion input me permite insertar informacion, interactuando con el usuario final, sin embargo, esta informacion, solo sera en formato STRING

print ('Thanks!')
print ('your age is {0}'.format (age)) #aca, estoy imprimiendo lo que el usuario inserto por pantalla

new_age = int(age) + 11 #aca esstoy transformando lo que ingreso el usuario a un numero entero, se va a caer el programa si el usuario ingresa algo que no sea un numero, luego de hace esa transformacion, le estoy sumando 11

print ('you know how old you will be in eleven year?, the answer is: {0}'.format(new_age)) #aca le muestro el resultado de su edad mas 11
print ('enjoy your life, you just have one...')
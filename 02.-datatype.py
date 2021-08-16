print ('*************************************')
print   ('Ejercicio 02: Tipos de datos')
print ('*************************************')

#Ejemplo de Strings
#Hay que considerar que se debe poner atencion con los espacios, mayuscylas y minusculas

print ('---------------------------------------')
print ('Los STRINGS, pueden ser datos de distintos tipos, existen diferencias entre un dato definido entre comilla simple o comilla doble, podemos crear datos hasta con triples comillas simples o dobles')
print ('a continuacion hay varios strings definidos, escritos de distinta forma, pero son todos el mismo tipo de dato, STRING.')
#Strings
print ('Datos tipo STRING ')
print ("is")
print (type ('Datos tipo STRING '))
print ('Ejemplos:') 
print ("Hello World")
print ("Hello world")
print ('''Hello World''')
print ("""Hello World""")
print (type ("Hello World"))
print (type (100))    
print ("Bye" + "World")
print (3+10)    

print ('---------------------------------------')

#Numeros
print ('Datos tipo NUMEROS o ENTEROS o INTEGER')
#Integer - enteros
print (30) 
print ("is") 
print (type (30))

print ('---------------------------------------')


#Float - decimales
print ('Datos tipo DECIMALES o FLOAT ')

print (30.5)

print ('---------------------------------------')


#Boolean - boleano - tipo de dato logico
print ('Datos tipo BOOLEAN' )

print (True)
print ('is')
print (type (True))
print ('and')
print (False)
print ('is')
print (type (False))

print ('---------------------------------------')


#List - Datos tipo listado
print ('Datos tipo LIST o LISTADO' )
print ('Los datos de una lista pueden cambiar, es su principal carasteristica, junto con que los datos de la lista, no tienen que ser necesariamente del mismo tipo')

print ([10, 20, 30, 40, 50])
print ('is')
print (type ([10, 20, 30, 40, 50]))
print ('---------------------------------------')

print (['Hello', 'Bye', '10', '10.5'])
print ('is')
print (type (['Hello', 'Bye', '10', '10.5']))

print ('---------------------------------------')
print (['Bye', 'Hola', 'JELOU'])
print (type (['Bye', 'Hola', 'JELOU']))

#Tuples

print ('Datos tipo TUPLES o TUPLAS' )
print ('-Los datos de una TUPLES no pueden cambiar, son inmutables, es su principal carasteristica')
print ('-Las TUPLAS, tambien se pueden crear vacias')
print ('-Las TUPLES, se deben escribir con parentesis redondo')

(10, 20, 30)
()

print ((10, 20, 30))
print ('is')
print (type((10, 20, 30)))

#Dictionary 
print ('---------------------------------------')
print ('Datos tipo DICTYONARY o DICCIONARIO' )
print ('Son datos que estan agrupados por clave y valor, en el ejemplo Apellido es la clave, Ray es el valor' )


print ({
"Nombre de la persona":"Ryan",
"Apellido":"Ray",
"Seudonimo":"FAZT"
})
print ('is')
print (type ({
"Nombre de la persona":"Ryan",
"Apellido":"Ray",
"Seudonimo":"FAZT"
}))

print ('---------------------------------------')

#Nonetype 
print ('---------------------------------------')
print ('Datos tipo NoneType' )
print ('Son datos que estan vacios, en Python, se pueden definir datos que aun no tengan valor' )

print (None)
print (type (None))
print ('---------------------------------------')

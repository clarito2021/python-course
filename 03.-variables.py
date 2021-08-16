print ('*************************************')
print   ('Ejercicio 03: Variable, Constantes y Convenciones al respecto')
print ('*************************************')

#defnicion variable espacio, solo para formatear mejor el output
espacio = ' '

#variables

print ('***********VARIABLES***********')
print ('La variable "name", tiene asignado el valor Carlos')
print (espacio)

name = "Carlos" #este es el nombre de mi variable
print (name)
print ('is')
print (type(name)) #en esta linea imprimo el tipo de dato de mi variable
print (espacio)

print ('---------------------------------------')
print (espacio)

print ('La variable "numero", tiene asignado el valor 100')

numero = 100
print (numero)
print ('is')
print (type (numero))
print (espacio)


print ('---------------------------------------')

print ('La variable "suma", tiene asignado el 3+2')
print (espacio)

suma = (3+2)
print (suma)
print ('is')
print (type (suma))
print (espacio)


print ('---------------------------------------')

print ('La variable "listado", tiene asignado el valor de una lista de distintos datos')
print (espacio)


listado = ['Hello', 'Bye', '10', '10.5']

print (listado)
print ('is')
print (type (listado))
print (espacio)


print ('---------------------------------------')

print ('La variable "tuplas", aunque suene redundante, tiene asignado el valor de una lista de distintos datos')
print (espacio)


tuplas = (10, 20, 30)

print (tuplas)
print ('is')
print (type (tuplas))
print (espacio)


print ('---------------------------------------')

print ('La variable "estado01" & "estado02", tiene asignados valores tipo Boolean')
print (espacio)

estado01 = True
estado02 = False

print (estado01 , estado02)
print ('are')
print (type(estado01))
print (espacio)

print ('---------------------------------------')

print ('La variable "diccionario"'', tiene asignados valores tipo Diccionario')

print (espacio)

diccionario = {"Nombre de la persona":"Ryan",
"Apellido":"Ray",
"Seudonimo":"FAZT"}

print (diccionario)
print (espacio)

print ('is')
print (espacio)

print (type (diccionario))
print (espacio)


print ('---------------------------------------')

print ('La variable "nada_definido", tiene asignado el valor tipo NoneType')

nada_definido = None

print (nada_definido)
print (espacio)

print ('is')
print (espacio)

print (type (nada_definido))



#convenciones sobre como escribir variables

#Casesensity determina que aunque dos variables tengan el mismo nombre, si van on mayusculas o minusculas, no seran lo mismo

print ('***********CONVENCIONES SOBRE COMO ESCRIBIR VARIABLES o CONSTANTES***********')
print (espacio)

print ('Ejemplos de Casesensity')
print ('A continuacion escribos tres variables llamadas "book", "Book" y "BoOk", todas con valores distintos, suenan igual, pero para Python, no son lo mismo incluso tienen tipos de datos distintos')
print (espacio)

book = 'Orgullo y Prejuicio'
Book = True
BoOk = '65498654654'

print (book, Book, BoOk)
print (espacio)
print ('book')
print ('is')
print (type(book))
print (espacio)

print (espacio)
print ('Book')
print ('is')
print (type(Book))
print (espacio)


print (espacio)
print ('BoOk')
print ('is')
print (type(BoOk))
print (espacio)


print ('---------------------------------------')
print (espacio)
print ('hay que considerar que no se puede escribir cualquier nombre de variable, Python, acusara en rojo, cuando una variable este mal escrita, porque Python, no lo entendera')
print ('a continuacion nombre no permitido y nombres permitidos por el compilador.')
print (espacio)
print ('CORRECTO   = _2book =')
print ('CORRECTO   = asdasd =')
print ('INCORRECTO = 2book =')
print (espacio)
print ('---------------------------------------')
print (espacio)


print ('---------------------------------------')

print ('Tambien puedo definir e imprimir mis variables en una sola linea')

x,libro, condicion= 10, "El Quijote", False

print (x, libro, condicion)

print (espacio)
print ('---------------------------------------')
print (espacio)
#constantes

print ('Las Constantes se escriben en MAYUSCULA, al interprete de Python, le da lo mismo, pero por orden, es mejor hacerlo asi')

PI = 3.1416

print (PI)
print ('is')
print (type (PI))

print (espacio)
print ('---------------------------------------')
print (espacio)
    
#convenciones sobre como escribir constantes

print ('Convenciones sobre como escribir el nombre de las variables')
print ('book_name, a esta forma se le como Snakecase')
print ('bookName, a esta forma se le como Camelcase')
print ('BookName, a esta forma se le como Snakecase')

print ('---------------------------------------')
print (espacio)
print ('La mas usada en Python, es SnakeCase, y estas convenciones sirven para manejar un codigo mas ordenado, no se recomienda cambiar entre una y otra forma en un mismo programa')

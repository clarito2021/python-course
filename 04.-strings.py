#Defininos una variable y le asignamos datos tipo String
#Definimos variables para formatear la salida de manera rudimentaria

myStr = "hello world"
espacio = " "
linea = "-----------------------------------"

#con el siguiente comando dir(), podemos ver que tipo de funciones hay asociadas a un dato tipo string

print (espacio)
print (linea)
print (espacio)

print ('Tipos de funciones predefinidas en Python,  que se pueden asociar a un dato String')

print (espacio)
print (linea)
print (espacio)

print (dir(myStr))

#luego, una vez que revisamos el output, podemos jugar con las funciones, utilizando la sintaxys que vemos a continuacion
print (espacio)
print (linea)
print (espacio)


print (myStr.upper()) #regresa una copia del string, en letras mayusculas
print (myStr.lower()) #retorna una copia del string, en minusculas, en este caso, no hara nada, porque el string, esta en minusculas
print (myStr.swapcase()) #retorna los caracteres de string que estaban en minusculas a mayusculas y viceversa
print (myStr.replace('hello', 'bye')) #retorna en la copia del string, una palabra o dato de reemplazo, segun lo definanos dentro de los parametros de la funcion replace
print (myStr.count('l')) #lo que hace esta funcion, es contar el numero de caracteres que aparecen en el string, en este caso la letra "l", tambien puede contar espacios vacios, al poner un espacio entre las comillas
print (myStr.startswith ('hello')) #con esta funcion, lo que hago es preguntar si el sting, empieza con la palabra "hello", retornara un boolean, en este caso TRUE
print (myStr.startswith ('Hola')) #con esta funcion, lo que hago es preguntar si el sting, empieza con la palabra "Hola", retornara un boolean, en este caso FALSE
print (myStr.endswith ('world')) #con esta funciono, preguntamos si le string termina en una palabra determinada, en este caso, debe retornar TRUE
print (myStr.replace('hello', 'bye').upper()) #aqui podemos ver como unir dos funciona, primero replace y luego upper, esta sintaxys puede ser  muy util, son metodos encadenados
print (myStr.split()) #esta funcion separa el string y retorna una lista, pero a partir de un espacio en blanco, pero si en los parametros de la funcion, podemos poner otro caracter, un espacio, una coma, lo que Python pueda entender
print (myStr.find ('o')) #esta funcion encuentra un caracter en particular, en este caso, retorna un cuatro, porque la o tene la poscicion cuatro, si lo cambiamos, cambia el valor
print (myStr.__len__()) #esta funcion, entrega el largo del string, retorna 11, porqe parte en cero
print (myStr.index ('d')) #busca donde esta un caracter determinado dentro del string

print (myStr.isalpha()) #con esta funcion, pregunto si el string esta en orde alfabeticoa, ahora respondera FALSE
print (myStr.isalnum()) #con esta funcion, pregunto si el string es lfanumerico, en este caso, respondera FALSE
print (myStr[4]) #con este comando, imprimo lo que esta en la posicion 4 del string, RECORDAR QUE LOS STRING PARTEN CON LA POSICION CERO
print (myStr[0])
print (myStr[1])
print (myStr[2])
print (myStr[3])
print (myStr[4])
print (myStr[5])
print (myStr[6])
print (myStr[7])
print (myStr[8])
print (myStr[9])
print (myStr[10])

print ('Esta string se llama'+myStr) #de esta forma vemos como es que se concatenan dos strings, uno es el que escribimos como parametro en print, mas la variable que definimos previamente

print ("Esta string se llama {0}".format(myStr)) #de esta forma, podemos escribir un sting, mencionandolo como paraetro, con la funcion format, en donde, la funcion, insertara la variable tipo string en donde le indiquemos mediante los parentesis de llave {} y dentro de ellos el valor cero
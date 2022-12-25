# Una diferencia importante entre las tuplas y las listas es que las tuplas son más rápidas que las listas en términos de eficiencia y rendimiento. 
# Esto se debe a que las tuplas son inmutables, lo que significa que el interprete de Python puede optimizar el uso de la memoria y el acceso a los elementos de la 
# tupla de manera más eficiente que en el caso de las listas.

# En general, se recomienda utilizar tuplas en casos donde se necesite una estructura de datos que no pueda ser 
# modificada, como por ejemplo cuando se quiera representar un conjunto de valores constantes. Por otro lado, se recomienda utilizar listas en casos donde se 
# necesite una estructura de datos que pueda ser modificada, como por ejemplo cuando se quiera almacenar una secuencia de elementos que puedan ser cambiados 
# en el transcurso del programa.

#Enlace de la web: https://stackoverflow.com/questions/14135542/how-is-tuple-implemented-in-cpython

#Las tuplas son ordenadas.
#Las tuplas son inmutables
#Las tuplas permiten valores duplicados.

################### 1.CREACIÓN DE TUPLAS #####################
tupla_vacia = ()

################### 2.INSERTAR Y ACTUALIZAR #####################
#Las tuplas no cuentan con métodos de inserción y actualización puesto que son inmutables, una vez creadas no se pueden cambiar.
tupla_uno = ('Arturo','Lorenzo','Hernandez')
tupla_dos = ('R2D2', 'Coder')

################### 3.BORRADOS #####################
del tupla_vacia #Borra una tupla de memoria, no se pueden hacer borrados por elemento.

################### 4.OPERACIONES DE TUPLAS #####################
tupla_tres = tupla_uno + tupla_dos #Unión de tuplas
index_arturo = tupla_uno.index('Arturo') #Devuelve el indice de la primera aparición de ese elemento, en este caso, devuelve 0.
count_coder = tupla_uno.count('Coder') #Devuelve el número de aparaciones del elemento que se pasa por parámetro, en este caso, devuelve 1.

################### 5.OTROS METODOS #####################
tupla_num = (1,2,3)
len(tupla_num)  # Devuelve la longitud de la tupla
min(tupla_num)  # Minimo de una lista
max(tupla_num)  # Maximo de una lista
sum(tupla_num)  # Suma los elementos de la lista
len(tupla_num)  # Longitud de la lista

################### 6.ACCESO A LOS TUPLAS #####################
for elemento in tupla_tres:
    print(elemento)
# El paradigma funcional es popular porque ofrece varias ventajas sobre otros paradigmas de programación. El código funcional es:

# De alto nivel: Describe el resultado deseado en lugar de especificar explícitamente los pasos necesarios para conseguirlo. Las sentencias
# simples tienden a ser concisas, pero tienen mucha fuerza.

# Transparente: el comportamiento de una función pura depende únicamente de sus entradas y salidas, sin valores intermedios.
# Esto elimina la posibilidad de efectos secundarios, lo que facilita la depuración.

# Paralelizable: Las rutinas que no provocan efectos secundarios pueden ejecutarse más fácilmente en paralelo.

# Funciones más famosas utilizadas en programación funcional:

# map(): aplica una función a cada elemento de un iterable (como una lista) y devuelve un iterable con los resultados.
# filter(): filtra los elementos de un iterable según una función dada y devuelve un iterable con los elementos que cumplen la condición.
# reduce(): aplica una función binaria a los elementos de un iterable de forma acumulativa.
# zip(): combina elementos de varios iterables en uno solo.
# all(): devuelve True si todos los elementos de un iterable son verdaderos.
# any(): devuelve True si al menos un elemento de un iterable es verdadero.
# sorted(): devuelve una lista ordenada de los elementos de un iterable.

############################## FUNCIONES ANONIMAS #####################################

# Muchas veces necesitamos una funcionalidad en código que no tiene porque estar ligada a un nombre, por eso las funciones anonimas son muy útiles,
# especialmente en programación funcional.

numeros = [1,2,3,4]
impares = [1,3,5,7,9]
pares = [2,4,6,8,10]

reversa = lambda lista: lista[::-1]

numeros_reversa = reversa(numeros)

print(numeros_reversa)

############################## MODIFICAR UNA COLECCION #####################################

sumar_uno = lambda numero : numero + 1 
lista_modificada = list(map(sumar_uno, numeros))
print(lista_modificada)

############################## FILTRAR UNA COLECCION #####################################

es_par = lambda numero : numero % 2 == 0
lista_pares = list(filter(es_par,numeros))
print(lista_pares)

############################## USO DEL REDUCE #####################################

# El reduce sirve para hacer funciones acumuladas sobre dos parámetros de entrada.

from functools import reduce

multiplicar = lambda numero1, numero2 : numero1 * numero2

multiplicacion_acumulada = reduce(multiplicar, numeros) # Haría lo siguiente: 1 * 2 * 3 * 4

print(multiplicacion_acumulada)

############################## UNIR VARIAS COLECCIONES EN UNA #####################################

union = list(zip(impares, pares))

print(union)


############################## COMPROBAR SI TODOS LOS VALORES SON TRUE EN UNA COLECCION #####################################

son_pares = all(map(es_par, pares)) #Mapeamos cada numero par a valor True or False y después comprobamos si todo es True.
print(son_pares)


############################## COMPROBAR SI ALGUN VALOR ES TRUE EN UNA COLECCION #####################################

algun_par = any(map(es_par, numeros))

print(algun_par)
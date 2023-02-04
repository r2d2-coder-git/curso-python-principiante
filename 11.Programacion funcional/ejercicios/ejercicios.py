################### EJERCICIOS DE PROGRAMACION FUNCIONAL #####################

################### EJERCICIO 1 #####################

# Crea una función que tome una lista de números y devuelva solo los números pares. Utiliza la función filter lograrlo.

def lista_pares(numeros : list) -> list : 
    pares_filtrados = list(filter(lambda numero : numero % 2 == 0, numeros))
    return pares_filtrados

numeros = [1,2,3,4,5,6,7,8]
pares = lista_pares(numeros)
print(pares)

################### EJERCICIO 2 #####################

# Crea una función que tome una lista de palabras y devuelva solo las palabras que tienen más de n letras. Utiliza la funcion filter para lograrlo.

def palabras_n(palabras : list, longitud: int) -> list : 
    palabras_largas = list(filter(lambda palabra : len(palabra) >= longitud, palabras))
    return palabras_largas

palabras = ['hola', 'mi','nombre','es','arturo']
palabras_largas = palabras_n(palabras, 3)
print(palabras_largas)

################### EJERCICIO 3 #####################

# Crea una función que tome una lista de tuplas, donde cada tupla tiene un nombre y una edad, y devuelva una lista de nombres de las personas mayores de edad. 
# Utiliza funciones como filter y lambda para lograrlo.

def mayores_de_edad(personas : tuple):
    personas_mayores_edad = list(filter(lambda persona: persona[1] >= 18,personas))
    nombres_personas_mayores = list(map(lambda persona_mayor: persona_mayor[0], personas_mayores_edad))
    return nombres_personas_mayores

personas = [('Arturo',24),('Pepe', 19),('Ana', 10)]

personas_mayores = mayores_de_edad(personas)
print(personas_mayores)


################### EJERCICIO 4 #####################

# Crea una función que tome una lista de números y devuelva la suma de todos los números. Utiliza funciones como reduce y lambda para lograrlo.

from functools import reduce

def suma_numeros(numeros : tuple):
    suma = reduce(lambda n1,n2: n1+n2, numeros)
    return suma

numeros = [1,2,3,4,5,6,7,8]
suma  = suma_numeros(numeros)
print(suma)
    
################### EJERCICIO 5 #####################

# Crea dos listas, una con nombres y otra con edades, y utiliza la función zip para crear una lista de tuplas con los nombres y las edades asociadas. 
# Utiliza la función all para verificar si todas las edades son mayores de 18 y la función any para verificar si hay alguna edad menor a 18.

nombres =['arturo', 'alejandro','pepe']
edades = [10,18,17]

personas = list(zip(nombres,edades))


todos_mayores = all(list(map(lambda persona: True if persona[1] >= 18 else False  ,personas)))
algun_mayor = any(list(map(lambda persona: True if persona[1] >= 18 else False  ,personas)))
print(personas)
print(todos_mayores)
print(algun_mayor)




#Las listas hacen uso de arrays de longitud variable internamente, los arrays de longitud variable son una variante de los arrays 
#cuyo tamaño no se especifica inicialmente, o cuya longitud o tamaño se establece durante el tiempo de ejecución, 
#también puede llamarlos arreglos automáticos, se van redimensionando según las necesidades del programa, se dicen arrays automáticos porque cada vez que se hace un append 
#se guardan en memoria más espacio del que se necesita para prevenir redimensionar muchas veces.

#Enlace de la web: https://towardsdatascience.com/how-lists-in-python-are-optimised-internally-for-better-performance-847c8123b7fa

#Las listas en Python son ordenadas, quiere decir que cada vez que se añade un elemento tiene un orden definido, se va al final de la lista. Y cada vez que se borra un elemento
#se corren los elementos de la derecha una posición a la izquierda. [0,1,2,3,4] -> Quitamos el 2 -> [0,1,3,4]
#Las lista son cambiantes, es decir, se pueden actualizar los valores de sus elementos. 
#Las listas permiten valores duplicados.

################### 1.CREACIÓN DE LISTAS #####################

# 1. Lista vacía
lista_vacia = []
lista_vacia = list()
# 2. Lista con elementos
motocicletas = ['honda', 'yamaha', 'suzuki','honda']

################### 2.INSERCIONES Y ACTUALIZACIONES #####################

motocicletas.append('ducati') #Añade un elemento al final de la lista
motocicletas.insert(0, 'daelim') #Añade un elemento en una posición de la lista.
motocicletas[1] = 'bmw' #Actualizar una lista es muy fácil, sólo tienes que sobreescribir la posición. 

################### 3.BORRADOS #####################

elemento_cero = motocicletas.pop(0) #Borra el elemento que esté en el índice pasado por parámetro con pop y obtiene el valor borrado.
ultimo_elemento = motocicletas.pop() #El método pop sin un parámetro borra el último elemento de la lista.
motocicletas.remove('yamaha') #Borra la primera apariencia del elemento indicado y no devuelve nada
motocicletas.clear() #Borra todos los elementos de una lista
# Borrar todas las apariciones de un elemento de la lista.
while 'honda' in motocicletas:
    motocicletas.remove('honda')
    
################# 4.SORT ######################

vocales = ['e','i','o','u','a']
vocales.sort() #Ordenar alfabeticamente de forma ascendente [a,e,i,o,u]
vocales.sort(reverse=True) #Ordenar alfabeticamente de forma ascendente [u,o,i,e,a]
vocales.reverse() #Darle la vuelta a una lista
# Le podemos asignar un criterio de ordenación.
def ordenar_por_longitud(elemento):
  return len(elemento)

coches = ['Ford', 'Mitsubishi', 'BMW', 'VW']
coches.sort(key=ordenar_por_longitud)

################# 5.OTROS MÉTODOS ######################

comida = ['pizza', 'tacos', 'kebab', 'pizza', 'hamburguesa', 'pizza', 'tacos']
# IMPORTANTE: No asignar una lista a otra variable para copia la lista, 
# van a apuntar a la misma zona de memoria (friends_foods = my_foods no funciona)
copia_de_comida = comida[:] #Una forma de hacer copia de listas.
copia_de_comida = comida.copy() #Forma oficial de hacer copia de listas.
cuenta_pizzas = comida.count('pizza') #Contar el número de elementos de un valor específico, en este caso el resultado es 3.
comida.extend(['ensalada', 'manzana']) #Añadir una lista a otra lista, una forma de hacerlo. 
comida = comida + ['ensalada', 'manzana'] #Añadir una lista a otra lista, otra forma de hacerlo. 
comida.index('pizza') #Devuelve el indice de la primera aparición de un elemento de la lista, en este caso el índice 0.


# 6. Rangos númericos con la función range(x,y-1) El tipico for (i; i < x; i++) eso en python no existe.
for numero in list(range(1, 5)):
    print(numero)

numeros_pares = list(range(2, 11, 2))  # Lista de pares del 2 al 10

# 7. Funciones Built-in de python que se pueden aplicar sobre las listas
min(numeros_pares)  # Minimo de una lista
max(numeros_pares)  # Maximo de una lista
sum(numeros_pares)  # Suma los elementos de la lista
len(numeros_pares)  # Longitud de la lista
sorted(numeros_pares) # Si queremos ver una lista ordenada pero no ordenarla realmente. 

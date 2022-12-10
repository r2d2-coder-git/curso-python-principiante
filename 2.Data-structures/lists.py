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
motorcycles = ['honda', 'yamaha', 'suzuki','honda']

################### 2.INSERCIONES Y ACTUALIZACIONES #####################
# 1. Añade un elemento al final de la lista
motorcycles.append('ducati')
# 2. Añade un elemento en una posición de la lista, empezando por 0.
motorcycles.insert(0, 'daelim')
# 3. Actualizar una lista es muy fácil, sólo tienes que sobreescribir la posición. 
motorcycles[1] = 'bmw'

################### 3.BORRADOS #####################
# 1. Tambien podemos borrar un elemento especifico con pop y obtener el valor borrado.
element = motorcycles.pop(0)
# 2. Por defecto borrar el ultimo elemento de la lista.
last_element = motorcycles.pop()
# 3. Borrar un elemento de la lista, solo borra la primera apariencia del elemento indicado y no devuelve nada.
motorcycles.remove('yamaha')
# 4. Borrar un elemento de la lista.
while 'honda' in motorcycles:
    motorcycles.remove('honda')
# 5. Borra todos los elementos de una lista
motorcycles.clear()

################# 4.SORT ######################
# 1. Ordenar alfabeticamente
vocales = ['e','i','o','u','a']
vocales.sort()
vocales.sort(reverse=True)
# 2. Si queremos ver un lista ordenada pero no ordenarla realmente. 
sorted(vocales)
# 3. Darle la vuelta a una lista
vocales.reverse()
# 4. Le podemos asignar un criterio de ordenación.
def order_by_length(element):
  return len(element)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=order_by_length)

################# 5.OTROS MÉTODOS ######################
my_foods = ['pizza', 'tacos', 'kebab', 'pizza', 'hamburguesa', 'pizza', 'tacos']
# 1. IMPORTANT [:] Importante no asignar una lista a otra variable para copia la lista, 
# van a apuntar a la misma zona de memoria (friends_foods = my_foods no funciona)
copy_of_food = my_foods[:]
copy_of_food_version_two = my_foods.copy()
# 2. Contar el número de elementos de un valor específico.
pizza_number = my_foods.count('pizza')
# 3. Añadir una lista a otra lista. 
my_foods.extend(['ensalada', 'manzana'])
my_foods = my_foods + ['ensalada', 'manzana']
# 4. Devuelve el indice de la primera aparición de un elemento de la lista.
my_foods.index('pizza') #Devuelve 0


# 5. Rangos númericos con la función range(x,y-1) El tipico for (i; i < x; i++) eso en python no existe.
for value in list(range(1, 5)):
    print(value)

even_numbers = list(range(2, 11, 2))  # Lista de pares del 2 al 10

# 6. Funciones Built-in de python que se pueden aplicar sobre las listas
min(even_numbers)  # Minimo de una lista
max(even_numbers)  # Maximo de una lista
sum(even_numbers)  # Suma los elementos de la lista
len(even_numbers)  # Longitud de la lista


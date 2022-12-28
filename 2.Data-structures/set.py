#La estructura de datos utilizada en SET es Hashing, una técnica popular para realizar inserción, eliminación y recorrido en O(1) en promedio. 
#Las operaciones en Hash Table son algo similares a las de Linked List. Los sets en python son una lista desordenada con elementos duplicados eliminados.
#Un set es un mapa hash con linked list desordenadas. Por eso es mejor utilizar set que list cuando el orden de inserción y eliminación nos den igual.

#Enlace en la web: https://www.codesansar.com/python-programming/how-sets-are-internally-stored-python.htm

#Los sets establecidos no están ordenados, es decir, cuando se añade un elemento o se borra no se sabe en que posición del set va a caer.
#Los elementos de un set no se pueden modificar, es decir, no puedes sobreescribir una posición de un set, pero si puedes hacer inserciones y borrados en el set. 
#Los sets no permiten valores duplicados.


################### 1.CREACIÓN DE SETS #####################

# 1. set vacío
nuevo_set = set()
# 2. Inicializar un set con elementos
nuevo_set = {'uno','dos'}

################### 2.INSERTAR Y ACTUALIZAR #####################

nuevo_set.add('uno') #Añade un elemento, solo puedes pasar un elemento, no un set.
nuevo_set.update({'dos','tres'}) #Actualiza un set con otro set, añade los elementos que no están en el primer set.
copia_set = nuevo_set.copy() #Crea una copia del set.

################### 3.BORRADOS #####################

nuevo_set.discard('dos') #Borra el elemento, pero NO lanza un error si no existe
nuevo_set.remove('tres') #Borra el elemento, pero lanza un error si no existe
nuevo_set.clear() #Borra todos los elementos del set

################### 4.OPERACIONES DE SETS #####################

set_uno = {1,2,3,4}
set_dos = {4,5,6,7}
# ***Los siguientes métodos devuelven un conjunto nuevo, no modifican el conjunto. ***

set_diferencia = set_uno.difference(set_dos) #Devuelve un conjunto con los elementos que están en el set_uno y no en el set_dos, en este caso {1,2,3}
set_diferencia_simetrica = set_uno.symmetric_difference(set_dos) #Devuelve todos los elementos que están en el primer conjunto y en el segundo conjunto, excepto los que son comunes. 
                                                                 #En este caso {1,2,3,5,6,7}, el 4 es común, es como una antiintersección. 
                                                                 
set_interseccion = set_uno.intersection(set_dos) #Devuelve un conjunto con los elementos que están en ambos conjuntos, en este caso {4}
set_union = set_uno.union(set_dos) #Devuelve un conjunto con la del conjunto uno con el conjunto dos, en este caso {1,2,3,4,5,6,7}

# ***Los siguientes métodos modifican el conjunto sobre el que se aplica el método. ***

set_uno.difference_update(set_dos) #La variable set_uno contiene {1,2,3} ahora, es decir, la diferencia entre set_uno y set_dos. 
set_uno = {1,2,3,4} #Reestablecemos el conjunto con los valores iniciales.
set_uno.intersection_update(set_dos) #La variable set_uno contiene {4} ahora, es decir, la intersección entre set_uno y set_dos.
set_uno = {1,2,3,4} #Reestablecemos el conjunto con los valores iniciales.
set_uno.symmetric_difference_update(set_dos) #La variable set_uno contiene {1,2,3,5,6,7}, es decir, la diferencia simetrica entre set_uno y set_dos.


################### 5.OTROS METODOS #####################

no_tiene_interseccion = set_uno.isdisjoint(set_dos) #Devuelve true si NO tienen elementos compartidos, es decir, si la intersección es vacía. En este caso devuelve FALSE.
es_subconjunto = set_uno.issubset(set_dos) #Devuelve true si el primer conjunto es subconjunto del set dos. En este caso es FALSE.
es_superconjunto = set_uno.issuperset(set_dos) #Devuelve true si el segundo conjunto es subconjunto del set uno. En este caso es FALSE.
frozen_set = frozenset(set_uno) #Un frozenset es una versión inmutable de un set, es decir, a un set le podemos añadir y borrar elementos, estas operaciones desaparecen en un frozenset.
print(dir(frozen_set)) #Métodos disponibles: 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union'

################### 6.ACCESO A LOS SETS #####################

#No hay una forma de acceder de forma indexada
for element in set_uno:
    print(element)


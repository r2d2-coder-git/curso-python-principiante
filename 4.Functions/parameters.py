############################# PARAMETROS POR VALOR #####################################

# En Python los tipos de datos simples se pasan por valor: ENTEROS, FLOATS, STRINGS, BOOLEANOS, es decir, la variable que se pasa por parámetros 
# no se modifica, se hace una copia dentro de la función.

def comer_manzana_valor(numero_manzanas : int) -> None:
    numero_manzanas = numero_manzanas - 1

manzanas = 10
comer_manzana_valor(manzanas)
print(manzanas)

############################# PARAMETROS POR REFERENCIA #####################################

# En Python los tipos de datos compuestos se pasan por referencia: LISTAS, DICCIONARIOS, CONJUNTOS, es decir, si modificamos la colección pasada por
# parámetro la colección se verá afectada después de la ejecución de la función.

def comer_manzana_referencia(manzanas : list) -> None:
    manzanas[0] = manzanas[0] - 1

manzanas = [10] 
comer_manzana_referencia(manzanas)
print(manzanas)

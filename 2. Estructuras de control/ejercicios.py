################### EJERCICIOS DE CONDICIONALES #####################


################### EJERCICIO 1 #####################

# 1.Crea una variable "temp" con la temperatura actual en grados Celsius (por ejemplo: 25).
# 2.Crea una variable "viento" con la velocidad del viento en km/h (por ejemplo: 10).
# 3.Usando una estructura "if-elif-else", determina si el clima es agradable, fresco o frío:
# 4.Si la temperatura es mayor a 25 grados Celsius y la velocidad del viento es menor a 5 km/h, imprime "Clima agradable"
# 5.Si la temperatura está entre 20 y 25 grados Celsius o la velocidad del viento está entre 5 y 15 km/h, imprime "Clima fresco"
# 6.Si la temperatura es menor a 20 grados Celsius o la velocidad del viento es mayor a 15 km/h, imprime "Clima frío"

################### EJERCICIO 2 #####################

# 1.Crea una variable "edad" y asignale tu edad actual.
# 2.Crea una variable "tiene_permiso" y asignale "True" si tienes permiso para conducir, "False" en caso contrario.
# 3.Usando una estructura "if-elif-else", imprime un mensaje diferente dependiendo de si tienes permiso para conducir o no.
#   3.1.Si tienes permiso para conducir y tu edad es mayor o igual a 21, imprime "Puedes conducir y además eres mayor de edad."
#   3.2.Si tienes permiso para conducir pero tu edad es menor a 21, imprime "Puedes conducir pero aún eres menor de edad."
#   3.3.Si no tienes permiso para conducir, imprime "No tienes permiso para conducir."


################### EJERCICIOS DE BUCLES #####################

################### EJERCICIO 1 #####################

# 1.Crea una lista llamada "numeros" de numeros enteros con los numeros [3,1,5,7,9,22,0].
# 2.Crea una variable llamada "numero_min" e inicializala con el primer valor de la lista.
# 3.Crea una variable llamada "numero_max" e incializala con el primer valor de la lista.
# 4.Usando un bucle "for" recorre la lista de numeros.
# 5.Utiliza un condicional "if" dentro del bucle "for" para actualizar el valor de la variable "numero_min" si el valor actual es menor.
# 6.Utiliza un condicional "if" dentro del bucle "for" para actualizar el valor de la variable "numero_max" si el valor actual es mayor.
# 7.Imprime los valores de las variables "numero_min" y "numero_max" despues de terminar el bucle.

numeros = [3,1,5,7,9,22,0]
numero_min = numeros[0]
numero_max = numeros[0]
for numero in numeros:
    if numero < numero_min:
        numero_min = numero
    if numero > numero_max:
        numero_max = numero
        
print(numero_min)
print(numero_max)

################### EJERCICIO 2 #####################

# 1.Crea una lista llamada "precios" con los precios de varios productos (por ejemplo: 10, 15, 20, 25, 30).
# 2.Crea una variable "descuento" con un porcentaje de descuento (por ejemplo: 0.2 para un 20% de descuento).
# 3.Usando un bucle "for" y una estructura "if-elif-else", recorre la lista "precios" y aplica el descuento correspondiente a cada precio:
# 4.Si el precio es menor a 20, no se aplica descuento.
# 5.Si el precio está entre 20 y 30, se aplica un descuento del 10%.
# 6.Si el precio es mayor a 30, se aplica el descuento establecido en la variable "descuento".
# 7.Usando la función "enumerate()" imprime el índice y el precio con descuento de cada producto.

################### EJERCICIO 3 #####################

# 1.Crea una lista llamada "libros" con los títulos de los libros que has leído recientemente 
# (por ejemplo: "El señor de los anillos", "Harry Potter", "Cien años de soledad", "El gran Gatsby").
# 2.Usando un bucle "for" recorre la lista "libros" y con la función "print()" imprime cada título en una línea diferente.
# 3.Crea una variable "numero_de_libros" con un valor inicial de 0. 
# 4.Usando un bucle "for" cuenta la cantidad de libros en la lista "libros" y guarda el resultado en la variable "numero_de_libros".
# 5.Crea una variable "libro_mas_largo" con un valor inicial de "" (un string vacío).
# 6.Usando un bucle "for" recorre la lista "libros" y compara cada título con la variable "libro_mas_largo" y si el título es más largo que "libro_mas_largo" se guarda en esa variable.
# 7.Imprime el número de libros en la lista y el título del libro más largo que has leído.

################### EJERCICIO 4 #####################

# 1.Crea una lista llamada "numeros" con varios números enteros (por ejemplo: 4, 8, 15, 16, 23, 42).
# 2.Usando un bucle "for" recorre la lista "numeros" y usando la sentencia "if-elif-else" realiza las siguientes acciones:
# 3.Si el número es divisible entre 2 y 3, imprime "El número es divisible entre 2 y 3" y usa la sentencia "break" para salir del bucle.
# 4.Si el número es divisible entre 2, imprime "El número es divisible entre 2" y usa la sentencia "continue" para saltear a la siguiente iteración del bucle.
# 5.Si el número es divisible entre 3, imprime "El número es divisible entre 3"
# 6.Si ninguna de las condiciones anteriores se cumple, usa la sentencia "pass" para no hacer nada.

################### EJERCICIO 5 #####################

# 1.Crea una variable "dinero_inicial" con el dinero que tienes en tu billetera (por ejemplo: 50).
# 2.Crea una variable "compra" con el precio de un producto que deseas comprar (por ejemplo: 20).
# 3.Usando un bucle "while" realiza las siguientes acciones:
# 4.Si el dinero en tu billetera es suficiente para comprar el producto (dinero_inicial >= compra), resta el precio del producto al dinero inicial e imprime el mensaje
# "Producto comprado, dinero restante: " y el dinero restante en tu billetera.
# 5.Si el dinero en tu billetera no es suficiente para comprar el producto, imprime "No tienes suficiente dinero para comprar este producto" fuera del bucle.


dinero_inicial = 50
compra = 20
while dinero_inicial - compra > 0:
    print(f"Producto comprado, dinero restante: {dinero_inicial-compra}")
print("No tienes suficiente dinero para comprar este producto.")

################### EJERCICIO 6 #####################

# 1.Crea una lista llamada "nombres" con varios nombres (por ejemplo: Juan, Ana, Pedro, Maria, Sofia).
# 2.Crea una variable "amado_buscado" con un nombre de tu amado buscado (por ejemplo: Maria).
# 3.Crea una variable "encontrado" con valor inicial de "False".
# 4.Usando un bucle "while" y la función "enumerate()" recorre la lista "nombres" y realiza las siguientes acciones:
# 5.Si el nombres es igual a "nombre_buscado", cambia el valor de "encontrado" a "True" y mensaje "Nombre encontrado en la posicion: " y la posición del nombre.
# 6.Si "encontrado" sigue siendo "False" después de recorrer toda la lista "nombres", mensaje "Nombre no encontrado".
################### EJERCICIOS DE LISTAS #####################

################### EJERCICIO 1 #####################

# 1.Crea una lista llamada "compras" con los productos que necesitas comprar en un supermercado (por ejemplo: leche, pan, huevos, manzanas, queso, etc.).
# 2.Usando un bucle "for", imprime cada producto de la lista.
# 3.Usando la función "append()", agrega un producto nuevo a la lista (por ejemplo: cereales).
# 4.Usando la función "insert()", agrega un producto esencial al principio de la lista (por ejemplo: sal).
# 5.Usando la función "remove()", elimina un producto que ya no necesitas comprar de la lista (por ejemplo: queso).
# 6.Usando la función "pop()", elimina el último elemento de la lista y guarda su valor en una variable llamada "ultimo_producto".
# 7.Imprime la longitud de la lista usando "len()".
# 8.Usando un bucle "for", imprime cada producto de la lista en orden inverso.

################### EJERCICIO 2 #####################

# 1.Crea una lista llamada "empleados" que contenga 3 listas vacías. Cada lista vacía representa un departamento (por ejemplo, ventas, marketing, tecnología).
# 2.Usando un bucle "for", añade 3 nombres a cada una de las listas vacías dentro de "empleados". Cada nombre debe ser un string.
# 3.Crea una variable "total_empleados" e inicialízala en cero. Usando un bucle anidado (dentro de otro bucle), recorre cada nombre de cada lista dentro de "empleados" y 
# suma 1 a la variable "total_empleados".
# 4.Usando la función "append()", agrega un nuevo empleado en una lista específica (por ejemplo, en el departamento de tecnología).
# 5.Usando la función "remove()", elimina un empleado específico de una lista dentro de "empleados" (por ejemplo, el empleado "Juan" en el departamento de ventas).
# 6.Usando la función "pop()", elimina el último empleado de una lista dentro de "empleados" (por ejemplo, del departamento de marketing) y guarda su valor en una variable llamada "ultimo_empleado".
# 7.Imprime la longitud de "empleados" usando "len()" y la longitud de cada una de las listas dentro de "empleados" usando un bucle anidado.
# 8.Usando un bucle anidado, imprime el nombre de cada empleado en cada departamento.

################### EJERCICIO DE SETS #####################

# 1.Crea un set llamado "amigos_invitados" con los nombres de tus amigos a los que has invitado a una fiesta (por ejemplo: Juan, Pedro, Ana, Marta, Carlos).
# 2.Crea otro set llamado "amigos_confirmados" con los nombres de tus amigos que han confirmado asistencia a la fiesta (por ejemplo: Juan, Pedro, Ana).
# 3.Usando la función "add()", agrega un amigo adicional a "amigos_confirmados" (por ejemplo: Luis).
# 4.Usando la función "difference()" obtén los amigos que están en "amigos_invitados" pero no en "amigos_confirmados" y guarda el resultado en una variable "amigos_sin_confirmar".
# 5.Usando la función "intersection()" obtén los amigos que están en ambos sets y guarda el resultado en una variable "amigos_confirmados".
# 6.Usando la función "discard()" elimina un amigo específico de "amigos_invitados" (por ejemplo: Marta).
# 7.Usando la función "clear()" vacía el set "amigos_invitados".
# 8.Usando la función "len()" imprime la cantidad de elementos en "amigos_confirmados".

################### EJERCICIO DE TUPLAS #####################

# 1.Crea una tupla llamada "direccion" con tus datos de dirección (por ejemplo: calle, número, ciudad, código postal, país).
# 2.Usando la función "index()" imprime el índice de la ciudad en la tupla "direccion".
# 3.Usando acceso por intervalos, imprime solo el código postal y el país de tu dirección.
# 4.Crea una variable "nueva_direccion" igual a "direccion" y cambia el número de tu dirección en la variable "nueva_direccion".
# 5.Usando la función "count()" cuenta cuantas veces aparece la ciudad en la tupla "direccion".
# 6.Usando la función "len()" imprime la cantidad de elementos en "direccion".
# 7.Unir dos tuplas creando una tercera con el contenido de ambas.

################### EJERCICIOS DE DICCIONARIOS #####################

################### EJERCICIO 1 #####################

# 1.Crea un diccionario vacío llamado "agenda" que almacene los contactos de una persona.
# 2.Agrega algunos elementos al diccionario, como por ejemplo, "Juan": "555-555-5555", "Maria": "444-444-4444", "Pedro":"333-333-3333"
# 3.Usa el metodo "update()"" para agregar un nuevo contacto "Lucia":"222-222-2222"
# 4.Usa el metodo "pop()" para eliminar el contacto "Juan"
# 5.Usa el metodo "items()" para ver todos los contactos y sus numero de telefono
# 6.Usa el metodo "get()" para buscar un contacto específico "Lucia"


################### EJERCICIO 2 #####################

# 1.Crea un diccionario vacío llamado "estudiantes" que almacene información de los estudiantes de una clase.
# 2.Agrega algunos elementos al diccionario, como por ejemplo, "Juan": {"edad":22, "notas": [8, 9, 10, 8], "asistencia": {"Lunes": True, "Martes": True, "Miercoles": False, "Jueves": True, "Viernes": True}}, "Maria": {"edad":20, "notas": [6, 7, 8, 9], "asistencia": {"Lunes": True, "Martes": False, "Miercoles": True, "Jueves": False, "Viernes": True}}
# 3.Utiliza el método "update()"" para agregar un nuevo estudiante "Lucia":{"edad":21, "notas": [9, 8, 7, 6], "asistencia": {"Lunes": False, "Martes": True, "Miercoles": True, "Jueves": True, "Viernes": False}}
# 4.Utiliza el método "pop()" para eliminar el estudiante "Juan"
# 5.Utiliza un ciclo for para calcular el promedio de notas de cada estudiante y añadirlo al diccionario
# 6.Utiliza el método "get()"" para buscar la asistencia de un estudiante específico "Lucia"
# 7.Utiliza un ciclo for para contar el número de veces que un estudiante ha faltado a clase y añadirlo al diccionario.
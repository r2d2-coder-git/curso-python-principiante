



















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

compras = ['leche','pan','huevos','manzanas','queso']

for compra in compras:
    print(f'Producto: {compra}')

compras.append('cereales')
compras.insert(0,'sal')
compras.remove('queso')
ultimo_elemento = compras.pop()

print(f'La longitud de la lista es {len(compras)}.')

for compra in compras[::-1]:
    print(f"Producto en orden inverso: {compra}")


################### EJERCICIO 2 #####################

# 1.Crea una lista llamada "empleados" que contenga 3 listas con 4 nombres de persona cada una. Cada lista vacía representa un departamento (por ejemplo, ventas, marketing, tecnología).
# Ejemplo: [['Juan','Arturo','Maria','Arturo'],['Alberto','Pedro','Ana','Alberto'],['Andrea','Cristina','Pepe','Alvaro']]
# 2.Crea una variable "total_empleados_empresa" e inicialízala en cero. Usando un bucle anidado (dentro de otro bucle), recorre cada nombre de cada departamento dentro de "empleados" y 
# suma 1 a la variable "total_empleados".
# 3.Usando la función "append()", agrega un nuevo empleado en una lista específica (por ejemplo, en el departamento de tecnología).
# 4.Usando la función "remove()", elimina un empleado específico de una lista dentro de "empleados" (por ejemplo, el empleado "Juan" en el departamento de ventas).
# 5.Usando la función "pop()", elimina el último empleado de una lista dentro de "empleados" (por ejemplo, del departamento de marketing) y guarda su valor en una variable llamada "ultimo_empleado".
# 6.Imprime la longitud de "empleados" usando "len()" y la longitud de cada una de las listas dentro de "empleados" usando un bucle anidado sin utilizar "len()", debes utilizar una variable
#   auxiliar llamada "numero_empleados_departamento" inicializada a 0.
# 7.Usando un bucle anidado, imprime el nombre de cada empleado en cada departamento.

empleados = [['Juan','Arturo','Maria','Arturo'],['Alberto','Pedro','Ana','Alberto'],['Andrea','Cristina','Pepe','Alvaro']] #Ventas, marketing, tecnologia
total_empleados = 0

for departamento in empleados:
    for empleado in departamento:
        total_empleados = total_empleados + 1
        
print(total_empleados)

empleados[2].append('Amador')
empleados[0].remove('Juan')
ultimo_empleado_marketing = empleados[1].pop()

print(f"El numero total de departamentos son: {len(empleados)}")

numero_empleados_departamento = 0
for departamento in empleados:
    numero_empleados_departamento =0
    for empleado in departamento:
        numero_empleados_departamento = numero_empleados_departamento + 1
    print(f"El numero de empleados del departamento {empleados.index(departamento)} son {numero_empleados_departamento}")
    
        

    
################### EJERCICIO DE SETS #####################

# 1.Crea un set llamado "amigos_invitados" con los nombres de tus amigos a los que has invitado a una fiesta (por ejemplo: Juan, Pedro, Ana, Marta, Carlos).
# 2.Crea otro set llamado "amigos_confirmados" con los nombres de tus amigos que han confirmado asistencia a la fiesta (por ejemplo: Juan, Pedro, Ana).
# 3.Usando la función "add()", agrega un amigo adicional a "amigos_confirmados" (por ejemplo: Luis).
# 4.Usando la función "difference()" obtén los amigos que están en "amigos_invitados" pero no en "amigos_confirmados" y guarda el resultado en una variable "amigos_sin_confirmar".
# 5.Usando la función "intersection()" obtén los amigos que están en ambos sets y guarda el resultado en una variable "amigos_confirmados".
# 6.Usando la función "discard()" elimina un amigo específico de "amigos_invitados" (por ejemplo: Marta).
# 7.Usando la función "clear()" vacía el set "amigos_invitados".
# 8.Usando la función "len()" imprime la cantidad de elementos en "amigos_confirmados".

amigos_invitados = {'Juan', 'Pedro', 'Ana', 'Marta', 'Carlos'}
amigos_confirmados = {'Juan', 'Pedro', 'Ana'}

amigos_confirmados.add('Luis')

amigos_sin_confirmar = amigos_invitados.difference(amigos_confirmados)
amigos_confirmados = amigos_invitados.intersection(amigos_confirmados)
amigos_invitados.discard('Marta')
amigos_invitados.clear()

print(len(amigos_confirmados))


################### EJERCICIO DE TUPLAS #####################

# 1.Crea una tupla llamada "direccion" con tus datos de dirección (por ejemplo: calle, número, ciudad, código postal, país).
# 2.Usando la función "index()" imprime el índice de la ciudad en la tupla "direccion".
# 3.Usando acceso por intervalos, imprime solo el código postal y el país de tu dirección.
# 4.Crea una variable "nueva_direccion" igual a "direccion" y cambia el número de tu dirección en la variable "nueva_direccion", 
#   es necesario cambiar la tupla a lista para modificarla.
# 5.Usando la función "count()" cuenta cuantas veces aparece la ciudad en la tupla "direccion".
# 6.Usando la función "len()" imprime la cantidad de elementos en "direccion".
# 7.Unir dos tuplas creando una tercera con el contenido de ambas.

direccion = ('Calle Rosario', 10, 'Madrid', 20919, 'España')

print(direccion.index('Madrid'))
print(direccion[-2:])

nueva_direccion = list(direccion)
nueva_direccion[1] = 15
nueva_direccion = tuple(nueva_direccion)

print(direccion.count('Madrid'))
print(len(direccion))

union_direcciones = direccion + nueva_direccion

print(union_direcciones)

################### EJERCICIOS DE DICCIONARIOS #####################

################### EJERCICIO 1 #####################

# 1.Crea un diccionario vacío llamado "agenda" que almacene los contactos de una persona.
# 2.Agrega algunos elementos al diccionario, como por ejemplo, "Juan": "555-555-5555", "Maria": "444-444-4444", "Pedro":"333-333-3333"
# 3.Usa el metodo "update()"" para agregar un nuevo contacto "Lucia":"222-222-2222"
# 4.Usa el metodo "pop()" para eliminar el contacto "Juan"
# 5.Usa el metodo "items()" para ver todos los contactos y sus numero de telefono
# 6.Usa el metodo "get()" para buscar un contacto específico "Lucia"

agenda = {"Juan": "555-555-5555", "Maria": "444-444-4444", "Pedro":"333-333-3333"}
agenda.update({"Lucia":"222-222-2222"})
agenda.pop("Juan")
for nombre, telefono in agenda.items():
    print(f"{nombre} tiene el telefono {telefono}.")
telefono_lucia = agenda.get("Lucia")

################### EJERCICIO 2 #####################

# 1.Crea un diccionario vacío llamado "estudiantes" que almacene información de los estudiantes de una clase.
# 2.Agrega algunos elementos al diccionario, como por ejemplo, 
# "Juan": {"edad":22, "notas": [8, 9, 10, 8], "asistencia": {"Lunes": True, "Martes": True, "Miercoles": False, "Jueves": True, "Viernes": True}}, 
# "Maria": {"edad":20, "notas": [6, 7, 8, 9], "asistencia": {"Lunes": True, "Martes": False, "Miercoles": True, "Jueves": False, "Viernes": True}}
# 3.Utiliza el método "update()"" para agregar un nuevo estudiante 
# "Lucia":{"edad":21, "notas": [9, 8, 7, 6], "asistencia": {"Lunes": False, "Martes": True, "Miercoles": True, "Jueves": True, "Viernes": False}}
# 4.Utiliza un ciclo for para calcular el promedio de notas de cada estudiante y añadelo al diccionario de informacion del estudiante.
# 5.Utiliza el método "get()"" para buscar la asistencia de un estudiante específico "Lucia"
# 6.Utiliza un ciclo for para contar el número de veces que un estudiante ha faltado a clase y añadirlo al diccionario.
# 7.Utiliza el método "pop()" para eliminar el estudiante "Juan"

estudiantes = {"Juan": {"edad":22, "notas": [8, 9, 10, 8], "asistencia": {"Lunes": True, "Martes": True, "Miercoles": False, "Jueves": True, "Viernes": True}}, 
               "Maria": {"edad":20, "notas": [6, 7, 8, 9], "asistencia": {"Lunes": True, "Martes": False, "Miercoles": True, "Jueves": False, "Viernes": True}}}

estudiantes.update({"Lucia":{"edad":21, "notas": [9, 8, 7, 6], "asistencia": {"Lunes": False, "Martes": True, "Miercoles": True, "Jueves": True, "Viernes": False}}})

for nombre, informacion in estudiantes.items():
    notas = informacion['notas']
    suma_notas = 0
    for nota in notas:
        suma_notas = suma_notas + nota
    promedio = suma_notas / len(notas)
    informacion.update({"Promedio": promedio})

for nombre, informacion in estudiantes.items():
    asistencia = informacion['asistencia']
    numero_falta_asistencia = 0
    for dia, valor_asistencia in asistencia.items():
        if valor_asistencia == False:
            numero_falta_asistencia = numero_falta_asistencia + 1
    informacion.update({'Dias_fallados':numero_falta_asistencia})
    
print(estudiantes)
estudiantes.pop("Juan")
        
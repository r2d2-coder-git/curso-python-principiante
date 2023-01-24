################### EJERCICIOS DE FUNCIONES #####################

################### EJERCICIO 1 #####################

# 1.Crea una función llamada "calcular_impuestos" que reciba dos argumentos: "ingresos" y "tasa_impuestos" (por ejemplo: calcular_impuestos(50000, 0.25))
# 2.Dentro de la función, calcula el impuesto debido multiplicando los ingresos por la tasa de impuestos y guarda el resultado en una variable "impuesto_debido".
# 3.Retorna el valor de "impuesto_debido".
# 4.Crea una variable "ingresos" con el valor de tus ingresos anuales (por ejemplo: 75000)
# 5.Crea una variable "tasa_impuestos" con el porcentaje de impuestos que debes pagar (por ejemplo: 0.3)
# 6.Crea una variable "impuesto_a_pagar" que sea igual a la función "calcular_impuestos" con los argumentos "ingresos" y "tasa_impuestos".
# 7.Imprime "Impuesto a pagar: " y el valor de "impuesto_a_pagar".

################### EJERCICIO 2 #####################

# 1.Crea una función llamada "calcular_promedio" que reciba una lista de números como argumento.
# 2.Dentro de la función, calcula el promedio de los números en la lista y guarda el resultado en una variable "promedio".
# 3.Retorna el valor de "promedio".
# 4.Crea una lista de números con las calificaciones obtenidas en un curso (por ejemplo: [9, 8, 10, 7, 8, 9, 6, 8, 10, 9])
# 5.Llama a la función "calcular_promedio" con la lista de calificaciones como argumento y guarda el resultado en una variable "promedio_curso"
# 6.Imprime "El promedio del curso es: " y el valor de "promedio_curso"

################### EJERCICIO 3 #####################

# 1.Crea una función llamada "calcular_costo_envio" que reciba dos argumentos: "origen" y "destino" (por ejemplo: calcular_costo_envio("Nueva York", "Los Ángeles"))
# 2.Dentro de la función, crea un diccionario con los costos de envio entre diferentes ciudades (por ejemplo: {"Nueva York": {"Los Ángeles": 20, "Chicago": 10, "Miami": 15}, "Los Ángeles": {"Nueva York": 25, "Chicago": 17, "Miami": 20}, ...})
# 3.Usa los argumentos "origen" y "destino" para obtener el costo de envio entre esas dos ciudades del diccionario y guarda el resultado en una variable "costo"
# 4.Retorna el valor de "costo"
# 5.Crea una variable "origen" con el lugar de origen del envio (por ejemplo: "Nueva York")
# 6.Crea una variable "destino" con el lugar de destino del envio (por ejemplo: "Los Ángeles")
# 7.Llama a la función "calcular_costo_envio" con las variables "origen" y "destino" como argumentos y guarda el resultado en una variable "costo_envio"
# 8.Imprime "El costo de envio desde " + origen + " hasta " + destino + " es de: " + costo_envio

################### EJERCICIO 4 #####################

# 1.Crea una función llamada "verificar_stock" que reciba un argumento: "productos" (por ejemplo: verificar_stock(productos))
# 2.Dentro de la función, crea una lista vacia llamada "productos_agotados" para almacenar los productos que ya no tienen stock
# 3.Usa un bucle "for" para recorrer la lista "productos" y verificar el stock de cada producto
# 4.Si el stock es 0, agrega el producto a la lista "productos_agotados"
# 5.Retorna la lista "productos_agotados"
# 6.Crea una lista de diccionarios con información de los productos (nombre, precio, stock) (por ejemplo: 
# [{"nombre": "Laptop", "precio": 800, "stock": 10},    {"nombre": "Teclado", "precio": 30, "stock": 20},    {"nombre": "Mouse", "precio": 15, "stock": 50},    
# {"nombre": "Monitor", "precio": 200, "stock": 5},    {"nombre": "Impresora", "precio": 80, "stock": 0},    {"nombre": "Parlantes", "precio": 40, "stock": 15},    
# {"nombre": "Cargador", "precio": 20, "stock": 0},    {"nombre": "Audifonos", "precio": 25, "stock": 30},    
# {"nombre": "Memoria USB", "precio": 10, "stock": 100},    {"nombre": "Disco duro externo", "precio": 75, "stock": 20}])
# 7.Llama a la función "verificar_stock" con la variable "productos" como argumentos y guarda el resultado en una variable "productos_agotados"
# 8.Imprime "Los productos agotados son: " y el valor de "productos_agotados"

################### EJERCICIO 5 #####################

# 1.Crea una función llamada "analizar_datos" que reciba un argumento "pacientes", que es una lista de diccionarios con información de pacientes (nombre, edad, sexo, enfermedad).
# 2.Dentro de la función, crea variables vacías para almacenar información estadística, como "pacientes_masculinos", "pacientes_femeninos", "pacientes_mayores", "pacientes_menores", "pacientes_enfermos" y "pacientes_sanos".
# 3.Usando un bucle "for" recorre la lista "pacientes" y analiza cada paciente:
#   3.1.Si el paciente es masculino, aumenta en 1 la variable "pacientes_masculinos"
#   3.2.Si el paciente es femenino, aumenta en 1 la variable "pacientes_femeninos"
#   3.3.Si el paciente tiene más de 18 años, aumenta en 1 la variable "pacientes_mayores"
#   3.4.Si el paciente tiene menos de 18 años, aumenta en 1 la variable "pacientes_menores"
#   3.5.Si el paciente tiene una enfermedad, aumenta en 1 la variable "pacientes_enfermos"
#   3.6.Si el paciente no tiene una enfermedad, aumenta en 1 la variable "pacientes_sanos"
# 4.Crea una variable "pacientes" con la lista de diccionarios con información de los pacientes (por ejemplo: 
# [{{ "nombre": "Pedro", "edad": 45, "sexo": "masculino", "enfermedad": "hipertensión" }
#   { "nombre": "Ana", "edad": 35, "sexo": "femenino", "enfermedad": "artritis" }
#   { "nombre": "Juan", "edad": 25, "sexo": "masculino", "enfermedad": None }
#   { "nombre": "Sofia", "edad": 40, "sexo": "femenino", "enfermedad": "migraña" }
#   { "nombre": "Carlos", "edad": 55, "sexo": "masculino", "enfermedad": "colesterol alto" }
#   { "nombre": "Isabel", "edad": 30, "sexo": "femenino", "enfermedad": "asma" }]).
# 5.Llama a la función "analizar_datos" con la variable "pacientes" como argumento.
# 6.Dentro de la función "analizar_datos", imprime las estadísticas obtenidas, como "Pacientes masculinos: ", "Pacientes femeninos: ", "Pacientes mayores de 18 años: ", 
# "Pacientes menores de 18 años: ", "Pacientes enfermos: " y "Pacientes sanos: ".
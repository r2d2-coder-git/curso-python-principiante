################### EJERCICIOS DE MODULOS #####################

################### EJERCICIO 1 #####################

# 1.Crea un archivo llamado "matematicas.py" y define una función llamada "calcular_promedio" que reciba una lista de números como argumento y retorne el promedio de los números en la lista.
# 2.Crea otro archivo llamado "estadisticas.py" y importa el módulo "matematicas" con la sentencia "import matematicas"
# 3.Crea una función en el archivo "estadisticas.py" llamada "estadisticas_basicas" que reciba una lista de números como argumento. Dentro de esta función, utiliza la función "calcular_promedio" del módulo "matematicas" para calcular el promedio de los números en la lista.
# 4.Crea un archivo llamado "main.py" e importa el módulo "estadisticas" con la sentencia "import estadisticas"
# 5.Crea una lista de números en el archivo "main.py" y llama a la función "estadisticas_basicas" del módulo "estadisticas" pasando la lista como argumento.
# 6.Imprime el resultado retornado por la función "estadisticas_basicas".

################### EJERCICIO 2 #####################

# 1.Crea un archivo llamado "utilidades.py" y define una función llamada "mayusculas" que reciba una cadena de texto como argumento y retorne la cadena convertida en mayúsculas. 
# 2.También define una función llamada "minusculas" que reciba una cadena de texto como argumento y retorne la cadena convertida en minúsculas.
# 3.Crea otro archivo llamado "texto.py" e importa el módulo "utilidades" con la sentencia "import utilidades"
# 4.Crea una función en el archivo "texto.py" llamada "formatear_texto" que reciba una cadena de texto y un formato como argumentos ('mayusculas' o 'minusculas'). 
# Dentro de esta función, utiliza las funciones "mayusculas" o "minusculas" del módulo "utilidades" dependiendo del formato especificado para convertir la cadena de texto en el formato especificado.
# 5.Crea un archivo llamado "main.py" e importa el módulo "texto" con la sentencia "import texto"
# 6.En el archivo "main.py" llama a la función "formatear_texto" del módulo "texto" pasando una cadena de texto y un formato como argumentos.

################### EJERCICIO 3 #####################

# 1.Crea un archivo llamado "validaciones.py" y define una función llamada "validar_email" que reciba una cadena de texto como argumento y retorne verdadero 
#   si es una dirección de correo electrónico válida o falso en caso contrario, un correo es válido: 
#   si empieza por algo distinto al '@' y termina en '@gmail.com'.
# 2.Crea otro archivo llamado "registro.py" e importa el módulo "validaciones" con la sentencia "import validaciones"
# 3.Crea una función en el archivo "registro.py" llamada "registrar_usuario" que reciba un nombre y un correo electrónico como argumentos. 
#   3.1.Dentro de esta función, utiliza la función "validar_email" del módulo "validaciones" para verificar si el correo electrónico es válido. 
#   3.2.Si es válido, imprime "El usuario [nombre] ha sido registrado con el correo [correo electrónico]", de lo contrario imprime "El correo electrónico no es válido".
# 4.Crea un archivo llamado "main.py" e importa el módulo "registro" con la sentencia "import registro"
# 5.En el archivo "main.py" llama a la función "registrar_usuario" del módulo "registro" pasando un nombre y un correo electrónico como argumentos.
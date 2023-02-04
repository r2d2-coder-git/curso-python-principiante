# En Python, un string es una secuencia de caracteres. Pueden ser números, letras, símbolos, y cualquier otro carácter que puedas imaginar. 
# Se representan con comillas simples ('') o comillas dobles ("").

# Los strings se utilizan para representar texto o información alfanumérica en un programa. Pueden ser manipulados y concatenados 
# con otros strings y números utilizando operadores matemáticos y especiales de concatenación.



################### FUNCIONES MÁS UTILIZADAS #####################

# len(string): Devuelve la longitud de un string.

# str.strip(): Devuelve un string sin espacios en blanco al principio o al final.

# str.replace(old, new): Reemplaza una parte de un string con otra.

# str.lower(): Convierte todos los caracteres de un string a minúsculas.

# str.upper(): Convierte todos los caracteres de un string a mayúsculas.

# str.title(): Convierte el primer carácter de cada palabra en un string a mayúsculas.



# 1. Longitud de un string

saludo = "Hola me llamo Arturo"

longitud_string1 = len(saludo)
print(longitud_string1)

# 2. Quitar espacios en blanco de al principio y final de un string

string_espacios = "                     Esto es un string con espacios feos                   "
print(string_espacios)

string_sin_espacio = string_espacios.strip()
print(string_sin_espacio)

# 3. Reemplazar partes de un string por otro.

mensaje_cifrado = "PEESTOPEESPEUNPEMENSAJEPECIFRADOPE"
mensaje_sin_cifrar= mensaje_cifrado.replace('PE',' ')

print(mensaje_sin_cifrar)

# 4. Poner un string en minusculas o mayusculas

minuscula = 'vamos a gritar un poco'
grito = minuscula.upper()
print(grito)

mayusculas = 'HABLEMOS MAS BAJITO'
susurro = mayusculas.lower()
print(susurro)





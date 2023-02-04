
################### EJERCICIOS DE MANEJO DE FICHEROS #####################

################### EJERCICIO 1 #####################

# Crea un script que lea el archivo "contar_palabras.txt" de la carpeta "ficheros" y cuente la cantidad de palabras en él. 
# Puedes utilizar el método split() para separar las palabras en una lista y luego utilizar la función len() para contar el número de elementos en la lista.

nombre_fichero = '7.Ficheros y excepciones/ejercicios/ejercicios_ficheros/ficheros/contar_palabras.txt'

with open(nombre_fichero) as fichero_abierto:
    contenido = fichero_abierto.read()
    contenido_parseado = contenido.replace('\n',' ')
    palabras = contenido_parseado.split(' ')
    cantidad_palabras = len(palabras)
    print(cantidad_palabras)
    
################### EJERCICIO 2 #####################

# Crea un script que lea el archivo de texto "palabras_repetidas.txt de la carpeta "ficheros" y cuenta la cantidad de veces que aparece una palabra específica en él. 
# Puedes utilizar el método count() para contar la cantidad de veces que aparece una palabra en una cadena de texto, imprimer el número.
# Reemplaza esta palabra repetida con el método "replace" y vuelve a escribir el texto en otro fichero llamado "palabras_sin_repetir.txt" .

fichero_fuente = '7.Ficheros y excepciones/ejercicios/ejercicios_ficheros/ficheros/palabras_repetidas.txt'
fichero_destino = '7.Ficheros y excepciones/ejercicios/ejercicios_ficheros/ficheros/palabras_sin_repetir.txt'

with open(fichero_fuente,'r') as fichero_abierto:
    contenido = fichero_abierto.read()
    contenido_parseado = contenido.replace('\n',' ')
    palabras = contenido_parseado.split(' ')
    cantidad_palabras_repetidas = palabras.count('palabras')
    print(f"La palabras 'palabras' se repite {cantidad_palabras_repetidas} veces.")
    contenido_sin_palabra_repetida = contenido.replace('palabras', '')
    
with open(fichero_destino,'w') as fichero_abierto:
    fichero_abierto.write(contenido_sin_palabra_repetida)

     
################### EJERCICIO 3 #####################

# Crea un script que tome una lista de números y los escriba en un archivo de texto llamado "numeros.txt", uno por línea. 
# Luego, crea otro script que lea ese archivo y sume los números e imprima el resultado por pantalla.
# Puedes utilizar el método write() para escribir en un archivo y el método read() para leer su contenido.

numeros = [1,2,3,4,5,6,7,8,9,10]
nombre_fichero = '7.Ficheros y excepciones/ejercicios/ejercicios_ficheros/ficheros/numeros.txt'

with open(nombre_fichero,'w') as fichero_abierto:
    for numero in numeros:
        if numero != numeros[-1]:
            fichero_abierto.write(str(numero) + '\n')
        else:
            fichero_abierto.write(str(numero))
        
with open(nombre_fichero,'r') as fichero_abierto:
    contenido = fichero_abierto.read()
    numeros_str = contenido.split('\n')
    suma_numeros = 0
    for numero in numeros_str:
        suma_numeros = suma_numeros + int(numero)
    print(suma_numeros)

################### EJERCICIO EXTRA 1 #####################

# Crea un script que tome coja las imagenes de la carpeta "imagenes" y los copie en otra carpeta con el nombre "imagenes_procesadas". 
# Puedes utilizar el módulo "os" para crear la carpeta "imagenes_procesadas" con la función "os.makedirs(ruta)"
# Utiliza el módulo "os" también para listar las imagénes de la carpeta "imagenes" con la función "os.listdir(ruta)"
# Utiliza el módulo "shutil" para copiar cada imagen a la nueva carpeta "imagenes_procesadas" con la función "shutil.copy(ruta_origen,ruta_destino)"

carpeta_fuente = '7.Ficheros y excepciones/ejercicios/ejercicios_ficheros/imagenes/'
carpeta_destino = '7.Ficheros y excepciones/ejercicios/ejercicios_ficheros/imagenes_procesadas/'

import shutil
import os

os.makedirs(carpeta_destino,exist_ok=True)
imagenes = os.listdir(carpeta_fuente)
for imagen in imagenes:
    ruta_origen = carpeta_fuente + imagen
    ruta_destino = carpeta_destino + imagen
    shutil.copy(ruta_origen, ruta_destino)

################### EJERCICIO EXTRA 2 #####################

# Crea un script que lea el archivo "presupuestos.csv" CSV (comma-separated values) y lo almacene en una lista de diccionarios con el método "DictReader" de la librería "csv", 
# donde cada diccionario representa una fila del archivo y las claves son los nombres de las columnas.
import csv

nombre_fichero = '7.Ficheros y excepciones/ejercicios/ejercicios_ficheros/ficheros/vacunaciones.csv'

with open(nombre_fichero, 'r') as file:
  lector_filas = csv.DictReader(file)
  diccionario_filas = list(lector_filas)
  print(diccionario_filas[0])


# La palabra clave WITH cierra el archivo una vez que ya no se necesita acceder a él observa que en este programa llamamos a open() pero no a close(). Se podría abrir
# archivo y cerrar el archivo llamando a open() y close(), pero si un error en su programa impide que se ejecute la sentencia close(), puede que el archivo nunca
# cierre. Esto puede parecer trivial, pero los archivos mal cerrados pueden causar que los datos se pierdan o se corrompan. Y si llama a close() demasiado pronto en su programa,
# te encontrarás intentando trabajar con un archivo cerrado (un archivo al que no puedes acceder), lo que conduce a más errores. No siempre es fácil saber exactamente cuándo se debe 
# cerrar un archivo. Pero con la estructura que se muestra aquí, Python lo averiguará por ti.Todo lo que tienes que hacer es abrir el archivo y trabajar con él como desees,
# confiando en que Python lo cerrará automáticamente cuando sea el momento adecuado.

nombre_fichero = './7.Ficheros y excepciones/pi_digits.txt'
############################# LEER EL FICHERO COMPLETO EN UNA VARIABLE #####################################

with open(nombre_fichero) as fichero_abierto:
    contenido = fichero_abierto.read()
    print(contenido)
    
############################# LEER EL FICHERO LINEA A LINEA #####################################

with open(nombre_fichero) as fichero_abierto:
    for linea in fichero_abierto:
        print(linea)
        
############################# LEER EL FICHERO LINEA A LINEA #####################################
with open(nombre_fichero) as fichero_abierto:
    lineas = fichero_abierto.readlines()


############################# ESCRIBIR CONTENIDO EN EL FICHERO #####################################
nombre_fichero = './7.Ficheros y excepciones/programacion.txt'
with open(nombre_fichero, 'w') as fichero_abierto: #open has options: 'r' (read mode) 'w' (write mode) 'a' (append mode)
    fichero_abierto.write("Me encanta programar.")
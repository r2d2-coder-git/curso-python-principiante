# La palabra clave WITH cierra el archivo una vez que ya no se necesita acceder a él observa que en este programa llamamos a open() pero no a close(). Se podría abrir
# archivo y cerrar el archivo llamando a open() y close(), pero si un error en su programa impide que se ejecute la sentencia close(), puede que el archivo nunca
# cierre. Esto puede parecer trivial, pero los archivos mal cerrados pueden causar que los datos se pierdan o se corrompan. Y si llama a close() demasiado pronto en su programa,
# te encontrarás intentando trabajar con un archivo cerrado (un archivo al que no puedes acceder), lo que conduce a más errores. No siempre es fácil saber exactamente cuándo se debe 
# cerrar un archivo. Pero con la estructura que se muestra aquí, Python lo averiguará por ti.Todo lo que tienes que hacer es abrir el archivo y trabajar con él como desees,
# confiando en que Python lo cerrará automáticamente cuando sea el momento adecuado.

filename = './pi_digits.txt'
############################# LEER EL FICHERO COMPLETO EN UNA VARIABLE #####################################

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)
    
############################# LEER EL FICHERO LINEA A LINEA #####################################

with open(filename) as file_object:
    for line in file_object:
        print(line)
        
############################# LEER EL FICHERO LINEA A LINEA #####################################
with open(filename) as file_object:
    lines = file_object.readlines()


############################# ESCRIBIR CONTENIDO EN EL FICHERO #####################################
filename = 'programming.txt'
with open(filename, 'w') as file_object: #open has options: 'r' (read mode) 'w' (write mode) 'a' (append mode)
    file_object.write("I love programming.")
############################# BUCLES FOR IN #####################################
#Sintaxis:
#For elemento in elementos:
#   Acciones

iterador = list(range(0,11)) #Lista de 0-10
suma = 0
for i in iterador:
    suma = suma + i

lista_palabras = ['r2d2.coder','instagram','tiktok']
for palabra in lista_palabras:
    print(palabra)

############################# BUCLES WHILE #####################################
#Sintaxis:
#While condicion:
#   Acciones

while suma > 0:
    suma = suma - 1

############################# SENTENCIAS BREAK, PASS Y CONTINUE #####################################

#Break: Detiene la ejecución del bucle.
while True:
    break

#Pass: Se utiliza para dejar vacío un trozo de código que todavía no queremos especificar.
for i in iterador:
    pass

#Continue: Pasa a la siguiente iteración del bucle.
for i in iterador: 
    if i % 2 == 0:
        continue
    print(i)
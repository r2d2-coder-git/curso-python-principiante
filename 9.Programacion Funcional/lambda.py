# El paradigma funcional es popular porque ofrece varias ventajas sobre otros paradigmas de programación. El código funcional es:

# De alto nivel: Describe el resultado deseado en lugar de especificar explícitamente los pasos necesarios para conseguirlo. Las sentencias
# simples tienden a ser concisas, pero tienen mucha fuerza.

# Transparente: el comportamiento de una función pura depende únicamente de sus entradas y salidas, sin valores intermedios.
# Esto elimina la posibilidad de efectos secundarios, lo que facilita la depuración.

# Paralelizable: Las rutinas que no provocan efectos secundarios pueden ejecutarse más fácilmente en paralelo.


############################## FUNCIONES ANONIMAS #####################################

# Muchas veces necesitamos una funcionalidad en código que no tiene porque estar ligada a un nombre, por eso las funciones anonimas son muy útiles,
# especialmente en programación funcional.


reversa = lambda lista: lista[::-1]
numeros = [1,2,3,4]

numeros_reversa = reversa(numeros)

print(numeros_reversa)
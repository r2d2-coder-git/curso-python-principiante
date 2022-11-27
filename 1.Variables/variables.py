#TIPOS DE DATOS BÁSICOS (Hacer una diapositiva)
#Como bien sabemos una variable es un espacio asignado en memoria RAM y que ocupa un tamaño dependiendo de su tipo de datos, los tipos de datos básicos que implementa python por defecto son los siguientes.

#Números (Entero, float, complejo)
contador : int = 0
numero_pi : float = 3.14
imaginario : complex = -5j
#Booleanos
es_verdad : bool = True
es_mentira : bool = False
#String
mi_nombre : str = 'r2d2.coder'

#OPERADORES (Hacer una diapositiva)
#Un operador es un signo que utilizamos para señalar que operacion realizamos entre dos o más operandos, por ejemplo el operador de suma, el de resta, multiplicación y otros más específicos de la programación

#ARITMÉTICA (Devuelven un dato de tipo Número (Entero,float,complejo))
suma = 1 + 1 
resta = 1 - 1 
multiplicacion = 10 * 10 
division_con_decimales = 18 / 5 #Resultado = 3.6
division_sin_decimales = 18 // 5 #Resultado = 3
modulo = 11 / 10 
potencia = 2 ** 3 
#OPERADORES RELACIONALES (Devuelven un dato de tipo booleano)
mayor_que = 2 > 1
menor_que = 1 < 2
igual_que = 1 == 1
mayor_o_igual_que = 2 >= 1
menor_o_igual_que = 1 <= 2
distinto_que = 2 != 1

#(CURIOSIDADES) OPERADORES BIT A BIT (Se usa 2 = 10 y 3 = 11 en binario para hacer las operaciones de ejemplo. )
and_bit_a_bit = 2 & 3 # 10 & 11 = 10 (2)  se hace and bit a bit el (1&1 = 1) y (0&1= 0)
or_bit_a_bit = 2 | 3 # 10 | 11 = 11 (3)
xor_bit_a_bit = 2 ^ 3 # 10 ^ 11 = 01 (1)
not_bit_a_bit  = ~2 # ~1~0 = 01 (1)


#Estructuras de datos básicas
mi_lista : list = ['Hola', 'Mundo']
mi_tupla : tuple = ('Hola', 'Mundo')
mi_conjunto : set = {1,2,3}
mi_diccionario : dict = {'nombre' : 'r2d2', 'apellido': 'coder'}


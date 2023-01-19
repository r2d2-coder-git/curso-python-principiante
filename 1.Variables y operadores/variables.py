################### TIPOS DE DATOS BASICOS #####################

# Una variable es un espacio asignado en memoria RAM y que ocupa un tamaño dependiendo de su tipo de datos,
# los tipos de datos básicos que implementa Python por defecto son los siguientes.

#Números (Entero, float, complejo)
contador: int = 0
numero_pi: float = 3.14
imaginario: complex = -5j
# Booleanos
es_verdad: bool = True
es_mentira: bool = False
# String
mi_nombre: str = 'r2d2.coder'

################### OPERADORES #####################

# Un operador es un signo que utilizamos para señalar que operacion realizamos entre dos o más operandos, por ejemplo el operador de suma, el de resta, multiplicación y otros más específicos de la programación

################### OPERADORES ARITMETICOS #####################

suma = 1 + 1
resta = 1 - 1
multiplicacion = 10 * 10
division_con_decimales = 18 / 5  # Resultado = 3.6
division_sin_decimales = 18 // 5  # Resultado = 3
modulo = 11 / 10
potencia = 2 ** 3

################### OPERADORES RELACIONALES #####################

mayor_que = 2 > 1
menor_que = 1 < 2
igual_que = 1 == 1
mayor_o_igual_que = 2 >= 1
menor_o_igual_que = 1 <= 2
distinto_que = 2 != 1

################### OPERADORES LOGICOS #####################

and_operation = True and False  # False
or_operation = True or False  # True
not_operation = not False  # True

################### OPERADORES DE PERTENENCIA #####################

# (Devuelve un valor booleano) Estos operadores aplican a las secuencias. (Strings, listas y tuplas)
in_operation = "hola" in "hola mundo"  # True
not_in_operation = "hola" not in "hola mundo"  # False

################### OPERADORES DE IDENTIDAD #####################

# (Devuelve valor booleano) Sirve para comprobar si dos variables emplean la misma ubicación en memoria.
x = 1
y = x
is_operation = x is y  # True
is_not_operation = x is not y  # False

################### OPERADORES DE BIT A BIT #####################

# (Se usa 2 = 10 y 3 = 11 en binario para hacer las operaciones de ejemplo. )
# 10 & 11 = 10 (2)  se hace and bit a bit el (1&1 = 1) y (0&1= 0)
and_bit_a_bit = 2 & 3
or_bit_a_bit = 2 | 3  # 10 | 11 = 11 (3)
xor_bit_a_bit = 2 ^ 3  # 10 ^ 11 = 01 (1)
not_bit_a_bit = ~2  # ~10 = Complemento a 2 negación.
right_shift_bit_a_bit = 2 >> 3 # Se desplazan 3 bits a la derecha el 10 = 000 (0)
left_shift_bit_a_bit = 2 << 3 # 0000010 << 00000011 = 0010000 (16) se le meten 3 bits a la derecha del 10

# Estructuras de datos básicas
mi_lista: list = ['Hola', 'Mundo']
mi_tupla: tuple = ('Hola', 'Mundo')
mi_conjunto: set = {1, 2, 3}
mi_diccionario: dict = {'nombre': 'r2d2', 'apellido': 'coder'}

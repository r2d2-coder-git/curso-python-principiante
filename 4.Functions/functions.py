# Sintaxis: def nombre_funcion(parametro1 : Tipo1, parametro2: Tipo2) -> TipoDatoRetorno:
#               Acciones
#               return Valor (Opcional)

############################# FUNCIÓN SIN PARÁMETROS #####################################

def funcion_basica() -> None:
    print("Uso de función básica")


funcion_basica()

############################# FUNCIÓN CON PARÁMETROS #####################################

# Python es un lenguaje con tipado dinámico, es decir, no hace falta indicar que tipo de datos va a recibir o devolver una función ya que Python
# va a inferir los tipo de datos en tiempo de ejecución. Es muy recomendable indicar los tipos de datos para aumentar la legibilidad del código.
# Es más, aunque tu le indiques el tipo de parámetros y luego le pasas otro tipo de datos NO va a dar un fallo.


def suma(numero1: int, numero2: int) -> int:
    resultado = numero1 + numero2
    return resultado


suma_resultado = suma(15, 24)

############################# FUNCIÓN CON PARÁMETROS CON VALORES POR DEFECTO #####################################


def sacar_dinero(cuenta_bancaria: int, dinero_a_retirar: int = 50) -> int:
    return cuenta_bancaria - dinero_a_retirar


cuenta_bancaria = 5000
cuenta_bancaria = sacar_dinero(cuenta_bancaria)
cuenta_bancaria = sacar_dinero(cuenta_bancaria, 1000)
print(cuenta_bancaria)


############################# FUNCIÓN CON PARÁMETROS OPCIONALES #####################################

# En los parametros opcionales no hace falta definir que tipo de datos tienen porque internamente python los va a meter en tuplas. Los toppings que
# le pasemos en la función van a ser metidos en una tupla internamente.

def crear_pizza(tipo_pizza: str, *toppings_extra) -> str:
    tipos_pizza = ['margarita', 'cuatro quesos', 'barbacoa']
    frase_respuesta = ''

    if tipo_pizza in tipos_pizza and not toppings_extra:
        frase_respuesta = f'Tu pizza {tipo_pizza} se está procesando vuelve en 10 minutos.'
    elif tipo_pizza in tipos_pizza and toppings_extra:
        frase_respuesta = f'Tu pizza {tipo_pizza} con los toppings {str(toppings_extra)} se está procesando vuelve en 10 minutos.'
    else:
        frase_respuesta = f'El tipo de pizza {tipo_pizza} no lo hacemos en este restaurante.'

    return frase_respuesta


respuesta1 = crear_pizza('margarita')
# Salchicha y pimiento rojo son parámetros opcionales.
respuesta2 = crear_pizza('margarita', 'salchicha', 'pimiento rojo')


############################# FUNCIÓN CON PARÁMETROS KEY-VALUE #####################################

# Sirve para cuando necesitamos un número variable de parámetros que tengan forma de diccionario, el nombre kwargs se pone por convención del lenguaje.
# En este caso queremos crear un perfil de usuario que tenga como obligatorio poner el nombre y apellidos y la demás información de forma opcional.

def crear_perfil_usuario(nombre: str, apellidos: str, **kwargs) -> str:
    perfil = f'********INFORMACIÓN DEL USUARIO {nombre} {apellidos}*************'
    for key, value in kwargs.items():
        perfil = f'{perfil}\n{key} : {value}'
    return perfil


perfil = crear_perfil_usuario('Arturo', 'Lorenzo')
perfil_kwargs = crear_perfil_usuario(
    'Arturo', 'Lorenzo', Ciudad='Murcia', Pais='España', Comida_favorita='Pizza')

print(perfil_kwargs)

############################# FUNCIÓNES QUE TIENEN COMO PARÁMETROS FUNCIONES #####################################

# Todo en Python son objetos hasta las funciones por eso podemos pasar una función como parámetro a otra función.
# En este ejemplo hacemos una función que reciba que tipo de operación tiene que hacer sobre dos números, está operación se define como una función.


def sumar(x, y):
    return x + y


def calculadora(operacion, x, y):
    return operacion(x, y)


resultado = calculadora(sumar, 4, 6)
print(resultado)


############################# ORDEN DE PARÁMETROS #####################################

# Orden de posicionamiento de los parámetros según el tipo:
# 1. Parametros obligatorios
# 2. Parametros opcionales
# 3. Parametros key-value.
#        def funcion(parametros_obligatorios, *parametros_opcionales, **kwargs_arguments)

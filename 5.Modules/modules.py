############################# FUNCIÓN CON PARÁMETROS CON VALORES POR DEFECTO #####################################

def sacar_dinero(cuenta_bancaria:int, dinero_a_retirar:int = 50) -> int:
    return cuenta_bancaria - dinero_a_retirar


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
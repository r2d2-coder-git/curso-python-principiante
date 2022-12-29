 #Order of parameters def function(positional_arguments, *optional_arguments, **kwargs_arguments)
#Sintaxis: def nombre_funcion(parametro1 : Tipo1, parametro2: Tipo2) -> TipoDatoRetorno:
#               Acciones
#               return Valor (Opcional)

############################# FUNCIÓN SIN PARÁMETROS #####################################

def funcion_basica() -> None:
    print("Uso de función básica")

funcion_basica()

############################# FUNCIÓN CON PARÁMETROS #####################################

#Python es un lenguaje con tipado dinámico, es decir, no hace falta indicar que tipo de datos va a recibir o devolver una función ya que Python 
#va a inferir los tipo de datos en tiempo de ejecución. Es muy recomendable indicar los tipos de datos para aumentar la legibilidad del código.
#Es más, aunque tu le indiques el tipo de parámetros y luego le pasas otro tipo de datos NO va a dar un fallo.

def suma(numero1 : int, numero2: int) -> int:
    resultado = numero1 + numero2
    return resultado

suma_resultado = suma(15,24)

############################# FUNCIÓN CON PARÁMETROS OPCIONALES #####################################

#Los argumentos opcionales no hace falta definir que tipo de datos tienen porque internamente python los va a meter en tuplas. Los toppings que
#le pasemos en la función van a ser metidos en una tupla internamente.

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
respuesta2 = crear_pizza('margarita', 'salchicha', 'pimiento rojo') #Salchicha y pimiento rojo son parámetros opcionales.

    

############################# FUNCIÓN CON PARÁMETROS OPCIONALES Y KEY-VALUE #####################################


'''
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#Important of positional arguments
describe_pet('hamster', 'harry')
#With keywords in the parameters you can skip the order of arguments.
describe_pet(pet_name='harry', animal_type='hamster')

#Function with parameter with default value "animal_type = 'dog'"
def describe_pet2(pet_name, animal_type='dog'): 
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet2(pet_name='willie')

#Function with list 
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] #Always has to be passed as a copy if we want to add this in other lists
completed_models = []
print_models(unprinted_designs[:], completed_models[:]) # IMPORTANT: Argument with COPY of LIST completed_models
print(completed_models)
print_models(unprinted_designs[:], completed_models) #Append all elements of the list completed_models
print(completed_models)
show_completed_models(completed_models)


#Functions with optional arguments (Optional arguments are empties tuples filled in the moment of calling the function)
#Optional arguments has to be always the last parameters if there arent **kwargs.
def make_pizza(size, *toppings):
    print(type(toppings))
    for topping in toppings:
        print(topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Functions with arbitrary keyword arguments using **. Python internally generates a empty dictionary and fill it with the key-value arguments.
def build_profile(first, last, **user_info,):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        return profile

user_profile = build_profile('albert', 'einstein',
 location='princeton', #Key-value parameter 1
 field='physics') #Key-value parameter 2
print(user_profile)

'''
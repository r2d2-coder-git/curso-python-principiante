#Los diccionarios son colecciones iterables, ordenadas y mutables de elementos compuestos 
#por una clave (que identifica de modo único al elemento) y el valor que se desea almacenar. 
#No pueden aparecer elementos con claves repetidas.

#Un diccionario se utiliza cuando se quieren asociar conceptos y definiciones.

#URL: https://www2.eii.uva.es/fund_inf/python/notebooks/11_Diccionarios_conjuntos/Diccionarios_conjuntos.html

import copy #Modulo para hacer copias profundas de diccionarios.

################### 1.CREACIÓN Y ACCESO DE DICCIONARIOS #####################

# Diccionario vacío inicializado con dict()
diccionario = dict()
# Diccionario vacío inicializado con llaves
diccionario = {}
# Diccionario definido con tuplas 
diccionario = dict([("clave1", "valor1"), ("clave2", "valor2")])
# Creación de un diccionario con valores constantes
diccionario = dict.fromkeys(['Uno', 'Dos', 'Tres'], 'ValorFijo')
# Diccionario inicializado con valores
tecnologias = {'Web': ['Javascript', 'Html', 'CSS'], 'Videojuegos' : ['Unity', 'C#']}


################### 2.INSERCION Y ACTUALIZACION EN DICCIONARIOS #####################

tecnologias['Data engineer'] = ['Python', 'Hadoop'] #Inserta un nuevo elemento de tecnologías para 'Data engineer' como clave y lista como valor.
tecnologias.update({'Desarrollo Movil': ['Android', 'IOS']}) #Inserta un nuevo elemento con el método update, si el elemento ya existe lo actualiza.
tecnologias['Web'].append('Angular') #Actualiza la lista de tecnologías Web, al ser una lista mutable podemos directamente añadir un elemento.
tecnologias['Web'] = [] #Actualiza un elemento del diccionario con una asignación.
tecnologias.update({'Web': ['NodeJS']}) #Actualiza un elemento con el método update, se sustituye la lista.


################### 3.BORRADOS DE ELEMENTOS EN DICCIONARIOS #####################

valor_borrado = tecnologias.pop('Data engineer') #Borra un elemento señalando la clave y devuelve el valor, si no existe la clave salta un error.
mensaje_error = tecnologias.pop('IA','No existe el elemento la clave IA') #Borra un elemento y devuelve el valor, si no existe la clave devuelve el mensaje por default.
ultimo_elemento = tecnologias.popitem() #Borra el último elemento del diccionario y lo devuelve en forma de tupla.
tecnologias.clear() #Borra todos los elementos del diccionario.

################### 4.OTROS MÉTODOS #####################

tecnologias = {'Web': ['Javascript', 'Html', 'CSS'], 'Videojuegos' : ['Unity', 'C#']}
copia_superficial = tecnologias.copy() #Copia superficial de un diccionario, esto quiere decir que si un diccionario contiene listas,
                                # y modificas la lista en la copia también se modifica la lista en el diccionario original.
copia_superficial['Web'].append('NodeJS') #Modificamos la lista de Web y se cambian las lista del diccionario de copia y el original.
copia_profunda = copy.deepcopy(tecnologias) #Copia profunda de un diccionario.    
copia_profunda['Web'].append('Angular') #Angular solo se va a añadir al diccionario de copia profunda.
numero_elementos = len(tecnologias) #Devuelve la longitud del diccionario, es decir, la cantidad de elementos que tiene.

################### 5.ACCESO A ELEMENTOS EN DICCIONARIOS #####################

# ***La diferencia entre get y setdefault es que get no modifica el diccionario y setdefault si añade el elemento si no existe.***
tecnologias_web = tecnologias.get('Web','No existe la clave Web') #Devuelve el valor asociado a una clave, si no existe la clave devuelve valor por default.
tecnologias_sistemas = tecnologias.setdefault('Sistemas', 'C++') #Devuelve el valor asociado a la clave Sistemas, si no existe añade el elemento {'Sistemas':'C++'} y devuelve C++.
tecnologias_items = tecnologias.items() #Devuelve un objeto dict_items que contien una lista de tuplas, una tupla por cada clave-valor. Tupla (key, value)
tecnologia_keys = tecnologias.keys() #Devuelve un objeto dict_keys que contiene una lista con las claves del diccionario.

for key, value in tecnologias.items(): #Recorrido de un diccionario.
    print(f"La clave {key} está asociado al valor {value}")



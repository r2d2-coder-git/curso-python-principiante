############################# IMPORTAR MODULOS COMPLETOS #####################################

# 1.Importar todas las funciones de un módulo con *.
from modules import * 
crear_pizza('margarita','pepperoni')

# 2.Importar todo el módulo.
import modules
modules.crear_pizza('margarita', 'pepperoni')

# 3.Importar todo el módulo con un alias.
import modules as m 
m.crear_pizza('margarita', 'pepperoni')

############################# IMPORTAR PARTES CONCRETAS DE UN MODULO #####################################

# 1.Importar varias funciones de un módulo.
from modules import crear_pizza, sacar_dinero
crear_pizza('margarita', 'pepperoni')

# 2.Importar funciones con alias.
from modules import crear_pizza as mp, sacar_dinero as sd
mp('margarita', 'pepperoni')


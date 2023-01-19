############################# SINTAXIS #####################################

#CONDICION SIMPLE

#if condition1:
#   accion1
#elif condition2:
#   accion2
#else:
#   accion3

#CONDICION ANIDADA

#if condition1:
#   if condition2:
#       action1
#   elif condition3:
#       action2
#   else: 
#       action3
#elif condition4:
#   action4

############################# CONDICIONAL BOOLEANO #####################################
valor_booleano = True
if valor_booleano: #Esto es lo mismo que poner valor_booleano == True
    print("El valor booleano es True")

############################# CONDICIONAL BOOLEANO CON ELSE ##################################### 

if valor_booleano: 
    print("El valor booleano es True") 
else:
    print("El valor booleano es False")

############################# CONDICIONAL NUMÉRICO #####################################

edad = 18 
if edad > 18 and edad < 80: #Podemos aplicar condiciones compuestas con operadores: and, or, not.
    print("Enhorabuena puedes conducir un coche!")
else:
    print("Todavía estás chiquito, vuelve en unos años.")

############################# CONDICIONAL NUMÉRICON CON ELIF #####################################

dinero = 5
if dinero > 1000:
    print("Eres rico!")
elif dinero > 500:
    print("Tienes dinerillo")
elif dinero > 100:
    print("Hay que seguir estudiando programación")
else:
    print("Estamos pobres...")

############################# CONDICIONALES CON STRINGS #####################################

nombre = 'r2d2.coder'
# 1.Comparar valor de strings.

if nombre == 'r2d2.coder':
    print("Eres el auténtico!")
else:
    print("Eres un farsante!")

# 2.Comprobar si un string es vacío.
if nombre:
    print('Tenemos nombre')
else:
    print('Cadena vacía')

############################# CONDICIONALES CON LISTAS #####################################

lista = ['r2d2.coder']
# 1. Comprobar si un elemento está en una lista.
if 'r2d2.coder' in lista:
    print('Tenemos a r2d2 en la lista!')
else: 
    print('No tenemos a r2d2 en la lista...')

# 2. Comprobar si una lista está vacía.
if lista:
    print(lista[0])
else:
    print('Lista vacía')

############################# CONDICIONALES INLINE #####################################

# Es mucho más legible que poner if elif else asignando tres veces un valor a una variable.
# Sintaxis: Action1 if condition1 else Action2 if condition2 else Action3

dinero = 5
estatus_economico = 'Clase alta' if dinero > 1000 else 'Clase Media' if dinero > 500 else 'Clase baja'
print(estatus_economico)
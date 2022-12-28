##### SINTAXIS APLICADA A CONDICIONALES #####

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

#Los condicionales en Python además de comprobar si la condición es verdadera o falsa cuando se utiliza el símbolo ==, tambíen puede decir si una condición 
#es falsa o verdadera según si la variable a comprobar tiene elementos o no. Por ejemplo, comprobar si una lista es vacía, un string es vacío...

#Condicional booleano
valor_booleano = True
if valor_booleano: #Esto es lo mismo que poner valor_booleano == True
    print("El valor booleano es True")

#Condicional booleano con else 
if valor_booleano: 
    print("El valor booleano es True") 
else:
    print("El valor booleano es False")

#Condicional númerico
edad = 18 
if edad > 18:
    print("Enhorabuena puedes conducir un coche!")
else:
    print("Todavía estás chiquito, vuelve en unos años.")

#Condicional númerico con más de una condición
dinero = 5
if dinero > 1000:
    print("Eres rico!")
elif dinero > 500:
    print("Tienes dinerillo")
elif dinero > 100:
    print("Hay que seguir estudiando programación")
else:
    print("Estamos pobres...")

#Condicional comprobando si dos strings son iguales.
nombre = 'r2d2.coder'

if nombre == 'r2d2.coder':
    print("Eres el auténtico!")
else:
    print("Eres un farsante!")

#Condicional comprobando si el string está vacío
if nombre:
    print('Tenemos nombre')
else:
    print('Cadena vacía')

#Condicional para comprobar si lista vacia
lista = ['r2d2.coder']
if lista:
    print(lista[0])
else:
    print('Lista vacía')

#Condicional inline, es mucho más legible que poner if elif else asignando tres veces un valor a una variable.
#Sintaxis: Action1 if condition1 else Action2 if condition2 else Action3

dinero = 5
estatus_economico = 'Clase alta' if dinero > 1000 else 'Clase Media' if dinero > 500 else 'Clase baja'
print(estatus_economico)
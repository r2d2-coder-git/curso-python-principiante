############################# FUNCIÓNES ANIDADAS #####################################

# Una función interna es simplemente una función que se define dentro de otra función. La función interna puede acceder a las variables que se han
# definido dentro del alcance de la función externa, pero no puede cambiarlas.

# Hay varias razones por las que es posible que necesitemos crear una función interna:

# 1. Si queremos que la función anidada solo sea utilizada en el contexto de la función que la contiene, entonces podemos usarla para encapsular
# una parte del código y hacerlo más legible.

# 2. Las funciones anidadas también pueden ser útiles para compartir una parte del código entre varias funciones. En este caso,
# podemos definir la función anidada una vez y luego usarla desde varias funciones.

# 3. Las funciones anidadas también pueden ser útiles para crear funciones "auxiliares" que solo necesiten ser utilizadas en el contexto de otra
# función. En este caso, podemos definir la función anidada justo donde la necesitemos y luego usarla para realizar una tarea específica dentro
# de la función que la contiene.


def funcion1():
    print("Hola desde la función de fuera")

    def funcion2():
        print("Hola desde la función de dentro")
    funcion2()


funcion1()


def fuera(x):
    def dentro(y, z):
        return x + y + z
    return dentro


add_five = fuera(5)
result = add_five(5, 5)

############################# DECORADORES SIN PARAMETROS #####################################


def funcion_decoradora(func):

    def funcion_interna():
        print("Soy una funcion interna y te han decorado")
        func()
    return funcion_interna


@funcion_decoradora
def funcion_normal():
    print("Soy una función normal")


# La segunda ejecución haría exactamente lo mismo si funcion_normal no estuviese decorada
funcion_normal()
funcion_decorada = funcion_decoradora(funcion_normal)

############################# DECORADORES CON PARAMETROS #####################################


def dividir_inteligente(func):
    def funcion_interna(a, b):
        print("Voy a dividir ", a, " y ", b)
        if b == 0:
            print("Ooops! No está permitido dividir por cero!")
            return

        return func(a, b)
    return funcion_interna


@dividir_inteligente
def dividir(a, b):
    print(a/b)


dividir(2, 5)

dividir(2, 0)

############################# ENCADENAMIENTO DE DECORADORES #####################################


def estrella(func):
    def funcion_interna(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return funcion_interna


def porcentaje(func):
    def funcion_interna(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)

    return funcion_interna

# 1. Opcion con decoradores


@estrella
@porcentaje
def printer(msg):
    print(msg)


printer("Hello")

# 2. Opcion sin decoradores


def printer(msg):
    print(msg)


printer = estrella(porcentaje(printer))

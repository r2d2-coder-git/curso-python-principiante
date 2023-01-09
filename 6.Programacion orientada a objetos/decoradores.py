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


def make_pretty(func):
    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function


def ordinary():
    print("I am ordinary")


# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()


def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()

############################# DECORADORES CON PARAMETROS #####################################


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


divide(2, 5)

divide(2, 0)

############################# ENCADENAMIENTO DE DECORADORES #####################################


def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner

# 1. Opcion con decoradores


@star
@percent
def printer(msg):
    print(msg)

# 2. Opcion sin decoradores
#


def printer(msg):
    print(msg)


printer = star(percent(printer))

printer("Hello")

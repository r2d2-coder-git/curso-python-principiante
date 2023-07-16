################### EJERCICIOS DE EXCEPCIONES #####################

################### EJERCICIO 1 #####################

# Crea un script que lea un archivo de texto y cuente la cantidad de palabras en él. Utiliza un bloque try-except para manejar el caso en el que el 
# archivo especificado no existe o no se tiene acceso. En caso de que ocurra una excepción, el script debe imprimir un mensaje informando al usuario que el archivo no pudo ser abierto.

fichero = ''
try:
    with open(fichero) as file:
        contenido = file.read()
        palabras = contenido.split()
        cantidad_palabras = len(palabras)
        print(cantidad_palabras)
except FileNotFoundError:
    print("El archivo no existe.")

################### EJERCICIO 2 #####################

# Crea un script que solicite al usuario que ingrese un número y luego imprima el resultado de dividir 10 por ese número. Utiliza un bloque try-except para manejar el caso 
# en el que el usuario ingresa un cero o un valor no numérico. En caso de que ocurra una excepción, el script debe imprimir un mensaje informando al usuario que el valor ingresado no es válido.

try:
    numero = float(input("Ingrese un número: "))
    resultado = 10 / numero
    print(f"El resultado de dividir 10 por {numero} es: {resultado}")
except ValueError:
    print("El valor ingresado no es válido. Debe ser un número.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")

################### EJERCICIO 3 #####################

# Crea una clase "CuentaBancaria" que represente una cuenta bancaria con un saldo y un límite de extracción. Agrega un método "extraer" que permita al usuario retirar dinero de la cuenta. 
# Si el usuario intenta extraer más dinero del que tiene disponible en la cuenta (incluyendo el límite de extracción), lanza una excepción "SaldoInsuficiente" con un mensaje que 
# indique al usuario que no tiene suficientes fondos para realizar la transacción.

class SaldoInsuficiente(Exception):
    pass

class CuentaBancaria:
    def __init__(self, saldo, limite_extraccion):
        self.saldo = saldo
        self.limite_extraccion = limite_extraccion

    def extraer(self, cantidad):
        if cantidad > self.saldo or cantidad > self.limite_extraccion:
            raise SaldoInsuficiente("No tiene suficientes fondos para realizar la transacción.")
        self.saldo -= cantidad
        print(f"Se extrajeron {cantidad} unidades. Saldo restante: {self.saldo}")

# Ejemplo de uso
cuenta = CuentaBancaria(1000, 500)  # Saldo inicial de 1000 y límite de extracción de 500
try:
    cantidad_a_extraer = float(input("Ingrese la cantidad a extraer: "))
    cuenta.extraer(cantidad_a_extraer)
except ValueError:
    print("Ingrese un valor numérico válido.")
except SaldoInsuficiente as e:
    print(e)


################### EJERCICIO 4 #####################

# Crea una función "validar_edad" que reciba una edad y valide que sea un número entero y mayor a 0. Si no cumple con estas condiciones, 
# lanza una excepción "EdadInvalida" con un mensaje que indique al usuario que la edad ingresada no es válida. Utiliza esta función en otra función "registro" que 
# reciba un nombre y una edad y valide que la edad ingresada sea válida antes de registrar al usuario.

class EdadInvalida(Exception):
    pass

def validar_edad(edad):
    if not isinstance(edad, int) or edad <= 0:
        raise EdadInvalida("La edad ingresada no es válida.")

def registro(nombre, edad):
    try:
        validar_edad(edad)
        print(f"Usuario registrado: Nombre: {nombre}, Edad: {edad}")
    except EdadInvalida as e:
        print(e)

# Ejemplo de uso
nombre = input("Ingrese el nombre: ")
try:
    edad = int(input("Ingrese la edad: "))
    registro(nombre, edad)
except ValueError:
    print("La edad debe ser un número entero.")

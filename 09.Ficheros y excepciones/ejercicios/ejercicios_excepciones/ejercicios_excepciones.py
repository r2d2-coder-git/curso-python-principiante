################### EJERCICIOS DE EXCEPCIONES #####################

################### EJERCICIO 1 #####################

# Crea un script que lea un archivo de texto y cuente la cantidad de palabras en él. Utiliza un bloque try-except para manejar el caso en el que el 
# archivo especificado no existe o no se tiene acceso. En caso de que ocurra una excepción, el script debe imprimir un mensaje informando al usuario que el archivo no pudo ser abierto.

################### EJERCICIO 2 #####################

# Crea un script que solicite al usuario que ingrese un número y luego imprima el resultado de dividir 10 por ese número. Utiliza un bloque try-except para manejar el caso 
# en el que el usuario ingresa un cero o un valor no numérico. En caso de que ocurra una excepción, el script debe imprimir un mensaje informando al usuario que el valor ingresado no es válido.

################### EJERCICIO 3 #####################

# Crea una clase "CuentaBancaria" que represente una cuenta bancaria con un saldo y un límite de extracción. Agrega un método "extraer" que permita al usuario retirar dinero de la cuenta. 
# Si el usuario intenta extraer más dinero del que tiene disponible en la cuenta (incluyendo el límite de extracción), lanza una excepción "SaldoInsuficiente" con un mensaje que 
# indique al usuario que no tiene suficientes fondos para realizar la transacción.

################### EJERCICIO 4 #####################

# Crea una función "validar_edad" que reciba una edad y valide que sea un número entero y mayor a 0. Si no cumple con estas condiciones, 
# lanza una excepción "EdadInvalida" con un mensaje que indique al usuario que la edad ingresada no es válida. Utiliza esta función en otra función "registro" que 
# reciba un nombre y una edad y valide que la edad ingresada sea válida antes de registrar al usuario.

################### EJERCICIO 5 #####################

# Crea una clase "Automovil" que tenga como atributos la marca, modelo, año y velocidad actual. Agrega un método "acelerar" que permita al usuario aumentar la velocidad actual del automovil 
# en una cierta cantidad especificada. Si el usuario intenta acelerar más de lo permitido (por ejemplo, un límite de velocidad de 150km/h), 
# lanza una excepción "VelocidadExcedida" con un mensaje que indique al usuario que ha excedido el límite de velocidad permitido.

################### EJERCICIO 6 #####################

# Crea una clase "SistemaDeInventario" que represente un sistema de inventario para una tienda. Agrega un método "vender" que permita al usuario vender un cierto producto especificando 
# la cantidad. Si el usuario intenta vender una cantidad mayor a la que se tiene en el inventario, lanza una excepción "InventarioInsuficiente" con un mensaje que indique al usuario que no 
# hay suficiente inventario para vender esa cantidad. Además, agrega un método de clase "registrar_compra" que permita al usuario registrar una compra de inventario y si el usuario 
# intenta registrar una compra negativa, lanza una excepción "CompraInvalida" con un mensaje que indique al usuario que la compra registrada es inválida.
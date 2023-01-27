################### EJERCICIOS DE CLASES Y OBJETOS #####################

################### EJERCICIO 1 #####################

# 1.Crea un archivo llamado "vehiculo.py" y define una clase llamada "Vehiculo" con atributos como "marca", "modelo", "año" y "color". También define un método llamado "encender" que 
#   imprima "El vehículo ha sido encendido." y otro método llamado "apagar" que imprima "El vehículo ha sido apagado.".
# 2.Crea otro archivo llamado "concesionaria.py" e importa la clase "Vehiculo" del archivo "vehiculo.py" con la sentencia "from vehiculo import Vehiculo"
# 3.Crea una clase en el archivo "concesionaria.py" llamada "Concesionaria" con un atributo "inventario" que sea una lista vacía. También define un método "agregar_vehiculo" que reciba un objeto "Vehiculo" como argumento y lo agregue al inventario de la concesionaria. Otro método es "listar_vehiculos" que imprima los detalles de cada vehículo en el inventario de la concesionaria.
# 4.Crea un archivo llamado "main.py" e importa la clase "Concesionaria" del archivo "concesionaria.py" con la sentencia "from concesionaria import Concesionaria"
# 5.En el archivo "main.py" crea un objeto "concesionaria" de la clase "Concesionaria"

################### EJERCICIO 2 #####################

# 1.Crea un archivo llamado "persona.py" y define una clase llamada "Persona" con atributos como "nombre", "apellido" y "edad". 
#   También define un método llamado "saludar" que imprima "Hola, mi nombre es [nombre] [apellido] y tengo [edad] años".
# 2.Crea otro archivo llamado "familia.py" e importa la clase "Persona" del archivo "persona.py" con la sentencia "from persona import Persona".
# 3.Crea una clase en el archivo "familia.py" llamada "Familia" con un atributo "miembros" que sea una lista vacía. 
#   También define un método "agregar_miembro" que reciba un objeto "Persona" como argumento y lo agregue a la lista de miembros de la familia. 
#   Otro método es "listar_miembros" que imprima los detalles de cada miembro de la familia.
# 4.Crea un archivo llamado "main.py" e importa la clase "Familia" del archivo "familia.py" con la sentencia "from familia import Familia"
# 5.En el archivo "main.py" crea un objeto "familia" de la clase "Familia" y agrega varios objetos "Persona" a la lista de miembros de la familia utilizando el método "agregar_miembro".

################### EJERCICIO 3 #####################

# 1.Crea un archivo llamado "cuenta_bancaria.py" y define una clase llamada "CuentaBancaria" con atributos como "nombre_titular", "numero_cuenta" y "saldo". 
# 2.También define un método llamado "depositar" que reciba una cantidad como argumento y sume esa cantidad al saldo de la cuenta. También define un método llamado "retirar" 
#   que reciba una cantidad como argumento y reste esa cantidad al saldo de la cuenta. Si no hay suficiente saldo, el método debe imprimir un mensaje de error.
# 3.Crea otro archivo llamado "banco.py" e importa la clase "CuentaBancaria" del archivo "cuenta_bancaria.py" con la sentencia "from cuenta_bancaria import CuentaBancaria"
# 4.Crea una clase en el archivo "banco.py" llamada "Banco" con un atributo "cuentas" que sea un diccionario vacío. También define un método "crear_cuenta" que reciba un objeto 
#   "CuentaBancaria" como argumento y lo agregue al diccionario de cuentas del banco con el número de cuenta como clave. Otro método es "realizar_transaccion" que reciba el número de cuenta, 
#   el tipo de transacción (depósito o retiro) y la cantidad, y llame al método correspondiente en la cuenta especificada.
# 5.Crea un archivo llamado "main.py" e importa la clase "Banco" del archivo "banco.py" con la sentencia "from banco import Banco"
# 6.En el archivo "main.py" crea un objeto "banco" de la clase "Banco" y crea varias cuentas "CuentaBancaria" utilizando el método "crear_cuenta" del banco. Luego, realiza varias 
#   transacciones en las cuentas utilizando el método "realizar_transaccion" del banco.

################### EJERCICIO 4 #####################

# 1.Crea un archivo llamado "sistema_de_gestion.py" y define una clase llamada "Empleado" con atributos como "nombre", "apellido", "edad", "cargo" y "salario". 
# 2.También define un método llamado "aumentar_salario" que reciba un porcentaje como argumento y aumente el salario del empleado en ese porcentaje.
# 3.Crea otra clase llamada "Departamento" con atributos como "nombre" y "empleados" que es una lista vacía. 
# 4.También define un método "agregar_empleado" que reciba un objeto "Empleado" como argumento y lo agregue a la lista de empleados del departamento. 
#     Otro método es "listar_empleados" que imprima los detalles de cada empleado en el departamento.
# 5.Crea otra clase llamada "Empresa" con atributos como "nombre" y "departamentos" que es un diccionario vacío. 
# 6.También define un método "agregar_departamento" que reciba un objeto "Departamento" como argumento y lo agregue al diccionario de departamentos de la empresa con el nombre del 
#     departamento como clave. Otro método es "listar_departamentos" que imprima los detalles de cada departamento en la empresa.
# 7.Crea un archivo llamado "main.py" e importa las clases "Empleado", "Departamento" y "Empresa" del archivo "sistema_de_gestion.py"
# 8.En el archivo "main.py" crea un objeto "empresa" de la clase "Empresa" y agrega varios objetos "Departamento" a la empresa utilizando el método "agregar_departamento". 
# 9.Luego, agrega varios objetos "Empleado" a cada departamento utilizando el método "agregar_empleado" del departamento.

################### EJERCICIO 5 #####################

# 1.Crea un archivo llamado "sistema_de_inventario.py" y define una clase llamada "Producto" con atributos como "nombre", "cantidad" y "precio". 
# 2.También define un método llamado "vender" que reciba una cantidad como argumento y reste esa cantidad al atributo "cantidad" del producto. 
# 3.También define un método llamado "comprar" que reciba una cantidad como argumento y sume esa cantidad al atributo "cantidad" del producto.
# 4.Crea otra clase llamada "Inventario" con atributos como "productos" que es una lista vacía y "total_ventas" que es un número. 
# 5.También define un método "agregar_producto" que reciba un objeto "Producto" como argumento y lo agregue a la lista de productos del inventario. 
#     Otro método es "vender_producto" que reciba el nombre del producto y una cantidad, busque el producto correspondiente en la lista de productos y llame al método "vender" en ese producto. 
#     Ademas, suma el precio total de la venta al atributo "total_ventas" del inventario.
# 6.Crea otro método en la clase Inventario llamado "comprar_producto" que reciba el nombre del producto y una cantidad, busque el producto correspondiente en la lista de productos y 
#     llame al método "comprar" en ese producto.
# 7.Crea un archivo llamado "main.py" e importa la clase "Inventario" del archivo "sistema_de_inventario.py"
# 8.En el archivo "main.py" crea un objeto "inventario" de la clase "Inventario" y agrega varios objetos "Producto" al inventario utilizando el método "agregar_producto". 
# 9.Luego, realiza varias ventas y compras de productos utilizando los métodos "vender_producto" y "comprar_producto" del inventario.
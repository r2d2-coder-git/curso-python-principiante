################### EJERCICIOS DE PYTESTS #####################

import unittest

################### EJERCICIO 1 #####################

# 1.Crea una función "es_primo(n)" que reciba un número entero y devuelva un valor booleano indicando si el número es primo o no. 
# 2.Crea un test utilizando pytest para comprobar que la función funciona correctamente para distintos casos, como números primos y no primos, números negativos, y números mayores a 1.

def es_primo(n:int) -> bool:
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

class PrimoTestCase(unittest.TestCase):
    def test_es_primo(self):
        primo = es_primo(5)
        no_primo = es_primo(10)
        self.assertTrue(primo)
        self.assertFalse(no_primo)


    
################### EJERCICIO 2 #####################

# 1.Crea una función "area_triangulo(base, altura)" que reciba dos números y devuelva el área de un rectángulo (Formula = (base*altura)/2). 
# 2.Crea un test utilizando pytest para comprobar que la función funciona correctamente para distintos casos, como valores de base y altura negativos, valores de base y altura cero, 
# y valores de base y altura positivos.

def area_triangulo(base: int, altura:int) -> float:
    if base <= 0 or altura <= 0:
        return -1
    area = (base*altura) / 2
    return area

class PrimoTestCase(unittest.TestCase):
    def test_area_triangulo(self):
        area = area_triangulo(1,5)
        self.assertEqual(area, 2.5)

################### EJERCICIO 3 #####################

# 1.Crea una clase "Empleado" que tiene como atributos el salario y el tiempo de antigüedad en cantidad de años. 
# 2.Agrega un método "aumentar_salario" que permita al usuario aumentar el salario del empleado en un porcentaje especificado
#   puedes utilizar la clase "Empleado" del ejercicio 4 del módulo 6.Programacion orientada a objetos . 
# 3.Agrega otro método "verificar_antigüedad" que permita al usuario verificar si el empleado tiene una antigüedad mayor a un año. 
# 4.Crea varios test utilizando pytest para comprobar que los métodos funcionan correctamente para distintos casos, como aumentar 
#   el salario con un porcentaje negativo, verificar la antigüedad con un tiempo negativo, y verificar la antigüedad con un tiempo específico.

class Empleado():
    
    __salario : int
    __tiempo_antiguedad : int
    
    def __init__(self, salario, tiempo_antiguedad) -> None:
        self.__salario = salario
        self.__tiempo_antiguedad = tiempo_antiguedad
        
    @property
    def tiempo_antiguedad(self):
        return self.__tiempo_antiguedad

    @tiempo_antiguedad.setter
    def tiempo_antiguedad(self, value):
        self.__tiempo_antiguedad = value
        
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, value):
        self.__salario = value
        
    def aumentar_salario(self, porcentaje : float):
        self.salario = self.salario + (self.salario * porcentaje)
    
    def verificar_antiguedad(self) -> bool:
        return self.tiempo_antiguedad >= 1
    
    

class TestEmpleado(unittest.TestCase):
    def setUp(self):
        self.empleado = Empleado(2000, 2)

    def test_aumentar_salario(self):
        self.empleado.aumentar_salario(0.1)
        self.assertEqual(self.empleado.salario, 2200.0)

    def test_tiempo_antiguedad(self):
        mas_un_año = self.empleado.verificar_antiguedad()
        self.assertTrue(mas_un_año, True)
      
################### EJERCICIO 4 #####################

# 1.Crea una clase "Criptomoneda" que tenga como atributos el nombre, la cantidad de criptomonedas en posesión y el valor de 1 criptomoneda en dólares. 
#   (Por ejemplo: nombre -> bitcoin, cantidad -> 10, valor_dolares -> 20000) 
# 2.Agrega un método "comprar" que permita al usuario comprar una cierta cantidad de la criptomoneda especificando el precio en dólares. 
# 3.Agrega otro método "vender" que permita al usuario vender una cierta cantidad de la criptomoneda especificando el precio en dólares. 
# 4.Crea varios test utilizando pytest para comprobar que los métodos funcionan correctamente para distintos casos, como comprar una cantidad mayor a la disponible en el mercado, 
# vender una cantidad mayor a la disponible en posesión y comprar y vender con un valor en dólares específico.

class Criptomoneda():
    
    __nombre : str
    __cantidad : float
    __valor_dolares : float
    
    def __init__(self,nombre, cantidad, valor_dolares) -> None:
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__valor_dolares = valor_dolares
        
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
        
    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, value):
        self.__cantidad = value
        
    @property
    def valor_dolares(self):
        return self.__valor_dolares

    @valor_dolares.setter
    def valor_dolares(self, value):
        self.__valor_dolares = value
        
    def comprar(self, dolares_invertidos:float) :
        self.cantidad = self.cantidad + (dolares_invertidos / self.valor_dolares)
        
    def vender(self, dolares_invertidos:float) :
        self.cantidad = self.cantidad - (dolares_invertidos / self.valor_dolares)
        
class TestCriptomoneda(unittest.TestCase):
    
    def setUp(self):
        self.cripto = Criptomoneda('r2d2_coin', 5.0, 10000.0)

    def test_comprar_criptomonedas(self):
        self.cripto.comprar(5000.0)
        self.assertEqual(self.cripto.cantidad, 5.5)

    def test_vender_criptomonedas(self):
        self.cripto.vender(10000.0)
        self.assertEqual(self.cripto.cantidad, 4.0)
   
unittest.main()
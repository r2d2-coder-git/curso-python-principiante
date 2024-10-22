import sys

sys.path.append('08.Programacion orientada a objetos/ejercicios/soluciones/ejercicio2/')

from persona import Persona

class Empleado(Persona):
    __cargo : str
    __salario : int
    
    def __init__(self, nombre, apellidos, edad, cargo, salario) -> None:
        super().__init__(nombre, apellidos, edad)
        self.__cargo = cargo
        self.__salario = salario
        
    def get_cargo(self) -> str:
        return self.__cargo

    def set_cargo(self, value):
        self.__cargo = value
        
    def get_salario(self) -> int:
        return self.__salario

    def set_salario(self, value):
        self.__salario = value
        
    def aumentar_salario(self, porcentaje : float):
        self.__salario = self.__salario + (self.__salario * porcentaje)
    
class Departamento:
    __nombre : str
    __empleados : list
    
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__empleados = []
    
    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, value):
        self.__nombre = value
        
    def get_empleados(self) -> list:
        return self.__empleados

    def set_empleados(self, value : list):
        self.__empleados = value.copy()

    def agregar_empleado(self, empleado: Empleado) -> None:
        self.__empleados.append(empleado)
        
    def listar_empleados(self) -> None:
        for empleado in self.__empleados:
            print(f"El empleado con nombre {empleado.get_nombre()} {empleado.get_apellidos()} tiene {empleado.get_edad()} años y tiene el cargo {empleado.get_cargo()} con un salario de {empleado.get_salario()}.")


class Empresa:
    __nombre : str
    __departamentos : dict
    
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__departamentos = {}
    
    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, value):
        self.__nombre = value
        
    def get_departamentos(self) -> dict:
        return self.__departamentos

    def set_departamentos(self, value : dict):
        self.__departamentos = value.copy()
        
    def agregar_departamento(self, departamento:Departamento) -> None:
        self.__departamentos.update({departamento.get_nombre() : departamento})
    
    def listar_departamentos(self) -> None:
        for nombre, departamento in self.__departamentos.items():
            print(f"El departamento {nombre} tiene los siguientes empleados: \n" )
            departamento.listar_empleados()
            print('\n')
    

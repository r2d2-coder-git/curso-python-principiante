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
        
    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, value):
        self.__cargo = value
        
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, value):
        self.__salario = value
        
    def aumentar_salario(self, porcentaje : float):
        self.salario = self.salario + (self.salario * porcentaje)
    
class Departamento:
    __nombre : str
    __empleados : list
    
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__empleados = []
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
        
    @property
    def empleados(self):
        return self.__empleados

    @empleados.setter
    def empleados(self, value : list):
        self.__empleados = value.copy()

    def agregar_empleado(self, empleado: Empleado) -> None:
        self.empleados.append(empleado)
        
    def listar_empleados(self) -> None:
        for empleado in self.empleados:
            print(f"El empleado con nombre {empleado.nombre} {empleado.apellidos} tiene {empleado.edad} años y tiene el cargo {empleado.cargo} con un salario de {empleado.salario}.")


class Empresa:
    __nombre : str
    __departamentos : dict
    
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__departamentos = {}
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
        
    @property
    def departamentos(self):
        return self.__departamentos

    @departamentos.setter
    def departamentos(self, value : dict):
        self.__departamentos = value.copy()
        
    def agregar_departamento(self, departamento:Departamento) -> None:
        self.departamentos.update({departamento.nombre : departamento})
    
    def listar_departamentos(self) -> None:
        for nombre, departamento in self.departamentos.items():
            print(f"El departamento {nombre} tiene los siguientes empleados: \n" )
            departamento.listar_empleados()
            print('\n')
    

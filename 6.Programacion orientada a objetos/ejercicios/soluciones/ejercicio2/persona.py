class Persona:
    __nombre : str
    __apellidos : str
    __edad :  int
    
    def __init__(self, nombre, apellidos, edad) -> None:
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad
        
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
        
    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        self.__apellidos = value
        
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        self.__edad = value
        
    def saludar(self) -> None:
        print(f"Hola, mi nombre es {self.nombre} {self.apellidos} y tengo {self.edad} años.")
    
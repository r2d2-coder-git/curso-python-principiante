class Persona:
    __nombre : str
    __apellidos : str
    __edad :  int
    
    def __init__(self, nombre, apellidos, edad) -> None:
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad
        
    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, value):
        self.__nombre = value
        
    def get_apellidos(self) -> str:
        return self.__apellidos

    def set_apellidos(self, value):
        self.__apellidos = value
        
    def get_edad(self) -> int:
        return self.__edad

    def set_edad(self, value):
        self.__edad = value
        
    def saludar(self) -> None:
        print(f"Hola, mi nombre es {self.__nombre} {self.__apellidos} y tengo {self.__edad} años.")
    
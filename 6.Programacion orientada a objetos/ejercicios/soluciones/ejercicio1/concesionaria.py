from vehiculo import Vehiculo

class Concesionaria():
    __inventario_coches : list
    
    def __init__(self) -> None:
        self.__inventario_coches = []
        
    @property
    def inventario_coches(self):
        return self.__inventario_coches

    @inventario_coches.setter
    def inventario_coches(self, value: list):
        self.__inventario_coches = value.copy()
        
    def agregar_vehiculo(self, vehiculo : Vehiculo):
        self.__inventario_coches.append(vehiculo)
    
    
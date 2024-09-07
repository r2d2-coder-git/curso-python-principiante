from vehiculo import Vehiculo

class Concesionaria():
    __inventario_coches : list
    
    def __init__(self) -> None:
        self.__inventario_coches = []
        
    def get_inventario_coches(self) -> list:
        return self.__inventario_coches

    def set_inventario_coches(self, value: list):
        self.__inventario_coches = value.copy()
        
    def agregar_vehiculo(self, vehiculo : Vehiculo):
        self.__inventario_coches.append(vehiculo)
    
    
class Vehiculo:
    
    __marca: str
    __modelo: str
    __año : int
    __color : str
    
    def __init__(self, marca, modelo, año, color):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__color = color
        
    
    def get_marca(self) -> str:
        return self.__marca
    
    def set_marca(self, value):
        self.__marca = value

    def get_modelo(self) -> str:
        return self.__modelo
    
    def set_modelo(self, value):
        self.__modelo = value
        
    def get_año(self) -> int:
        return self.__año
    
    def set_año(self, value):
        self.__año = value
   
    def get_color(self) -> str:
        return self.__color
    
    def set_color(self, value):
        self.__color = value
        
        
    def encender() ->None:
        print("El vehículo ha sido encendido.")
    
    def apagar() ->None:
        print("El vehículo ha sido apagado.")
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
        
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, value):
        self.__marca = value
        
    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, value):
        self.__modelo = value
        
    @property
    def año(self):
        return self.__año

    @año.setter
    def año(self, value):
        self.__año = value
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value
        
        
    def encender() ->None:
        print("El vehículo ha sido encendido.")
    
    def apagar() ->None:
        print("El vehículo ha sido apagado.")
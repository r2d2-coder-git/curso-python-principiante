from clases import Mascota


class Perro(Mascota):
    __color_pelo: str
    __raza: str
    __trofeos_ganados: dict

    def __init__(self, nombre, puntos_salud, nivel, edad, color_pelo, raza):
        super().__init__(nombre, puntos_salud, nivel, edad)
        self.__color_pelo = color_pelo
        self.__raza = raza
        self.__trofeos_ganados = {
            'Internacional': 0, 'Nacional': 0, 'Regional': 0
        }

    @property
    def color_pelo(self):
        return self.__color_pelo

    @color_pelo.setter
    def color_pelo(self, value):
        self.__color_pelo = value

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, value):
        self.__raza = value

    @property
    def trofeos_ganados(self):
        return self.__trofeos_ganados.copy()

    @trofeos_ganados.setter
    def trofeos_ganados(self, value):
        self.__trofeos_ganados = value.copy()

    # Sobreescritura del método ganar_torneo, utilizamos la funcionalidad del padre y la extendemos para que la clase Perro pueda guardar
    # los torneos ganados.
    def ganar_torneo(self, tipo_torneo: str) -> None:
        super().ganar_torneo(tipo_torneo)
        if tipo_torneo in self.__trofeos_ganados.keys():
            self.__trofeos_ganados[tipo_torneo] += 1


luisito: Perro = Perro('Luisito', 100, 1, 1, 'Pelirrojo', 'Lulu Pomerania')
luisito.ganar_torneo('Internacional')
print(luisito.nivel)
print(luisito.trofeos_ganados)

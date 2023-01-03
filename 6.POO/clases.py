
# Sintaxis:

# class NombreClase():
#   Atributos
#   def __init__(self):
#       Inicializar atributos (constructor)
#   Setters and getters
#   Metodos de clase
#

# Implementación de la clase mascota para un videojuego de animales.
# TODO: - Añade el atributo salud_maxima y cambiar el método alimentar_mascota para comprobar cuando tu mascota ya tenga la salud máxima
#       no añada más puntos de salud. Además, si una comida que se le va a dar supera la salud máxima también se tiene que controlar.

class Mascota():

    ############################# ATRIBUTOS DE LA CLASE #####################################

    __nombre: str
    _puntos_salud: int
    __nivel: int
    __edad: int

    ############################# CONSTRUCTOR DE LA CLASE #####################################

    def __init__(self, nombre, puntos_salud, nivel, edad):
        self.__nombre = nombre
        self._puntos_salud = puntos_salud
        self.__nivel = nivel
        self.__edad = edad

    ############################# METODOS GETTERS AND SETTERS #####################################

    # Con los decoradores lo que hacemos es convertir el acceso de los atributos como si fuesen publicos, pero en realidad están cumpliendo con
    # el principio de encapsulamiento de Programación Orienta a Objetos, ya que en realidad se están ejecutando los métodos definidos por nosotros.

    # Sintaxis getters: (Los atributos deben ser privados o protegidos, sino no tendría sentido hacer un get o set ya que podemos modificar y
    # consultar los atributos directamente, es más daría un bucle infinito.)
    # @property
    # def nombre_atributo(self):
    #   return self.__nombre_atributo

    # Sintaxis setters:
    # @nombre_atributo.setter
    # def nombre_atributo(self, value):
    #   self.__nombre_atributo = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def puntos_salud(self):
        return self._puntos_salud

    @puntos_salud.setter
    def puntos_salud(self, puntos_salud):
        self._puntos_salud = puntos_salud

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

  ############################# METODOS DE CLASE #####################################

  # Método que sirve para aumentar la salud a tu mascota.

    def alimentar_mascota(self, comida: str) -> None:
        if comida == 'comida_normal':
            self._salud += 10
        elif comida == 'comida_buena':
            self._salud += 20
        elif comida == 'comida_genial':
            self.salud += 30

        print(
            f'Mmm... que rico! Ahora me siento más fuerte y tengo {self._puntos_salud} puntos de salud.')

    # Método que sirve para aumentar de nivel a tu mascota en función del torneo que haya ganado.
    def ganar_torneo(self, tipo_torneo: str) -> None:
        if tipo_torneo == 'Regional':
            self.__nivel += 1
        elif tipo_torneo == 'Nacional':
            self.__nivel += 2
        elif tipo_torneo == 'Internacional':
            self.__nivel += 3

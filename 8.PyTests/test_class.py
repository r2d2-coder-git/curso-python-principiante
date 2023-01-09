############################## ¿COMO SE TESTEA UNA CLASE? #####################################


############################## 1. MANERA INEFICIENTE DE HACERLO #####################################

import unittest


class Encuesta():
    __pregunta: str
    __respuestas: list

    def __init__(self, pregunta):
        """Store a question, and prepare to store responses."""
        self.__pregunta = pregunta
        self.__respuestas = []

    @property
    def pregunta(self) -> str:
        return self.__pregunta

    @pregunta.setter
    def pregunta(self, value: str):
        self.__pregunta = value

    @property
    def respuestas(self) -> list:
        return self.__respuestas

    @respuestas.setter
    def nombre(self, value: list):
        self.__respuestas = value.copy()

    def mostrar_pregunta(self):
        print(self.question)

    def guardar_respuesta(self, nueva_respuesta):
        self.__respuestas.append(nueva_respuesta)

    def mostrar_resultados(self):
        print("Resultados de la encuesta:")
        for respuesta in self.__respuestas:
            print('- ' + respuesta)


# Este test es ineficiente ya que tenemos que crear un objeto Encuesta por cada llamada al método test_guardar_una_respuesta.
class TestEncuestaIneficiente(unittest.TestCase):
    def test_guardar_una_respuesta(self):
        pregunta = "Cuál es tu lengua materna?"
        encuesta = Encuesta(pregunta)
        encuesta.store_response('Castellano')
        self.assertIn('Castellano', encuesta.respuestas)


############################## 2. MANERA EFICIENTE DE HACERLO #####################################

# Python ejecuta el metodo setUp antes de ejecutar cada método que empiece por test_ dentro de una clase que hereda de unittest.TestCase.
# Por ello si sobreescribimos este método para inicilizar los objetos que vamos a usar en los tests nos ahorraremos mucha memoria evitando crear un objeto por test.

class TestEncuestaEficiente(unittest.TestCase):
    def setUp(self):
        pregunta = "Cuáles son los lenguajes que hablas?"
        self.encuesta = Encuesta(pregunta)
        self.respuestas = ['Ingles', 'Español', 'Chino']

    def test_guardar_una_respuesta(self):
        self.encuesta.guardar_respuesta(self.respuestas[0])
        self.assertIn(self.respuestas[0], self.encuesta.respuestas)

    def test_guardar_multiples_respuestas(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


# Esta llamada a main ejecuta los 3 tests aunque vengan de clases distintas porque las dos heredan de unittest.TestCase
unittest.main()

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

# This test is inneficient because we create one object per call to the method test_store_single_response.


class TestEncuesta(unittest.TestCase):
    def test_guardar_una_respuesta(self):
        pregunta = "Cuál es tu lengua materna?"
        encuesta = Encuesta(pregunta)
        encuesta.store_response('Castellano')
        self.assertIn('Castellano', encuesta.respuestas)


############################## 2. MANERA EFICIENTE DE HACERLO #####################################


class TestAnonymousSurvey(unittest.TestCase):
    # Python runs the setUp() method before runningeach method starting with test_.
    # In this method we create one object survey for all test methods.
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


# Esta llamada a main ejecuta los 3 tests aunque vengan de clases distintas porque las dos heredan de unittest.TestCase
unittest.main()

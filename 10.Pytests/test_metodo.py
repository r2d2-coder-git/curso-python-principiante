############################## ¿QUÉ SON LOS TESTS UNITARIOS? #####################################

# Los tests unitarios son pequeñas piezas de código que se escriben para probar que una determinada función o módulo de código funciona correctamente. 
# Sirven para asegurar que el código se comporta de la manera esperada y para detectar posibles errores o regressions en el código a medida que se realizan cambios.

# Los tests unitarios también son útiles para documentar cómo se espera que una función o módulo se comporte, lo que puede ser de gran ayuda para otros desarrolladores 
# que trabajen en el mismo código. Al escribir tests unitarios, es importante asegurarse de que se cubren todos los casos de uso posibles y de que se verifiquen todas 
# las condiciones de frontera. De esta manera, se puede tener más confianza en que el código funcionará correctamente en todos los casos.

############################## ¿CUÁLES SON LOS ASERTOS MÁS UTILIZADOS? #####################################

# assertEqual(a, b)  Comprobar que a == b
# assertNotEqual(a, b) Comprobar que a != b
# assertTrue(x) Comprobar que x es True
# assertFalse(x) Comprobar que x es False
# assertIn(item, list) Comprobar que un elemento está en una colección
# assertNotIn(item, list) Comprobar que un elemento no está en una colección.


############################## ¿COMO SE TESTEA UNA FUNCIÓN? #####################################

import unittest


def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()

# Para construir un test unitario tenemos que crear una clase que herede de unittest.TestCase, esta clase ejecuta todos los métodos que empiecen por test_, por eso hay que seguir la convención de definir nuestros tests
# como métodos que empiecen así. El método main de la clase unittest ejecuta nuestros tests unitarios.


class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name("arturo", "lorenzo")
        self.assertEqual(formatted_name, "Arturo Lorenzo")


unittest.main()

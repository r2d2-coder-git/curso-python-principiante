import unittest

def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name("arturo","lorenzo")
        self.assertEqual(formatted_name, "Arturo Lorenzo")

unittest.main()

"""
assertEqual(a, b) Verify that a == b
assertNotEqual(a, b) Verify that a != b
assertTrue(x) Verify that x is True
assertFalse(x) Verify that x is False
assertIn(item, list) Verify that item is in list
assertNotIn(item, list) Verify that item is not in list
"""
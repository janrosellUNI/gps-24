import unittest
import transform



class TestStringMethods(unittest.TestCase):
    """
        Esta clase contiene las pruebas unitarias para la función 'StringMethods'.
        """

    def test_is_upper(self):
        """
                Esta función cambia un string a mayusculas.
                """
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")

    def test_is_lower(self):
        """
                Esta función cambia un string a minusculas.
                """
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")

    def test_is_capitalize(self):
        """
                Esta función capitaliza un string.
                """
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")


if __name__ == '__main__':
    unittest.main()

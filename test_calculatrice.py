import unittest
from votre_module_calculatrice import addition, soustraction, multiplication, division

class TestCalculatrice(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(3, 5), 8)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)

    def test_soustraction(self):
        self.assertEqual(soustraction(8, 3), 5)
        self.assertEqual(soustraction(-1, 1), -2)
        self.assertEqual(soustraction(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 5), 15)
        self.assertEqual(multiplication(-1, 1), -1)
        self.assertEqual(multiplication(0, 0), 0)

    def test_division(self):
        self.assertEqual(division(8, 2), 4)
        self.assertEqual(division(-6, 3), -2)
        self.assertEqual(division(0, 5), 0)

        # Test de division par zéro
        self.assertEqual(division(5, 0), "Erreur : division par zéro")

if __name__ == '__main__':
    unittest.main()

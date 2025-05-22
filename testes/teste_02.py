def soma(a, b):
    return a + b

import unittest

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)  # 2 + 3 = 5

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)  # -1 + (-1) = -2

    def test_soma_mista(self):
        self.assertEqual(soma(5, -3), 2)  # 5 + (-3) = 2

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)  # 0 + 0 = 0

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

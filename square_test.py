import math

def area(a): 
    return a * a


def perimeter(a):
    return 4 * a

import unittest

class Test_Functions_Square(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(-3), 9)
        self.assertEqual(area(0), 0)
        self.assertAlmostEqual(area(2.5), 6.25)

    def test_perimeter(self):
        self.assertEqual(perimeter(-3), -12)
        self.assertEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(2.5), 10.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area('a')
            perimeter('b')

if __name__ == '__main__':
    unittest.main()

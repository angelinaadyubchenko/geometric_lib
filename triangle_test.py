import math

def area(a, h): 
    return a * h / 2 

def perimeter(a, b, c):
    return a + b + c 

import unittest

class Test_Functions_Triangle(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(-3, 4), -6)
        self.assertEqual(area(0, 4), 0)
        self.assertAlmostEqual(area(5, 6.5), 16.25)

    def test_perimeter(self):
        self.assertEqual(perimeter(3.5, 4.5, 5), 13)
        self.assertEqual(perimeter(0, 4, 5), 9)
        self.assertEqual(perimeter(-5, 6, 7), 8)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area('a', 'b')
            perimeter('a', 'b', 'c')

if __name__ == '__main__':
    unittest.main()

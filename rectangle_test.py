import math

def area(a, b): 
    return a * b 

def perimeter(a, b): 
    return 2*a + 2*b
 
import unittest

class Test_Functions_Rectangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(3, -4), -12)
        self.assertEqual(area(0, 4), 0)
        self.assertAlmostEqual(area(2.5, 3.5), 8.75)

    def test_perimeter(self):
        self.assertEqual(perimeter(-3, 4), 2)
        self.assertEqual(perimeter(0, 4), 8)
        self.assertAlmostEqual(perimeter(2.5, 3.5), 12.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area('a', 'b')
            perimeter('a', 'b')

if __name__ == '__main__':
    unittest.main()



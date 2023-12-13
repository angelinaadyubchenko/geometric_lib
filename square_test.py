import math
def area(a):
''Принимает число a, возвращает квадрат числа а'''
    return a * a


def perimeter(a):
'''Принимает число a, возвращает число a умноженное на 4'''
    return 4 * a
a = 2
print(area(a))
print(perimeter(a))

import unittest

def area(a):
    '''Принимает число a, возвращает квадрат числа а'''
    return a * a

def perimeter(a):
    '''Принимает число a, возвращает число a умноженное на 4'''
    return 4 * a

class Test_Square_Calculation(unittest.TestCase):

     def test_perimeter_calculation(self):
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(-4), -16)
    
    def test_area_calculation(self):
        self.assertEqual(area(4), 16)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(-4), 16)
        
    def test_negative_digits(self):
        self.assertEqual(area(-4), 16)
        self.assertEqual(perimeter(-4), -16)

if __name__ == '__main__':
    unittest.main()

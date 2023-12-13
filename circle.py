import math


def area(r):
''' Принимаем число r возвращаем значение квадрата числа умноженное на число пи ''' 
    return math.pi * r * r


def perimeter(r):
''' Принимаем число r возвращаем значение  числа 2 умноженное на число пи'''
    return 2 * math.pi * r
a = 2
print(area(a))
print(perimeter(a))

import unittest
class Circle_Test(unittest.TestCase):
   def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area('a')
            perimeter('b')


if name == '__main__':
    unittest.main()

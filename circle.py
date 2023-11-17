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
    def testarea(self):
        r = 5
        result = area(r)
        self.assertEqual(result, math.pi * r * r)

    def testperimeter(self):
        r = 5
        result = perimeter(r)
        self.assertEqual(result, 2  * math.pi * r)

    def testareaandperimeterconsistency(self):
        r = 5
        self.assertEqual(area(r), math.pi  * r  * r)
        self.assertEqual(perimeter(r), 2  math.pi  r)

if name == '__main__':
    unittest.main()

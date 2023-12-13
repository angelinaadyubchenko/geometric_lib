def area(a, h): 
'''Принимает число a и число h, возвращает среднее геометрическое чисел а и b'''
    return a * h / 2 

def perimeter(a, b, c): 
'''Принимает число a, число b и число с, возвращает сумму чисел a,b,c'''
    return a + b + c 
a = 2
h = 3
b = 4
c = 5 
print(area(a,h))
print(perimeter(a,b,c))

import unittest

def area(a, h):
    '''Принимает число a и число h, возвращает среднее геометрическое чисел а и b'''
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает число a, число b и число c, возвращает сумму чисел a, b, c'''
    return a + b + c

class Test_Geometry_Calculation(unittest.TestCase):

    def test_perimeter_calculation(self):
        self.assertEqual(perimeter(4, 5, 6), 15)
        self.assertEqual(perimeter(0, 5, 10), 15)
        self.assertEqual(perimeter(-4, 5, 3), 4)

    def test_area_calculation(self):
        self.assertEqual(area(4, 6), 12)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(-4, 5), -10)
    
        
    def test_negative_digits(self):
        self.assertEqual(area(-4, 5), -10)
        self.assertEqual(perimeter(-4, 5, 3), 4)

if __name__ == '__main__':
    unittest.main()

import math

def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

import unittest

class Test_Functions_Circle(unittest.TestCase):

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area('a')
            perimeter('b')

if __name__ == '__main__':
    unittest.main()
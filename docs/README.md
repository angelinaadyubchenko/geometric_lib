# Discription of function:
## Circle:
    import math

    - Импортирую библиотеку math для того чтобы использовать число пи

    def area(r):
    - Принимает число r, возвращает квадрат числа r, умноженный на число пи
        return math.pi * r * r

    def perimeter(r):
    - Принимает число r, возвращает число r умноженное на два и на число пи
        return 2 * math.pi * r
```
a = 2
print(area(a))
print(perimeter(a))
```
## Rectangle:
    def area(a, b):
    - Принимает число a и число b, возвращает число a умноженное на число b
        return a * b

    def perimeter(a, b):
    - Принимает число a и число b, возвращает сумму чисел a и b, умноженную на 2
        return 2*(a + b)
```
a = 2
b = 1
print(area(a,b))
print(perimeter(a,b))
```
## Square:
    def area(a):
    - Принимает число a, возвращает квадрат числа а
        return a * a

    def perimeter(a):
    - Принимает число a, возвращает число a умноженное на 4
        return 4 * a
```
a = 2
print(area(a))
print(perimeter(a))
```
## Tringle:
    def area(a, h):
    - Принимает число a и число h, возвращает среднее геометрическое чисел а и b
        return a * h / 2

    def perimeter(a, b, c):
    - Принимает число a, число b и число с, возвращает сумму чисел a,b,c
        return a + b + с
```
a = 2
h = 3
b = 4
c = 5 
print(area(a,h))
print(perimeter(a,b,c))
```

#History of project :
commit f97cedfa6616f9fc03b115ce7b4407fdb0fa22ff (HEAD -> main, origin/main, origin/HEAD, new_features_408573)
Author: angelina <angelinadyubchenko884@gmail.com>
Date:   Thu Oct 19 21:06:27 2023 +0300

    the bug has been fixed

commit a73386cd7edbcc0b8deb6d681157e4b6048836f5
Author: angelina <angelinadyubchenko884@gmail.com>
Date:   Thu Oct 19 21:02:50 2023 +0300

    new file has been created

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added


# Write Unit tests:
## Circle:
    import unittest
    import math
    
    -Импортирую библиотеку unittest для того чтобы использовать юниттесты 
    -Импортирую библиотеку math для того чтобы использовать число пи

    def area(r):
        '''Принимает число r, возвращает квадрат числа r, умноженный на число пи'''
        return math.pi * r * r

    def perimeter(r):
        '''Принимает число r, возвращает число r умноженное на два и на число п'''
        return 2 * math.pi * r


    
    class Circle_Test(unittest.TestCase):
	

    	def test_area(self):
	-В данной функции проверяется правильность работы функции area для различных входных значений
        	r = 5
        	result = area(r)
        	self.assertEqual(result, math.pi * r * r)
		-сравниваем значение, которое выдает функция area и правильный ответ 

    	def test_perimeter(self):
	-В данной функции проверяется правильность работы функции perimeter для различных входных значений
        	r = 5
        	result = perimeter(r)
        	self.assertEqual(result, 2  * math.pi * r)
		-сравниваем значение, которое выдает функция perimeter и правильный ответ

    	def test_area_and_perimeter_consistency(self):
	- В данной функции проверяется правильность работы предыдущих функций на отрицательных значениях
        	r = 5
        	self.assertEqual(area(r), math.pi  * r  * r)
        	self.assertEqual(perimeter(r), 2  math.pi  r)
		-сравниваем значение, которое выдает функция area  и perimeter при отрицательных значениях и правильный ответ
    	if __name__ == '__main__':
        	unittest.main()
    	-вызов юниттеста

## Rectangle:
    import unittest
    -Импортирую библиотеку unittest для того чтобы использовать юниттесты 
        
    def area(a, b):
        '''Принимает число a и число b, возвращает число a умноженное на число b'''
        return a * b

    def perimeter(a, b):
        '''Принимает число a и число b, возвращает сумму чисел a и b, умноженную на 2'''
        return 2*(a + b)
class Test_Area_And_Perimeter(unittest.TestCase):
    
    def test_area_calculation(self):
	  -В данной функции проверяется правильность работы функции area для различных входных значений
        self.assertEqual(area(4, 5), 20)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(-4, 5), -20)
	-сравниваем значение, которое выдает функция area и правильный ответ
    
    def test_perimeter_calculation(self):
	  -В данной функции проверяется правильность работы функции perimeter для различных входных значений
        self.assertEqual(perimeter(4, 5), 18)
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(-4, 5), 2)
	-сравниваем значение, которое выдает функция perimeter и правильный ответ
        
    def test_negative_values(self):
	- В данной функции проверяется правильность работы предыдущих функций на отрицательных значениях
        self.assertEqual(area(-4, 5), -20)
        self.assertEqual(perimeter(-4, 5), 2)
	-сравниваем значение, которое выдает функция area  и perimeter при отрицательных значениях и правильный ответ

	if __name__ == '__main__':
    		unittest.main()     
    	-вызов юниттеста

if name == 'main':
        unittest.main()
    -вызов юниттеста

## Square:
    import unittest
    -Импортирую библиотеку unittest для того чтобы использовать юниттесты 

    def area(a):
        '''Принимает число a, возвращает квадрат числа а'''
        return a * a

    def perimeter(a):
        '''Принимает число a, возвращает число a умноженное на 4'''
        return 4 * a
class Test_Square_Calculation(unittest.TestCase):

     def test_perimeter_calculation(self):
	 -В данной функции проверяется правильность работы функции perimetr для различных входных значений
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(-4), -16)
	-сравниваем значение, которое выдает функция perimetr и правильный ответ
    
    def test_area_calculation(self):
	 -В данной функции проверяется правильность работы функции area для различных входных значений
        self.assertEqual(area(4), 16)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(-4), 16)
	 -сравниваем значение, которое выдает функция area и правильный ответ
        
    def test_negative_digits(self):
	- В данной функции проверяется правильность работы предыдущих функций на отрицательных значениях
        self.assertEqual(area(-4), 16)
        self.assertEqual(perimeter(-4), -16)
	-сравниваем значение, которое выдает функция area  и perimeter при отрицательных значениях и правильный ответ

	if __name__ == '__main__':
    		unittest.main()
	-вызов юниттеста

## Tringle:
    import unittest
    -Импортирую библиотеку unittest для того чтобы использовать юниттесты 

    def area(a, h):
        '''Принимает число a и число h, возвращает среднее геометрическое чисел а и b'''
        return a * h / 2

    def perimeter(a, b, c):
        '''Принимает число a, число b и число c, возвращает сумму чисел a, b, c'''
        return a + b + c
class Test_Geometry_Calculation(unittest.TestCase):

    def test_perimeter_calculation(self):
	  -В данной функции проверяется правильность работы функции perimeter для различных входных значений
        self.assertEqual(perimeter(4, 5, 6), 15)
        self.assertEqual(perimeter(0, 5, 10), 15)
        self.assertEqual(perimeter(-4, 5, 3), 4)
	-сравниваем значение, которое выдает функция perimetr и правильный ответ

    def test_area_calculation(self):
	 -В данной функции проверяется правильность работы функции area для различных входных значений
        self.assertEqual(area(4, 6), 12)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(-4, 5), -10)
    	-сравниваем значение, которое выдает функция area и правильный ответ
        
    def test_negative_digits(self):
	- В данной функции проверяется правильность работы предыдущих функций на отрицательных значениях
        self.assertEqual(area(-4, 5), -10)
        self.assertEqual(perimeter(-4, 5, 3), 4)
	-сравниваем значение, которое выдает функция area  и perimeter при отрицательных значениях и правильный ответ

	if __name__ == '__main__':
    		unittest.main()
		-вызов юниттеста

# Description of function:
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

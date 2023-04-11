
# 0x0A. Python - Inheritance

## Tasks

### 0. Lookup

Write a function that returns the list of available attributes and methods of an object:

  - Prototype: def lookup(obj):
  - Returns a list object
  - You are not allowed to import any module </br>

File:[0-lookup.py](0-lookup.py)

### 1. My list

Write a class MyList that inherits from list:

  - Public instance method: def print\_sorted\(self\): that prints the list, but sorted \(ascending sort\)
  - You can assume that all the elements of the list will be of type int
  - You are not allowed to import any module </br>

File:[1-my\_list.py](1-my_list.py), [tests/1-my\_list.txt](tests/1-my_list.txt)

### 2. Exact same object

Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

  - Prototype: def is\_same\_class\(obj, a\_class\):
  - You are not allowed to import any module </br>

File:[2-is\_same\_class.py](2-is_same_class.py)

### 3. Same class or inherit from

Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

  - Prototype: def is\_kind\_of\_class\(obj, a\_class\):
  - You are not allowed to import any module </br>

File:[3-is\_kind\_of\_class.py](3-is_kind_of_class.py)

### 4. Only sub class of

Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

  - Prototype: def inherits\_from\(obj, a\_class\):
  - You are not allowed to import any module </br>

File:[4-inherits\_from.py](4-inherits_from.py)

### 5. Geometry module

Write an empty class BaseGeometry.

  - You are not allowed to import any module </br>

File:[5-base\_geometry.py](5-base_geometry.py)

### 6. Improve Geometry
Write a class BaseGeometry \(based on 5-base\_geometry.py\).

  - Public instance method: def area\(self\): that raises an Exception with the message area\(\) is not implemented
  - You are not allowed to import any module </br>

File:[6-base\_geometry.py](6-base_geometry.py)

### 7. Integer validator
Write a class BaseGeometry \(based on 6-base\_geometry.py\).

  - Public instance method: def area\(self\): that raises an Exception with the message area\(\) is not implemented
  - Public instance method: def integer\_validator\(self, name, value\): that validates value:
   >>   you can assume name is always a string
   >>   if value is not an integer: raise a TypeError exception, with the message \<name\> must be an integer
   >>   if value is less or equal to 0: raise a ValueError exception with the message \<name\> must be greater than 0
  - You are not allowed to import any module </br>

File:[7-base\_geometry.py](7-base_geometry.py), [tests/7-base\_geometry.txt](tests/7-base_geometry.txt)

### 8. Rectangle
Write a class Rectangle that inherits from BaseGeometry \(7-base\_geometry.py\).

  - Instantiation with width and height: def \_\_init\_\_\(self, width, height\):
  >>    width and height must be private. No getter or setter
  >>    width and height must be positive integers, validated by integer\_validator </br>

File:[8-rectangle.py](8-rectangle.py)

### 9. Full rectangle

Write a class Rectangle that inherits from BaseGeometry \(7-base\_geometry.py\). \(task based on 8-rectangle.py\)

  - Instantiation with width and height: def \_\_init\_\_\(self, width, height\)::
  >>    width and height must be private. No getter or setter
  >>    width and height must be positive integers validated by integer\_validator
  - the area\(\) method must be implemented
  - print\(\) should print, and str\(\) should return, the following rectangle description: \[Rectangle\] \<width\>/\\\<height\> </br>

File:[9-rectangle.py](9-rectangle.py)

### 10. Square #1

Write a class Square that inherits from Rectangle \(9-rectangle.py\):

  - Instantiation with size: def \_\_init\_\_\(self, size\)::
  >>    size must be private. No getter or setter
  >>    size must be a positive integer, validated by integer\_validator
  - the area\(\) method must be implemented </br>

File:[10-square.py](10-square.py)

### 11. Square #2
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

  - Instantiation with size: def \_\_init\_\_\(self, size\)::
  >>    size must be private. No getter or setter
  >>    size must be a positive integer, validated by integer\_validator
  - the area\(\) method must be implemented
  - print\(\) should print, and str\(\) should return, the square description: \[Square\] \<width\>/\<height\> </br>

File:[11-square.py](11-square.py)

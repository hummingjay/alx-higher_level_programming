
# 0x05. Python - Exceptions

## Tasks

### 0. Safe list printing

Write a function that prints x elements of a list.

  - Prototype: def safe\_print\_list(my\_list=[], x=0):
  - my\_list can contain any type (integer, string, etc.)
  - All elements must be printed on the same line followed by a new line.
  - x represents the number of elements to print
  - x can be bigger than the length of my\_list
  - Returns the real number of elements printed
  - You have to use try: / except:
  - You are not allowed to import any module
  - You are not allowed to use len() </br>
File: [0-safe\_print\_list.py](0-safe_print_list.py)

### 1. Safe printing of an integers list

Write a function that prints an integer with "{:d}".format().

  - Prototype: def safe\_print\_integer(value):
  - value can be any type (integer, string, etc.)
  - The integer should be printed followed by a new line
  - Returns True if value has been correctly printed (it means the value is an integer)
  - Otherwise, returns False
  - You have to use try: / except:
  - You have to use "{:d}".format() to print as integer
  - You are not allowed to import any module
  - You are not allowed to use type() </br>
File: [1-safe\_print\_integer.py](1-safe_print_integer.py)

### 2. Print and count integers

Write a function that prints the first x elements of a list and only integers.

  - Prototype: def safe\_print\_list\_integers(my\_list=[], x=0):
  - my\_list can contain any type (integer, string, etc.)
  - All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
  - x represents the number of elements to access in my\_list
  - x can be bigger than the length of my\_list - if it’s the case, an exception is expected to occur
  - Returns the real number of integers printed
  - You have to use try: / except:
  - You have to use "{:d}".format() to print an integer
  - You are not allowed to import any module
  - You are not allowed to use len() </br>
File: [2-safe\_print\_list\_integers.py](2-safe_print_list_integers.py)

### 3. Integers division with debug

Write a function that divides 2 integers and prints the result.

  - Prototype: def safe\_print\_division(a, b):
  - You can assume that a and b are integers
  - The result of the division should print on the finally: section preceded by Inside result:
  - Returns the value of the division, otherwise: None
  - You have to use try: / except: / finally:
  - You have to use "{}".format() to print the result
  - You are not allowed to import any module
File: [3-safe\_print\_division.py](3-safe_print_division.py)

### 4. Divide a list 

Write a function that divides element by element 2 lists.

  - Prototype: def list\_division(my\_list\_1, my\_list\_2, list\_length):
  - my\_list\_1 and my\_list\_2 can contain any type (integer, string, etc.)
  - list\_length can be bigger than the length of both lists
  - Returns a new list (length = list\_length) with all divisions
  - If 2 elements can’t be divided, the division result should be equal to 0
  - If an element is not an integer or float:
    >>  print: wrong type
  - If the division can’t be done (/0):
    >>  print: division by 0
  - If my\_list\_1 or my\_list\_2 is too short
    >>  print: out of range
  - You have to use try: / except: / finally:
  - You are not allowed to import any module </br>
File: [4-list\_division.py](4-list_division.py)

### 5. Raise exception 

Write a function that raises a type exception.

  - Prototype: def raise\_exception():
  - You are not allowed to import any module </br>
File: [5-raise\_exception.py](5-raise_exception.py)

### 6. Raise a message

Write a function that raises a name exception with a message.

  - Prototype: def raise\_exception\_msg(message=""):
  - You are not allowed to import any module </br>
File: [6-raise\_exception\_msg.py](6-raise_exception_msg.py)

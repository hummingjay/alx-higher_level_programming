
# 0x13. JavaScript - Objects, Scopes and Closures

## TASKS

### [0. Rectangle #0](0-rectangle.js)

Write an empty class Rectangle that defines a rectangle:

  * You must use the class notation for defining your class </br>

File:[0-rectangle.js](0-rectangle.js)

### [1. Rectangle #1](1-rectangle.js)

Write a class `Rectangle` that defines a rectangle:

  * You must use the `class` notation for defining your class
  * The constructor must take 2 arguments `w` and `h`
  * Initialize the instance attribute `width` with the value of `w`
  * Initialize the instance attribute `height` with the value of `h` </br>

File:[1-rectangle.js](1-rectangle.js)

### [2. Rectangle #2](2-rectangle.js)

Write a class `Rectangle` that defines a rectangle:

  * You must use the `class` notation for defining your class
  * The constructor must take 2 arguments `w` and `h`
  * Initialize the instance attribute width with the value of w
  * Initialize the instance attribute `height` with the value of `h`
  * If `w` or `h` is equal to 0 or not a positive integer, create an empty object </br>

File:[2-rectangle.js](2-rectangle.js)

### [3. Rectangle #3](3-rectangle.js)

Write a class `Rectangle` that defines a rectangle:

  * You must use the `class` notation for defining your class
  * The constructor must take 2 arguments: `w` and `h`
  * Initialize the instance attribute `width` with the value of `w`
  * Initialize the instance attribute `height` with the value of `h`
  * If `w` or `h` is equal to 0 or not a positive integer, create an empty object
  * Create an instance method called `print()` that prints the rectangle using the character `X` </br>

File:[3-rectangle.js](3-rectangle.js)

### [4. Rectangle #4](4-rectangle.js)

Write a class `Rectangle` that defines a rectangle:

  * You must use the `class` notation for defining your class
  * The constructor must take 2 arguments: `w` and `h`
  * Initialize the instance attribute `width` with the value of `w`
  * Initialize the instance attribute `height` with the value of `h`
  * If `w` or `h` is equal to 0 or not a positive integer, create an empty object
  * Create an instance method called `print()` that prints the rectangle using the character `X`
  * Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
  * Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2 </br>

File:[4-rectangle.js](4-rectangle.js)

### [5. Square #0](5-square.js)

Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

  * You must use the class notation for defining your class and extends
  * The constructor must take 1 argument: size
  * The constructor of Rectangle must be called (by using `super()`) </br>

File:[5-square.js](5-square.js)

### [6. Square #1](6-square.js)

Write a class Square that defines a square and inherits from Square of 5-square.js:

  * You must use the `class` notation for defining your class and `extends`
  * Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
    * If `c` is undefined, use the character `X`

File:[6-square.js](6-square.js)

### [7. Occurrences](7. Occurrences)

Write a function that returns the number of occurrences in a list:

  * Prototype: `exports.nbOccurences = function (list, searchElement)` </br>

File:[7-occurrences.js](7-occurrences.js)

### [8. Esrever](8-esrever.js)

Write a function that returns the reversed version of a list:

  * Prototype: `exports.esrever = function (list)`
  * You are not allow to use the built-in method `reverse` </br>

File:[8-esrever.js](8-esrever.js)

### [9. Log me](9-logme.js)

Write a function that prints the number of arguments already printed and the new argument value. (see example below)

  * Prototype: `exports.logMe = function (item)`
  * Output format: `<number arguments already printed>: <current argument value>` </br>

File:[9-logme.js](9-logme.js)

### [10. Number conversion ](10-converter.js)

Write a function that converts a number from base 10 to another base passed as argument:

  * Prototype: `exports.converter = function (base)`
  * You are not allowed to import any file
  * You are not allowed to declare any new variable (`var`, `let`, etc..) </br>

File:[10-converter.js](10-converter.js)

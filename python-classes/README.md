<h1 align="center">Python 🐍 - Classes and Objects</h1>

### Recommended Links 🔗

- [8. Object Oriented Programming - MIT *__by Dr. Bell__*](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

- [Object Oriented Programming *__By Bernd Klein.__*](https://python-course.eu/oop/object-oriented-programming.php) 

- [¿Cómo usar CLASES en PYTHON?](https://www.youtube.com/watch?v=9x7RK6mb1uA)
- [Python Classes and Objects *__by socratica__*](https://www.youtube.com/watch?v=apACNr7DC_s)
	
### Learning Objectives 🎯
- Why Python programming is awesome
- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or inst    ance
- What is an attribute
- What are and how to use public, protected and private attrib    utes
- What is self
- What is a method
- What is the special ``__init__`` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Informatio    n Hiding
- What is a property
- What is the difference between an attribute and a property i    n Python
- What is the Pythonic way to write getters and setters in Pyt    hon
- How to dynamically create arbitrary new attributes for exist    ing instances of a class
- How to bind attributes to object and classes
- What is the `` __dict__`` of a class and/or instance of a cl    ass and what does it contain
- How does Python find the attributes of an object or class
- How to use the getattr function

### Tasks 📚
__0. My first square__
- Write an empty class ``Square`` that defines a square:
	- You are not allowed to import any module

__1. Square with size__
- Write a class ``Square`` that defines a square by: (based on ``0-square.py``)
	- Private instance attribute: ``size``
	- Instantiation with ``size`` (no type/value verification)
	- You are not allowed to import any module
__Why?__

_Why ``size`` is private attribute?_

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

__2. Size validation__
- Write a class ``Square`` that defines a square by: (based on ``1-square.py``)
	- Private instance attribute: ``size``
	- Instantiation with optional ``size: def __init__(self, size=0):``
		- ``size`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``size must be an integer``
		- if ``size`` is less than ``0``, raise a ``ValueError`` exception with the message ``size must be >= 0``
	- You are not allowed to import any module

__3. Area of a square__
- Write a class ``Square`` that defines a square by: (based on ``2-square.py)``
	- Private instance attribute: ``size``
	- Instantiation with optional ``size: def __init__(self, size=0):``
		- ``size`` must be an integer, otherwise raise a ``TypeError`` exception with the message size must be an integer
		- if ``size`` is less than ``0``, raise a ``ValueError`` exception with the message ``size must be >= 0``
	- Public instance method: ``def area(self):`` that returns the current square area
	- You are not allowed to import any module
	     
__4. Access and update private attribute__
- Write a class ``Square`` that defines a square by: (based on ``3-square.py``)
	- Private instance attribute: ``size``:
		- property ``def size(self):`` to retrieve it
		- property setter ``def size(self, value):`` to set it:
			- ``size`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``size must be an integer``
			- if ``size`` is less than ``0``, raise a ``ValueError`` exception with the message ``size must be >= 0``
	- Instantiation with optional ``size: def __init__(self, size=0):``
	- Public instance method: ``def area(self):`` that returns the current square area
	- You are not allowed to import any module
__Why?__
_Why a getter and setter?_

Reminder: ``size`` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.


__5. Printing a square__
- Write a class ``Square`` that defines a square by: (based on ``4-square.py``)
	- Private instance attribute: ``size``:
		- property ``def size(self):`` to retrieve it
		- property setter ``def size(self, value):`` to set it:
			- ``size`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``size must be an integer``
			- if ``size`` is less than ``0``, raise a ``ValueError`` exception with the message ``size must be >= 0``
	- Instantiation with optional ``size: def __init__(self, size=0):``
	- Public instance method: ``def area(self):`` that returns the current square area
	- Public instance method: ``def my_print(self):`` that prints in stdout the square with the character ``#``:
		- if ``size`` is equal to 0, print an empty line
	- You are not allowed to import any module

__6. Coordinates of a square__
- Write a class Square that defines a square by: (based on 5-square.py)
	- Private instance attribute: ``size``:
		- property ``def size(self):`` to retrieve it
		- property setter ``def size(self, value):`` to set it:
			- ``size`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``size must be an integer``
			- if ``size`` is less than ``0``, raise a ``ValueError`` exception with the message ``size must be >= 0``
	- Private instance attribute: ``position``:
		- property ``def position(self):`` to retrieve it
		- property setter ``def position(self, value):`` to set it:
			- ``position`` must be a tuple of 2 positive integers, otherwise raise a ``TypeError`` exception with the message ``position must be a tuple of 2 positive integers``
	- Instantiation with optional ``size`` and optional ``position: def __init__(self, size=0, position=(0, 0)):``
	- Public instance method: ``def area(self):`` that returns the current square area
	- Public instance method: ``def my_print(self):`` that prints in stdout the square with the character ``#``:
		- if ``size`` is equal to 0, print an empty line
		- ``position`` should be use by using space - __Don’t fill lines by spaces__ when ``position[1] > 0``
	- You are not allowed to import any module						  


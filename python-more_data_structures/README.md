<h1 align="center">Python 🐍 - More Data Structures: Set, Dictionary</h1>

### Recommended Links 🔗
- [30-days-of-python 🐍 Study Repo](https://github.com/Asabeneh/30-Days-Of-Python/tree/master)
- [Curso de PYTHON desde CERO para PRINCIPIANTES 🐍 Estructuras de Datos](https://youtu.be/Kp4Mvapo5kc?t=10874)

- [Sequence Types 🐍 list, tuple, range](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

### Learning Objectives 🎯
- Why Python programming is awesome
- What are sets and how to use them
- What are the most common methods of set and how to use them
- When to use sets versus lists
- How to iterate into a set
- What are dictionaries and how to use them
- When to use dictionaries versus lists or sets
- What is a key in a dictionary
- How to iterate over a dictionary
- What is a lambda function
- What are the map, reduce and filter functions

### Tasks 📚
__0. Squared simple__
- Write a function that computes the square value of all integers of a matrix.
	- Prototype: ``def square_matrix_simple(matrix=[]):``
	- ``matrix`` is a 2 dimensional array
	- Returns a new matrix:
		- Same size as ``matrix``
		- Each value should be the square of the value of the input
	- Initial matrix should not be modified
	- You are not allowed to import any module
	- You are allowed to use regular loops, ``map``, etc.

__1. Search and replace__
- Write a function that replaces all occurrences of an element by another in a new list
	- Prototype: ``def search_replace(my_list, search, replace):``
	- ``my_list`` is the initial list
	- ``search`` is the element to replace in the list
	- ``replace`` is the new element
	- You are not allowed to import any module
'''
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/$ 	
'''	    

__2. Unique addition__
- Write a function that adds all unique integers in a list (only once for each integer)
	
	- Prototype: ``def uniq_add(my_list=[]):``
	- You are not allowed to import any module

__3. Present in both__
- Write a function that returns a set of common elements in two sets.
	- Prototype: ``def common_elements(set_1, set_2):``
	- You are not allowed to import any module

__4. Only differents__
- Write a function that returns a set of all elements present in only one set.
	- Prototype: ``def only_diff_elements(set_1, set_2):``
	- You are not allowed to import any module

__5. Number of keys__
- Write a function that returns the number of keys in a dictionary.
	- Prototype: ``def number_keys(a_dictionary):``
	- You are not allowed to import any module
	 
__6. Print sorted dictionary__
- Write a function that prints a dictionary by ordered keys.
	- Prototype: ``def print_sorted_dictionary(a_dictionary):``
	- You can assume that all keys are strings
	- Keys should be sorted by alphabetic order
	- Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
	- Dictionary values can have any type
	- You are not allowed to import any module	  

__7. Update dictionary__
- Write a function that replaces or adds key/value in a dictionary.
	- Prototype: ``def update_dictionary(a_dictionary, key, value):``
	- ``key`` argument will be always a string
	- ``value`` argument will be any type
	- If a key exists in the dictionary, the value will be replaced
	- If a key doesn’t exist in the dictionary, it will be created
	- You are not allowed to import any module

__8. Simple delete by key__
- Write a function that deletes a key in a dictionary.
	- Prototype: ``def simple_delete(a_dictionary, key=""):``
	- ``key`` argument will be always a string
	- If a key doesn’t exist, the dictionary won’t change
	- You are not allowed to import any module

__9. Multiply by 2__
- Write a function that returns a new dictionary with all values multiplied by 2
	- Prototype: def multiply_by_2(a_dictionary):
	- You can assume that all values are only integers
	- Returns a new dictionary
	- You are not allowed to import any module

10. Best score
- Write a function that returns a key with the biggest integer value.
	- Prototype: ``def best_score(a_dictionary):``
	- You can assume that all values are only integers
	- If no score found, return ``None``
	- You can assume all students have a different score
	- You are not allowed to import any module

__11. Multiply by using map__
- Write a function that returns a list with all values multiplied by a number without using any loops.
	- Prototype: ``def multiply_list_map(my_list=[], number=0):``
	- Returns a new list:
	    - Same length as ``my_list``
i	    - Each value should be multiplied by ``number``
	- Initial list should not be modified
	- You are not allowed to import any module
	- You have to use ``map``
	- Your file should be max 3 lines

__12. Roman to Integer__
__Technical interview preparation:__
	- You are not allowed to google anything
	- Whiteboard first
Create a function ``def roman_to_int(roman_string):`` that converts a ``Roman numeral`` to an integer.
	- You can assume the number will be between 1 to 3999.
	- ``def roman_to_int(roman_string)`` must return an integer
	- If the ``roman_string`` is not a string or ``None``, return 0

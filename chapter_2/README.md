# Variables and Data Types in Python

## Introduction

Python is a versatile and powerful programming language that supports various data types. Understanding how to use variables and data types is fundamental to writing effective Python code.

## Table of Contents

1. [Variables](#variables)
2. [Data Types](#data-types)
    - [Numbers](#numbers)
    - [Strings](#strings)
    - [Booleans](#booleans)
    - [Lists](#lists)
    - [Tuples](#tuples)
    - [Sets](#sets)
    - [Dictionaries](#dictionaries)
3. [Type Conversion](#type-conversion)

## Variables

Variables are used to store information that can be referenced and manipulated in a program. In Python, you do not need to declare the type of a variable explicitly.

### Example

```python
# Assigning values to variables
x = 10
name = "Alice"
is_student = True

print(x)         # Output: 10
print(name)      # Output: Alice
print(is_student) # Output: True

# Integer
age = 25

# Floating-point number
height = 5.9

# Complex number
complex_num = 3 + 4j

print(type(age))         # Output: <class 'int'>
print(type(height))      # Output: <class 'float'>
print(type(complex_num)) # Output: <class 'complex'>

#String
greeting = "Hello, World!"
print(greeting)          # Output: Hello, World!
print(type(greeting))    # Output: <class 'str'>

#Boolean
is_valid = True
print(is_valid)          # Output: True
print(type(is_valid))    # Output: <class 'bool'>

#List
fruits = ["apple", "banana", "cherry"]
print(fruits)            # Output: ['apple', 'banana', 'cherry']
print(type(fruits))      # Output: <class 'list'>

#Tuple
coordinates = (10.0, 20.0)
print(coordinates)       # Output: (10.0, 20.0)
print(type(coordinates)) # Output: <class 'tuple'>

#Sets
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)    # Output: {1, 2, 3, 4, 5}
print(type(unique_numbers)) # Output: <class 'set'>

#Dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)            # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(type(person))      # Output: <class 'dict'>

#Type Conversion
# Convert integer to string
num = 10
num_str = str(num)
print(num_str)           # Output: '10'
print(type(num_str))     # Output: <class 'str'>

# Convert string to integer
age_str = "25"
age = int(age_str)
print(age)               # Output: 25
print(type(age))         # Output: <class 'int'>

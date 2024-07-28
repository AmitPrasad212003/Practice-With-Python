# Python Decorators

Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behavior of a function or class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.

## Basic Decorator

A basic example of a decorator is as follows:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)

say_hello()
```
When you run this code, you will see:

```vbnet
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

# Using @ Syntax
Python provides a simpler syntax for applying decorators using the @ symbol, also known as "pie" syntax:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```
The output will be the same as before:

```vbnet
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```
Decorators with Arguments
If you want to create a decorator that accepts arguments, you need to add another level of nested functions:

```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("World")
```
This will print:
```
Hello World
Hello World
Hello World
```
# Decorators with Return Values
If the function being decorated returns a value, you can capture and return it from the wrapper function:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(2, 3))
```
This will output:
```
Before the function call
After the function call
5
```
Class Decorators
Decorators can also be applied to classes:

```python
def decorator(cls):
    class WrappedClass(cls):
        def new_method(self):
            return "New Method Added"
    return WrappedClass

@decorator
class MyClass:
    def original_method(self):
        return "Original Method"

obj = MyClass()
print(obj.original_method())  # Output: Original Method
print(obj.new_method())       # Output: New Method Added
```

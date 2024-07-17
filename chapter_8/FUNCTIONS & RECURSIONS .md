# FUNCTIONS & RECURSIONS

## Functions in Python

### What is a Function?
A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

### Defining a Function
In Python, a function is defined using the `def` keyword.

```python
def my_function():
    print("Hello from a function")
```
# Calling a Function
To call a function, use the function name followed by parenthesis.

```python
my_function()
```
# Function Parameters
Information can be passed to functions as parameters. Parameters are specified after the function name, inside the parentheses.

``` python
def my_function_with_params(name):
    print(f"Hello, {name}")

my_function_with_params("Alice")
```
# Default Parameter Value
If we call the function without parameter, it uses the default value.

```python
def my_function_with_default(name="Guest"):
    print(f"Hello, {name}")

my_function_with_default()
my_function_with_default("Bob")
```
# Return Values
To let a function return a value, use the return statement.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```
## Recursion in Python
# What is Recursion?
Recursion is a common mathematical and programming concept. It means that a function calls itself. This technique is known as recursion.

# Recursive Function
A function that calls itself is known as a recursive function.

# Example: Factorial of a Number
The factorial of a number is the product of all the integers from 1 to that number. For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.

```python
def factorial(n):
    if n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(6))  # Output: 720
```
# Understanding the Recursive Function
1. Base Case: This stops the recursion. If the base case is not defined, the function will call itself indefinitely.
2. Recursive Case: The part of the function where it calls itself with modified arguments.

# Example: Fibonacci Sequence
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # Output: 8
```
# Benefits of Recursion
- Simplifies the code, making it easier to read and maintain.
- Particularly useful for problems that can be broken down into similar sub-problems (e.g., tree traversal, graph traversal).

# Drawbacks of Recursion
- Can lead to performance issues (e.g., stack overflow) if not implemented carefully.
- Higher memory consumption due to function call stack.

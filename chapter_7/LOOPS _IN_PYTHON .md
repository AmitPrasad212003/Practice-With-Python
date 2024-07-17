# Loops in Python

## Introduction
Loops are used in programming to repeat a block of code. In Python, there are two main types of loops:

1. `for` loops
2. `while` loops

## `for` Loop
The `for` loop is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string). This is less like the `for` keyword in other programming languages, and works more like an iterator method.

### Syntax
```python
for variable in sequence:
    # code block to be executed
Example
python
Copy code
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
# while Loop
The while loop continues to execute a block of code as long as a specified condition is true.

Syntax
```python
while condition:
    # code block to be executed
# Example

count = 0
while count < 5:
    print(count)
    count += 1
```

# Loop Control Statements
Python provides three control statements to control the flow of loops:

1. break: Exits the loop prematurely.
2. continue: Skips the rest of the code inside the loop for the current iteration only.
3. pass: Does nothing and can be used as a placeholder.
# break Statement
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```
# continue Statement
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```
# pass Statement
```python
for i in range(10):
    if i == 5:
        pass
    print(i)
```
## Nested Loops
You can use one or more loops inside another loop. This is called nested loops.

# Example
```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

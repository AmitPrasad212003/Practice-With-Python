# Conditional Expressions in Python

Conditional expressions, also known as ternary operators, allow you to write simple conditional statements in a compact form. They are often used for assigning values based on a condition.

## Basic Syntax

The basic syntax for a conditional expression in Python is:

```python
value_if_true if condition else value_if_false
```
This can be broken down as:

- condition: The expression evaluated as either True or False.
- value_if_true: The value assigned if the condition is True.
- value_if_false: The value assigned if the condition is False.
## Examples
# Example 1: Basic Usage
```python
x = 5
y = 10
max_value = x if x > y else y
print(max_value)  # Output: 10
```

# Example 2: Conditional Assignment
```python
status = 'Success' if operation_completed else 'Failed'
print(status)
```
Here, status is assigned 'Success' if operation_completed is True, otherwise it is assigned 'Failed'.

# Example 3: Using with Functions
```python
def is_even(num):
    return "Even" if num % 2 == 0 else "Odd"

print(is_even(4))  # Output: Even
print(is_even(7))  # Output: Odd
```
In this example, the is_even function uses a conditional expression to return 'Even' if the number is even, and 'Odd' if it is odd.

# Example 4: Nested Conditional Expressions
```python
x = 10
result = "Positive" if x > 0 else ("Zero" if x == 0 else "Negative")
print(result)  # Output: Positive
```
Here, nested conditional expressions are used to check if x is positive, zero, or negative.

## Advantages of Conditional Expressions
1. Conciseness: They make the code more concise and readable by reducing the number of lines.
2. Readability: When used appropriately, they can make the code more readable by clearly expressing the intent.
3. Single Line: They allow for writing condition-based assignments in a single line.
# Use Cases
# Setting Default Values
Conditional expressions are often used to set default values:

```python
user_input = input("Enter your name: ")
name = user_input if user_input else "Guest"
print(name)
```
If the user provides input, it is assigned to name; otherwise, name is assigned "Guest".

# Inline Condition Checks
They can be used for inline condition checks without the need for a full if-else block:

```python
def get_discounted_price(price, discount):
    return price - discount if discount else price

print(get_discounted_price(100, 20))  # Output: 80
print(get_discounted_price(100, 0))   # Output: 100
```
# Simplifying Return Statements
Conditional expressions can simplify return statements in functions:

``` python
def check_age(age):
    return "Adult" if age >= 18 else "Minor"

print(check_age(20))  # Output: Adult
print(check_age(16))  # Output: Minor
```

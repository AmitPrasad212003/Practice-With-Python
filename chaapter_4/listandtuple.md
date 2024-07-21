# Lists and Tuples in Python

## Introduction

In Python, lists and tuples are data structures that can store multiple items. They are both sequence types and share a number of properties, but they have important differences.

## Lists

### Characteristics
- **Mutable**: Elements can be changed after the list is created.
- **Ordered**: Elements have a defined order, and this order will not change unless explicitly modified.
- **Dynamic**: Lists can grow and shrink as needed.

### Creating a List
You can create a list by placing comma-separated values between square brackets.
```python
# Example of creating a list
my_list = [1, 2, 3, 4, 5]
```

### Accessing Elements
- You can access elements by their index, starting from 0.
```python
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3
```
### Modifying Elements
- Lists allow modification of their elements.
```python
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]
```
### Adding Elements
- append(): Adds an element to the end of the list.
```python
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]
```
- insert(): Adds an element at a specified index.
```python
my_list.insert(1, 20)
print(my_list)  # Output: [10, 20, 2, 3, 4, 5, 6]
```
### Removing Elements
- remove(): Removes the first occurrence of a value.
```python
my_list.remove(20)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]
```
- pop(): Removes an element by index.
```python
my_list.pop(0)
print(my_list)  # Output: [2, 3, 4, 5, 6]
```

### Tuples
## Characteristics
- Immutable: Elements cannot be changed after the tuple is created.
- Ordered: Elements have a defined order, and this order will not change.
- Static: Tuples have a fixed size.
## Creating a Tuple
- You can create a tuple by placing comma-separated values between parentheses.
```python
# Example of creating a tuple
my_tuple = (1, 2, 3, 4, 5)
```
## Accessing Elements
- You can access elements by their index, starting from 0.
```python
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3
```
## Modifying Elements
- Tuples do not allow modification of their elements.
```python
# This will raise a TypeError
my_tuple[0] = 10
```
### Useful Tuple Methods
- count(): Returns the number of times a specified value appears in the tuple.
```python
count = my_tuple.count(2)
print(count)  # Output: 1
```
- index(): Returns the index of the first occurrence of a specified value.
```python
index = my_tuple.index(3)
print(index)  # Output: 2
```
## Key Differences
- Mutability: Lists are mutable, whereas tuples are immutable.
- Performance: Tuples can be more performant for certain operations due to their immutability.
- Use Cases: Use lists when you need a collection of items that can change. Use tuples when you need a collection of items that should not change.


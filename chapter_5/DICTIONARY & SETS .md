# Dictionaries and Sets in Python

## Dictionaries

A dictionary in Python is an unordered collection of items. Each item is stored as a key-value pair. Dictionaries are indexed by keys, which can be any immutable type; usually, strings or numbers.

### Creating a Dictionary

```python
# Example of a dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}
```
# Accessing Values
You can access the value associated with a specific key using square brackets or the .get() method.

```python
# Using square brackets
name = my_dict['name']
print(name)  # Output: John

# Using .get() method
age = my_dict.get('age')
print(age)  # Output: 25
```

# Adding and Modifying Items
You can add new key-value pairs or modify existing ones by assigning a value to a key.

```python
# Adding a new key-value pair
my_dict['email'] = 'john@example.com'

# Modifying an existing key-value pair
my_dict['age'] = 26
```
# Removing Items
You can remove items from a dictionary using the del statement, the `.pop()` method, or the `.popitem()` method.

```python
# Using del statement
del my_dict['city']

# Using .pop() method
email = my_dict.pop('email')

# Using .popitem() method (removes the last inserted item)
item = my_dict.popitem()
```
# Dictionary Methods
- my_dict.keys(): Returns a view object that displays a list of all the keys in the dictionary.
- my_dict.values(): Returns a view object that displays a list of all the values in the dictionary.
- my_dict.items(): Returns a view object that displays a list of dictionary's key-value tuple pairs.
- my_dict.update(other_dict): Updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs.
- 
# Sets
A set is an unordered collection of unique items. Sets are mutable, meaning you can add or remove items from them.

# Creating a Set
```python
# Example of a set
my_set = {1, 2, 3, 4, 5}
```
# Adding and Removing Items
You can add items to a set using the `.add()` method and remove items using the `.remove()` or `.discard()` methods.

```python
# Adding an item
my_set.add(6)

# Removing an item using remove (raises KeyError if item not found)
my_set.remove(3)

# Removing an item using discard (does not raise an error if item not found)
my_set.discard(2)

# Set Operations
Sets support various mathematical operations such as union, intersection, difference, and symmetric difference.

```python
# Union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # Output: {1, 2, 3, 4, 5}

# Intersection of sets
intersection_set = set1.intersection(set2)  # Output: {3}

# Difference of sets
difference_set = set1.difference(set2)  # Output: {1, 2}

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)  # Output: {1, 2, 4, 5}
```
#Set Methods
- my_set.add(item): Adds an item to the set.
- my_set.remove(item): Removes an item from the set; raises a KeyError if the item is not found.
- my_set.discard(item): Removes an item from the set; does nothing if the item is not found.
- my_set.pop(): Removes and returns an arbitrary set element; raises KeyError if the set is empty.
- my_set.clear(): Removes all items from the set.
- my_set.union(other_set): Returns the union of sets as a new set.
- my_set.intersection(other_set): Returns the intersection of sets as a new set.
- my_set.difference(other_set): Returns the difference of sets as a new set.
- my_set.symmetric_difference(other_set): Returns the symmetric difference of sets as a new set.

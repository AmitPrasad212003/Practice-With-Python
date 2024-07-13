# Python Strings and Their Functions

## Introduction to Strings

In Python, a string is a sequence of characters enclosed in single quotes (`'`) or double quotes (`"`). Strings are immutable, meaning they cannot be changed after they are created.

### Creating Strings

```python
# Single quotes
string1 = 'Hello, World!'

# Double quotes
string2 = "Hello, World!"

# Triple quotes for multi-line strings
string3 = '''Hello,
World!'''

string4 = """Hello,
World!"""

### String Functions
# len() : Returns the length of the string.
length = len('Hello')  # 5

# str() : Converts an object to a string.
num = 123
str_num = str(num)  # '123'

# upper() : Converts all characters in the string to uppercase.
s = 'hello'
s_upper = s.upper()  # 'HELLO'

# lower() : Converts all characters in the string to lowercase.
s = 'HELLO'
s_lower = s.lower()  # 'hello'

# capitalize() : Capitalizes the first character of the string.
s = 'hello'
s_cap = s.capitalize()  # 'Hello'

# title() : Converts the first character of each word to uppercase.
s = 'hello world'
s_title = s.title()  # 'Hello World'

# strip() : Removes leading and trailing whitespace.
s = '  hello  '
s_strip = s.strip()  # 'hello'

# replace(old, new) : Replaces all occurrences of a substring with another substring.
s = 'hello world'
s_replace = s.replace('world', 'Python')  # 'hello Python'

# split(separator) : Splits the string into a list of substrings based on a separator.
s = 'hello world'
s_split = s.split(' ')  # ['hello', 'world']

# join(iterable) : Joins elements of an iterable into a single string, separated by the string used to call the method.
list_of_strings = ['hello', 'world']
s_join = ' '.join(list_of_strings)  # 'hello world'

# find(substring) : Returns the lowest index of the substring if it is found in the string.
s = 'hello world'
index = s.find('world')  # 6

# startswith(prefix) : Returns True if the string starts with the specified prefix.
s = 'hello world'
s_start = s.startswith('hello')  # True

# endswith(suffix) : Returns True if the string ends with the specified suffix.
s = 'hello world'
s_end = s.endswith('world')  # True


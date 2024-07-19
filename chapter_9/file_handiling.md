## Introduction
File I/O (Input/Output) operations are essential for handling files in Python. This includes reading from and writing to files. This document covers various file modes and basic file operations in Python.

## File Modes
When opening a file in Python, you can specify the mode to indicate the purpose of opening the file.

| Mode | Description |
|------|-------------|
| `'r'` | Read mode. Opens the file for reading. An error occurs if the file does not exist. |
| `'w'` | Write mode. Opens the file for writing. Creates a new file if it does not exist or truncates the file if it exists. |
| `'a'` | Append mode. Opens the file for writing and appends to the end of the file if it exists. |
| `'x'` | Exclusive creation mode. Creates a new file. Fails if the file already exists. |
| `'b'` | Binary mode. Opens the file in binary mode. |
| `'t'` | Text mode. Opens the file in text mode (default mode). |
| `'+'` | Read and write mode. Opens the file for both reading and writing. |

## Basic File Operations

### Opening a File
The `open()` function is used to open a file. It requires the file path and the mode.

```python
# Open a file in read mode
file = open('example.txt', 'r')
```
# Writing to a File
The write() method is used to write content to a file.

```python
# Open a file in write mode
file = open('example.txt', 'w')
# Write content to the file
file.write('Hello, World!')
# Close the file
file.close()
```
# Reading from a File
The read() method is used to read the entire content of a file. The readline() method reads a single line from the file, and readlines() reads all lines and returns them as a list.

```python
# Open a file in read mode
file = open('example.txt', 'r')
# Read the content of the file
content = file.read()
# Print the content
print(content)
# Close the file
file.close()
```
# Using a Context Manager
Using a context manager (with statement) is a more Pythonic way to handle file operations, as it ensures the file is properly closed even if an error occurs.

```python
with open('example.txt', 'w') as file:
    file.write('Hello, World!')  # Writes content to the file
# File is automatically closed when exiting the with block
```
# Appending to a File
The a mode is used to append content to the end of a file without truncating it.

```python
# Open a file in append mode
with open('example.txt', 'a') as file:
    file.write('\nAppended text.')  # Appends content to the file
```

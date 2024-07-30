# Understanding Scope in Python

Scope in Python refers to the visibility and lifetime of variables within a program. It determines where a variable can be accessed and modified. Python uses the LEGB rule to resolve the scope of variables, which stands for Local, Enclosing, Global, and Built-in.

## LEGB Rule

The LEGB rule is a hierarchy that Python follows to resolve the scope of variables. When a variable is referenced, Python searches for the variable in the following order:

1. **Local Scope**: 
    - The local scope refers to the variables defined within a function. These variables are only accessible within that function.
    - Example:
      ```python
      def my_function():
          local_var = 10
          print(local_var)  # Accessible here
      my_function()
      print(local_var)  # Error: local_var is not defined
      ```

2. **Enclosing Scope**:
    - The enclosing scope refers to variables in the local scope of enclosing functions. This is applicable to nested functions.
    - Example:
      ```python
      def outer_function():
          outer_var = 20
          def inner_function():
              print(outer_var)  # Accessible here
          inner_function()
      outer_function()
      ```

3. **Global Scope**:
    - The global scope refers to variables defined at the top level of a script or module, or explicitly declared global using the `global` keyword. These variables are accessible from any part of the code.
    - Example:
      ```python
      global_var = 30
      def my_function():
          print(global_var)  # Accessible here
      my_function()
      print(global_var)  # Accessible here
      ```

4. **Built-in Scope**:
    - The built-in scope refers to special reserved keywords and functions provided by Python. These are always available without any need for declaration.
    - Example:
      ```python
      print(len("Hello World"))  # len() is a built-in function
      ```

## Global and Nonlocal Keywords

### Global Keyword
The `global` keyword is used to modify a global variable within a local scope.
```python
global_var = 40

def my_function():
    global global_var
    global_var = 50  # Modifies the global variable

my_function()
print(global_var)  # Output: 50
```
# Nonlocal Keyword
The nonlocal keyword is used to modify a variable in the enclosing (non-global) scope.

```python
def outer_function():
    outer_var = 60

    def inner_function():
        nonlocal outer_var
        outer_var = 70  # Modifies the enclosing variable

    inner_function()
    print(outer_var)  # Output: 70

outer_function()
```

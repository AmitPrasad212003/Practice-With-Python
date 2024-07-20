# Object-Oriented Programming (OOP) in Python

## Introduction

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. Objects can be thought of as real-world entities that have attributes (data) and behaviors (methods). Python is an object-oriented language, which means it supports the OOP paradigm alongside other programming paradigms like procedural and functional programming.

## Key Concepts of OOP

### 1. Classes and Objects

- **Class**: A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
- **Object**: An instance of a class. It is created using the class blueprint and can have unique values for its attributes.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking")

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
dog1.bark()  # Output: Buddy is barking
```
2. Inheritance
Inheritance is a mechanism where a new class inherits the attributes and methods of an existing class. The new class is called the derived (or child) class, and the existing class is called the base (or parent) class.

```python
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("Dog")
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} barks")

dog1 = Dog("Buddy", 3)
dog1.make_sound()  # Output: Buddy barks
```
## Types of Inheritance
1. Single Inheritance: A derived class inherits from a single base class.
```python
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

dog = Dog()
dog.eat()  # Inherited from Animal
dog.bark()  # Defined in Dog
```
2. Multiple Inheritance: A derived class inherits from more than one base class.
```python
class Canine:
    def bark(self):
        print("Barking")

class Pet:
    def play(self):
        print("Playing")

class Dog(Canine, Pet):
    pass

dog = Dog()
dog.bark()  # Inherited from Canine
dog.play()  # Inherited from Pet
```
3. Multilevel Inheritance: A derived class inherits from another derived class.
```python
class Animal:
    def eat(self):
        print("Eating")

class Mammal(Animal):
    def walk(self):
        print("Walking")

class Dog(Mammal):
    def bark(self):
        print("Barking")

dog = Dog()
dog.eat()  # Inherited from Animal
dog.walk()  # Inherited from Mammal
dog.bark()  # Defined in Dog
```
4. Hierarchical Inheritance: Multiple derived classes inherit from a single base class.
```python
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meowing")

dog = Dog()
cat = Cat()
dog.eat()  # Inherited from Animal
dog.bark()  # Defined in Dog
cat.eat()  # Inherited from Animal
cat.meow()  # Defined in Cat
```
5. Hybrid Inheritance: A combination of two or more types of inheritance.
```python
class Animal:
    def eat(self):
        print("Eating")

class Canine(Animal):
    def bark(self):
        print("Barking")

class Pet:
    def play(self):
        print("Playing")

class Dog(Canine, Pet):
    pass

dog = Dog()
dog.eat()  # Inherited from Animal
dog.bark()  # Inherited from Canine
dog.play()  # Inherited from Pet
```
3. Encapsulation
Encapsulation is the practice of bundling data (attributes) and methods (functions) that operate on the data into a single unit, or class. It restricts direct access to some of the object's components, which can prevent the accidental modification of data.

```python
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age > 0:
            self.__age = age

person1 = Person("Alice", 30)
print(person1.get_name())  # Output: Alice
person1.set_age(31)
```
4. Polymorphism
Polymorphism allows methods to do different things based on the object it is acting upon, even though they share the same name. It can be achieved through method overriding and method overloading (though Python does not support method overloading directly).

- Method Overriding: A child class can provide a specific implementation of a method that is already defined in its parent class.
```python
class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()
# Output:
# Bark
# Meow
```
# Advantages of OOP
- Modularity: The source code for an object can be written and maintained independently of the source code for other objects.
- Reusability: Objects and classes can be reused across programs.
- Scalability: Easier to manage complex software development.
- Maintainability: Encapsulation and modularity make it easier to update and maintain the code.

# Keywords
- Class: A blueprint for creating objects.
- Object: An instance of a class.
- Inheritance: A mechanism where a new class inherits attributes and methods from an existing class.
- Encapsulation: Bundling data and methods that operate on the data within one unit and restricting direct access to some components.
- Polymorphism: The ability of different objects to respond to the same function in different ways.
- Method Overriding: A child class provides a specific implementation of a method that is already defined in its parent class.
- Private Attribute: An attribute that is not accessible directly from outside the class, usually prefixed with double underscores (__).
  
# Access Modifiers in Python
Access modifiers in Python are used to set the accessibility of classes, methods, and variables. Unlike some other programming languages, Python does not have explicit keywords like private, protected, and public. Instead, it uses naming conventions to indicate the intended level of access control. Here are the common types of access modifiers in Python:

# Types of Access Modifiers
1. Public
Public members (attributes and methods) are accessible from outside the class.
By default, all members of a class are public unless specified otherwise.
```python
class MyClass:
    def __init__(self, name):
        self.name = name  # Public attribute

    def display_name(self):
        print(f"Name: {self.name}")  # Public method

obj = MyClass("John")
print(obj.name)  # Accessible
obj.display_name()  # Accessible
```
2. Protected
Protected members are intended to be accessible only within the class and its subclasses.
In Python, protected members are indicated by a single underscore (_) prefix.
```python
class BaseClass:
    def __init__(self, name):
        self._name = name  # Protected attribute

    def _display_name(self):  # Protected method
        print(f"Name: {self._name}")

class DerivedClass(BaseClass):
    def show_name(self):
        self._display_name()  # Accessible within subclass

obj = DerivedClass("John")
obj.show_name()  # Accessible
print(obj._name)  # Accessible, but not recommended
```
3. Private
Private members are intended to be accessible only within the class itself.
In Python, private members are indicated by a double underscore (__) prefix.
Python performs name mangling to prevent accidental access, which changes the name of the member internally.
```python
class MyClass:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def __display_name(self):  # Private method
        print(f"Name: {self.__name}")

    def public_method(self):
        self.__display_name()  # Accessible within the class

obj = MyClass("John")
obj.public_method()  # Accessible
# print(obj.__name)  # Not accessible, raises AttributeError
# obj.__display_name()  # Not accessible, raises AttributeError

# Accessing name-mangled attributes (not recommended)
print(obj._MyClass__name)  # Accessible
obj._MyClass__display_name()  # Accessible
```

# Keywords
- Public: Members accessible from outside the class.
- Protected: Members intended to be accessible within the class and its subclasses, indicated by a single underscore (_).
- Private: Members intended to be accessible only within the class itself, indicated by a double underscore (__).

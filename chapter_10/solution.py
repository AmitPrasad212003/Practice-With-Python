# 1. Create a class (2-D vector) and use it to create another class representing a 3-Dvector.

# class Two_D_Vector :
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"The vevtor is {self.i}i + {self.j}j ")


# class Three_D_Vector(Two_D_Vector) :
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k

#     def show(self):
#         print(f"The vevtor is {self.i}i + {self.j}j + {self.k}k")

# a = Two_D_Vector(1,2)
# a.show()
# b = Three_D_Vector(1,2,3)
# b.show()


# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

# class Animals:
#     pass

# class Pets(Animals):
#     pass 

# class Dog(Pets):
    
#     @staticmethod
#     def bark():
#         print("Bow Bow!")


# d = Dog()
# d.bark()


# 3. Create a class ‘Employee’ and add salary and increment properties to it.
 #Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary

# class Employee():
#     salary = 23
#     increment = 20

#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,salary):
#         self.increment = ((salary/self.salary) - 1)*100

# e = Employee()

# # print(e.salaryAfterIncrement)

# e.salaryAfterIncrement = 280

# print(e.increment)


# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.


# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i

#     def __add__(self,c2):
#         return Complex(self.r + c2.r , self.i + c2.i)
    
#     def __mul__(self, c2):
#         real_part = self.r * c2.r - self.i * c2.i
#         imaginary_part = self.r * c2.i + self.i * c2.r
#         return Complex(real_part, imaginary_part)
    
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
        
    
# c1 = Complex(1,2)
# c2 = Complex(3,4)

# print(c1+ c2)
# print(c1* c2)


# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.


# class Vector:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self, other):
#         result = (self.x + other.x + self.y + other.y + self.z + other.z )
#         return result
    
#     def __mul__(self, other):
#         result = (self.x * other.x + self.y * other.y + self.z * other.z )
#         return result
    
#     def __str__(self):
#         return f"Vector({self.x}, {self.y}, {self.z})"
    
    
# # Test the implementation 

# v1 = Vector(1,2,3)
# v2 = Vector(4,5,6)
# v3 = Vector(7,8,9)

# print(v1 + v2)
# print(v1 + v2 )

# print(v1 + v3)
# print(v1 * v3)
    


# 6. Write __str__() method to print the vector as follows:


# class Vector:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self, other):
#         result = Vector(self.x + other.x , self.y + other.y , self.z + other.z) 
#         return result
    
#     def __mul__(self, other):
#         result = self.x * other.x + self.y * other.y + self.z * other.z 
#         return result
    
#     def __str__(self):
#         return f" {self.x}i +  {self.y}j + {self.z}k "
    
    
# # Test the implementation 

# v1 = Vector(1,2,3)
# v2 = Vector(4,5,6)
# v3 = Vector(7,8,9)

# print(v1 + v2)
# print(v1 * v2 )

# print(v1 + v3)
# print(v1 * v3)
    


# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self,l):
        self.l = l
    
    def __len__(self):
        return len(self.l)
    
    
# Test the implementation 

v1 = Vector([1,2,3,4,5,6])
print(len(v1))
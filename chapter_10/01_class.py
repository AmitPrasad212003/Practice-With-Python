class Employee:
    language = "py" # This is a class attributes
    salary = 1200000


harry = Employee()
harry.name = "Harry" # This is an object attributes / instance attribute
print(harry.name,harry.language,harry.salary)

Amit = Employee()
Amit.name = "Amit" # This is an object attributes / instance attribute
print(Amit.name,Amit.language,Amit.salary)


# Here name is object attributes / instance attribute and salary & language are class attributes as they directly belong to the class
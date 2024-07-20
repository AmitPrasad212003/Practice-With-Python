class Employee:
    language = "py" # This is a class attributes
    salary = 1200000

    def __init__(self,name,salary,language): # dunder method which is automatically called
        print("I an creating an objects")
        self.name = name
        self.salary = salary
        self.language = language



    def getInfo(self):
        print(f"The language is {self.language}.\nThe salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


# harry = Employee()  # not work if set init constructor
# harry.name = "AMit" 
# print(harry.name,harry.salary)

Amit = Employee("Amit",1500000,"Python")
print(Amit.name,Amit.salary,Amit.language)


# amit = Employee()
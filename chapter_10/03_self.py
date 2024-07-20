class Employee:
    language = "py" # This is a class attributes
    salary = 1200000
    def getInfo(self):
        print(f"The language is {self.language}.\nThe salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning")


harry = Employee()
harry.language = "js" # This is an object attributes / instance attribute
harry.greet()
harry.getInfo()
# Employee.getInfo(harry)
class Employee:
    company = "ITC"
    name = "Default_name"
    salary = 120000
    def show(self):
        print(f"The name is {self.company} and the salary is {self.salary}")

class Coder:
    language = "Python"

    def printLanguage(self):
        print(f"Out of all the language here is your language : {self.language}")



class Programmer(Employee,Coder):
    company = "ITC InfoTech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language}")


a = Employee()
b = Programmer()

print(a.company,b.company)


b.show()
b.printLanguage()
b.showLanguage()



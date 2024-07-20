# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.

# class Programmer:
#     company = "Microsoft"

#     def __init__(slf,name, salary, pin):
#         slf.name = name
#         slf.salary = salary
#         slf.pin = pin

# p = Programmer("Harry",1200000,123123)
# # print(p.company,"\t",p.name,"\t",p.salary,"\t",p.pin)
# print(f"{p.company}  {p.name}  {p.salary}  {p.pin}")
# r = Programmer("Amit",2000000,234123)
# print(f"{r.company}  {r.name}  {r.salary}  {r.pin}")


# 2. Write a class “Calculator” capable of finding square, cube and square root of a number

# class Calculator:
#     def __init__(slf,n):
#         slf.n = n

#     def square(slf):
#         print(f"The square is {slf.n*slf.n}")

#     def cube(slf):
#         print(f"The cube is {slf.n*slf.n*slf.n}")

#     def squareroot(slf):
#         # print(slf.n)
#         print(f"The squareroot is {slf.n**1/2}")

# a = Calculator(4)
# a.square()
# a.cube()
# a.squareroot()


# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?


# class Demo:
#     a =  4

# o = Demo()
# print(o.a)# Print the class attribute because instance attribute is not present 
# o.a = 0 
# print(o.a)# Print the instance attribute because instance attribute is present 

# print(Demo.a) # print the class attribute
# # The ans. is NO


# 4. Add a static method in problem 2, to greet the user with hello.


# class Calculator:
#     def __init__(slf,n):
#         slf.n = n

#     def square(slf):
#         print(f"The square is {slf.n*slf.n}")

#     def cube(slf):
#         print(f"The cube is {slf.n*slf.n*slf.n}")

#     def squareroot(slf):
#         # print(slf.n)
#         print(f"The squareroot is {slf.n**1/2}")
    
#     @staticmethod
#     def hello():
#         print("Hello there!")

# a = Calculator(4)
# a.square()
# a.cube()
# a.squareroot()
# a.hello()


# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways
# from random import randint
# class Train:
#     def __init__(slf,trainNo):
#         slf.trainNo = trainNo
#     def book(slf,fro,to):
#         print(f"Ticket is booked in train no : {slf.trainNo} from {fro} to {to}")

#     def getStatus(slf):
#         print(f"Train no : {slf.trainNo} is running on time")

#     def getFare(slf,fro,to):
#          print(f"Ticket is fare in train no : {slf.trainNo}\nfrom {fro} to {to} is : {randint(222,5567)}")
    
# t = Train(345231)
# t.book("Randnagar","Randipaga")
# t.getFare("Randnagar","Randipaga")
# t.getStatus()

# 6. Can you change the slf-parameter inside a class to something else (say “harry”). Try changing slf to “slf” or “harry” and see the effects.

from random import randint
class Train:
    def __init__(slf,trainNo):
        slf.trainNo = trainNo
    def book(slf,fro,to):
        print(f"Ticket is booked in train no : {slf.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train no : {slf.trainNo} is running on time")

    def getFare(slf,fro,to):
         print(f"Ticket is fare in train no : {slf.trainNo}\nfrom {fro} to {to} is : {randint(222,5567)}")
    
t = Train(345231)
t.book("Randnagar","Randipaga")
t.getFare("Randnagar","Randipaga")
t.getStatus()
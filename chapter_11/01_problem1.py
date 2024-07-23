#1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below:

# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

# name = input("Enter name : ")
# marks = int(input("Enter marks : "))
# phone = int(input("Enter phone number : "))

# s = "The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phone)
# print(s)

# 3.A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.


# table = [str(7*i) for i in range(1,11)]

# s = "\n".join(table)

# print(s)


# 4. Write a program to filter a list of numbers which are divisible by 5

# def divisibles5(n):
#     if(n%5 == 0):
#         return True
#     return False

# a = [1,2,3,5,345,3453,4565,56780,98760,45645,4560]

# f = list(filter(divisibles5,a))
# print(f)


# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

# from functools import reduce
# l = [1,2,3,5,345,3453,4565,56780,98760,45645,4560]

# def greater(a,b):
#     if(a>b):
#         return a
#     return b

# print(reduce(greater,l))


# 6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

# pip freeze > requriments.txt
# virtualenv Amitenv

#7. Explore the ‘Flask’ module and create a web server using Flask & Python. 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.run()
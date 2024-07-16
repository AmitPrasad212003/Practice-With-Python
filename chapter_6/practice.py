# age = int(input("Enter your age : "))
# if(age >= 18):
#     print("Yes")
# elif(0 < age < 18):
#     print("No")
# else:
#     print("Invalid age")


# 1. Write a program to find the greatest of four numbers entered by the user.


# a = int(input("Enter the numer a : "))
# b = int(input("Enter the numer b : "))
# c = int(input("Enter the numer c : "))
# d = int(input("Enter the numer d : "))

# if(a>=b and a>c and a>d):
#     print("A is greater",a)
# elif( b>c and b>d):
#     print("B is greater",b)
# elif( c>d):
#     print("c is greater",c)
# else:
#     print("D is greater ",d)

# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# marks1 = int(input("Enter Marks 1 : "))
# marks2 = int(input("Enter Marks 2 : "))
# marks3 = int(input("Enter Marks 3 : "))

# check for total percentage , assuming total marks of each subjects is 100

# total_percentage = (marks1+ marks2 + marks3)/3

# if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
#     print("You are pass : ",total_percentage)
# else:
#     print("You failed , Try againn next year! : ",total_percentage)

# 3. A spam comment is defined as a text containing following keywords:"Make a lot of money ", "buy now ", "subscribe this ", "click this ". Write a program to detect these spams.

# p1 = "Make a lot of money "
# p2 = "buy now"
# p3 = "subscribe this "
# p4 = "click this "

# message = input("Enter your comments : ")

# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("This comment is a spam")
# else:
#     print("This comment is not a spam")


# 4. Write a program to find whether a given username contains less than 10 characters or not.

# user_name = input("Enter Username : ")

# if(len(user_name) < 10):
#     print(f"Your {user_name} contains less than 10 characters ")
# else:
#     print(f"{user_name} : All is well !! Your {user_name} contains more than or equal to 10 characters ")


# 5. Write a program which finds out whether a given name is present in a list or not.
# l = ["Harry","Amit","Kundan","shashwat","saurav","farhan","sujata"]

# name = input("Enter your name : ")

# if(name in l):
#     print("Your name is in the List !")
# else:
#     print("Your name is not present in the List !")



# 6. Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

# marks = int(input("Enter your marks : "))

# if(marks <= 100 and marks >= 90):
#     grade = "EX"
# elif(marks < 90 and marks >= 80):
#     grade = "A"
# elif(marks < 80 and marks >= 70):
#     grade = "B"
# elif(marks <=70 and marks >= 60):
#     grade = "C"
# elif(marks < 60 and marks >= 50):
#     grade = "D"
# elif(marks < 50):
#     grade = "F"
# else:
#     print("GANDU")

# print("Grade : ",grade)

# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = "Hey Amit bhai is good amit is very good and Amit is great"

if("Amit".lower() in post.lower()):
    print("This post is talking about Amit")
else:
    print("This post is not talking about Amit")

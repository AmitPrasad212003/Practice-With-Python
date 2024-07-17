# 1. Write a program to print multiplication table of a given number using for loop.

# n = int(input("Enter your number : "))

# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")


# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for i in l:
#     if(i.startswith("S")):
#         print(f"Namaste {i}")

# 3. Attempt problem 1 using while loop.

# l = [1,2,"Amit", False,"THIS","Prasad","Sujata"]

# i = 0

# while(i < len(l)):
#     print(l[i])
#     i += 1

# another example

# n = int(input("Enter a number : "))

# i = 1
# while(i < 11):
#     print(f"{n} X {i} = {n*i}")
#     i += 1

# 4. Write a program to find whether a given number is prime or not

# n = int(input("Enter a number : "))

# for i in range(2,n):
#     if(n%i)== 0:
#         print(f"{n} is not prime")
#         break
# else:
#     print(f"{n} is prime")



# 5. Write a program to find the sum of first n natural numbers using while loop.

# n = int(input("Enter a number : "))
# sum = 0

# # for i in range(1,n+1):
# #     sum += i

# i = 1
# while(i<= n):
#     sum += i
#     i += 1

# print(f"Sum of n natural number : {sum}")

# 6. Write a program to calculate the factorial of a given number using for loop.

# n = int(input("ENter a number :"))
# product = 1
# for i in range(1,n+1):
#     product *= i

# print(f"Factorial of {n} is : {product}")

# 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

# n = int(input("ENter a number : "))

# for i in range(1,n+1):
#     print(" "*(n-i),end ="" )
#     print("*"*(2*i-1),end ="")
#     print()


# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

# n = int(input("ENter a number"))

# for i in range(1,n+1):
#     print("*"*i)

# 9. Write a program to print the following star pattern.
# * * *
# *   *  for n = 3
# * * *

# n = int(input("ENter a number : "))

# for i in range(1,n+1):
#     if(i == 1 or i == n):
#         print("*"*n)
#     else:
#         print("*",end = "")
#         print(" "* (n-2),end = "")
#         print("*",end = "")
#         print()


# 10. Write a program to print multiplication table of n using for loops in reversed order

n = int(input("ENter a number : "))

for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")
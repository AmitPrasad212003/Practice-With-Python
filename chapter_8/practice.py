# 1. Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return a;
    elif(b>a and b>c):
        return b;
    elif(c>a and c>b):
        return c;
    else:
        return "all are number are equal to eachother"
    
print(f"The greatest number is {greatest(2,2,2)}")


#2. Write a python program using function to convert Celsius to Fahrenheit.

def f_to_c(f):
    c = 5*(f-32)/9
    return c

f = int(input("Enter temperature in F : "))
print(f"The Temperature in c is : {round(f_to_c(f),2)} \u00B0C ")


# 3. How do you prevent a python print() function to print a new line at the end.

print("a")
print("b")
print("c ", end="")
print("d ", end="")
print()

# 4. Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if (n == 1):
        return 1;
    return n+sum(n-1)
n = int(input("Enter a number : "))
print(f"The sum of n natural number is : {sum(n)}")


# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *


def pattern(n):
    if(n==0):
        return
    print(" * "*n)
    pattern(n-1)
n = int(input("Enter a number : "))
print(pattern(n))


# 6. Write a python function which converts inches to cms.


def inch_to_cms(inch):
    return inch * 2.54;

n = int(input("Enter a number  in inches: "))
print(f"{n} inch == {inch_to_cms(n)} cm")


# 7. Write a python function to remove a given word from a list ad strip it at the same time.


def rem(l,word):
    n = []
    for item in l:
        # l.remove(word)
        # return l;
        if not(item == word):
            n.append(item.strip(word))
    return n
    

l = ["Harry","Rohan","Shubham", "an"]

print(rem(l,"an"))


# 8. Write a python function to print multiplication table of a given number.

def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

n = int(input("Enter a number"))
 
print(multiply(n))


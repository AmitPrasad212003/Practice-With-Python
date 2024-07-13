# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.

name = input("Enter your name : ")

print(f"Good afternoon {name}")

#2. Write a program to fill in a letter template given below with name and date.

letter = ''' 
        Dear <|Name|>,
        You are selected!
        <|Date|>'''

print(letter.replace("<|Name|>","Amit Prasad"))
print(letter.replace("<|Date|>","21/03/2030"))
print(letter.replace("<|Name|>","Amit Prasad").replace("<|Date|>","21/03/2030"))

# 3. Write a program to detect double space in a string.

name = "AMit is a coder  boy  and  and "
print(name.find("  "))

# 4. Replace the double space from problem 3 with single spaces

name = "AMit is a coder  boy  and  and "
print(name.replace("  "," "))

# 5. Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry,\n\tThis python course is nice.\n\tThanks!"

print(letter)

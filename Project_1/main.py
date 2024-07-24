import random



''' 
computer choice
1 for snake 
-1 for water
0 for gun

'''

print('''
choice "s" for Snake
       "w" for Water
       "g" for gun
      
''')

computer =  random.choice([-1, 0, 1])

youstr = input("Enter your choice : ")
youDict = {"s": 1,"w":-1, "g": 0}
you = youDict[youstr]

reverseDict = {1:"Snake",-1:"Water",0:"Gun"}

print(f"You chose : {reverseDict[you]} \nComputer choose : {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")
else:
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 1 and you == 1):
        print("You lose!")
    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    else:
        print("Something went worng!!")
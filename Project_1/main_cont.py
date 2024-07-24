import random



''' 
computer choice
1 for snake 
-1 for water
0 for gun

'''

while(True):
    print('''
    choice "s" for Snake
        "w" for Water
        "g" for gun
        "q" for Exit
    ''')

    youstr = input("Enter your choice : ")

    if("q" == youstr):
        break
    else:
        computer =  random.choice([-1, 0, 1])
        youDict = {"s": 1,"w":-1, "g": 0}
        you = youDict[youstr]

        reverseDict = {1:"Snake",-1:"Water",0:"Gun"}

        print(f"You chose : {reverseDict[you]} \nComputer choose : {reverseDict[computer]}")

        if(computer == you):
            print("Its a draw")
        else:
            if((computer - you) == -1 or (computer - you) == 2):
                print("You Lose!")
            else:
                print("You Win!!")
    


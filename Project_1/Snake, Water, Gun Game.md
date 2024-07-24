
# Snake, Water, Gun Game

## Introduction
This is a simple command-line game based on the classic "Rock, Paper, Scissors" game. In this version, the options are "Snake", "Water", and "Gun". The rules are:
- Snake drinks water (Snake wins)
- Gun shoots snake (Gun wins)
- Water douses gun (Water wins)

## How to Play
1. Run the script.
2. Follow the prompt to choose:
   - "s" for Snake
   - "w" for Water
   - "g" for Gun
   - "q" to Exit the game
3. The computer will randomly choose one of the three options.
4. The result will be displayed on the screen indicating if you won, lost, or if it was a draw.

## Code Explanation

### Imports
```python
import random
```
- **random**: This module is used to generate random choices for the computer.

### Main Game Loop
```python
while(True):
    print('''
    choice "s" for Snake
        "w" for Water
        "g" for Gun
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

        print(f"You chose : {reverseDict[you]} \nComputer chose : {reverseDict[computer]}")

        if(computer == you):
            print("It's a draw")
        else:
            if((computer - you) == -1 or (computer - you) == 2):
                print("You Lose!")
            else:
                print("You Win!!")
```

- **while(True)**: Creates an infinite loop to keep the game running until the user decides to exit.
- **User Input**: Prompts the user to enter their choice.
- **Exit Condition**: Breaks the loop if the user chooses to exit.
- **Computer Choice**: Uses `random.choice` to randomly select one of the three options.
- **Outcome Determination**: Compares the choices and prints the result.

## Modules Used
### `random`
- **Purpose**: To generate random selections for the computer.
- **Function Used**: `random.choice()`
  - **Description**: `random.choice(seq)` returns a randomly selected element from the non-empty sequence `seq`.
  - **Usage**: `computer = random.choice([-1, 0, 1])`

Enjoy playing the Snake, Water, Gun game!

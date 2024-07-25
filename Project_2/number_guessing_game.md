
# Number Guessing Game

This document explains a simple number guessing game implemented in Python. The program generates a random number between 1 and 100, and the user has to guess it. The program provides feedback on whether the guessed number is higher or lower than the generated number and counts the number of attempts made by the user.

## Code Explanation

### Importing the `randint` function from the `random` module
```python
from random import randint
```
The `randint` function is used to generate a random integer within a specified range.

### Generating a random number
```python
n = randint(1,100)
```
This line generates a random integer between 1 and 100 and assigns it to the variable `n`.

### Initializing variables
```python
a = -1
guesses = 0
```
The variable `a` is initialized to -1 (a value outside the possible range of the random number), and `guesses` is initialized to 0 to count the number of attempts.

### Starting the guessing loop
```python
while(a != n):
```
This loop will continue running until the user guesses the correct number (`a` equals `n`).

### Counting guesses and taking user input
```python
guesses += 1
a = int(input("Guess a number : "))
```
Each iteration increments the `guesses` counter and takes user input, converting it to an integer.

### Providing feedback
```python
if(a > n):
    print("Lower number please ")
    guesses += 1
elif(a < n):
    print("Higher number please")
    guesses += 1
```
Based on the user's guess, the program informs whether the guessed number is too high or too low and increments the `guesses` counter again (note: this results in an extra increment, which may not be necessary).

### Ending the game
```python
print(f"You have guessed the number {n} correctly in {guesses} attempt")
```
Once the correct number is guessed, the program prints a congratulatory message along with the number of attempts made.

## Modules and Functions

- **`random` module**: The `random` module implements pseudo-random number generators for various distributions. It provides several functions to generate random numbers.
  - **`randint(a, b)`**: Returns a random integer `N` such that `a <= N <= b`.

## Example Usage

```python
from random import randint

# Generate a random number between 1 and 100
n = randint(1, 100)
a = -1
guesses = 0

while a != n:
    guesses += 1
    a = int(input("Guess a number: "))
    if a > n:
        print("Lower number please")
    elif a < n:
        print("Higher number please")

print(f"You have guessed the number {n} correctly in {guesses} attempt")
```

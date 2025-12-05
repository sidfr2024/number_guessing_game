# number_guessing_game
This Python program is a simple command-line Number Guessing Game. The computer randomly selects a number between 1 and 100, and the user must guess it. After each guess, the program provides hints such as “Too low” or “Too high” until the user correctly identifies the number.
# Number Guessing Game – Python

This project is a simple number guessing game implemented in Python. The computer selects a random number between 1 and 100, and the player must guess the correct number. The program gives helpful hints to guide the player and counts how many attempts are made.

---

## Features

- Random number generation using the `random` module  
- User input validation to ensure only integers are accepted  
- Hints provided after each guess:  
  - "Too low"  
  - "Too high"  
- Ensures the guess is within the valid range (1 to 100)  
- Displays the total number of attempts after the correct guess  

---

## How the Game Works

1. The program generates a random number between 1 and 100.  
2. The user is repeatedly prompted to enter a guess.  
3. After each guess, the program responds with guidance:  
   - If the guess is too low  
   - If the guess is too high  
   - If the guess is correct  
4. Invalid inputs automatically trigger an error message.  
5. When the player guesses correctly, the game ends and displays the attempt count.

---

## Code Overview

```python
import random

def number_guessing_game():
    print("Welcome to the number guessing game!!")
    print("I'm thinking of a number. Guess it if you can!")

    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_input = int(input("Enter your guess: "))
            guess = int(user_input)
            attempts += 1

            if guess < 1 or guess > 100:
                print("Choose a number between 1 and 100")
                continue
            elif guess < target_number:
                print("Too low!!")
            elif guess > target_number:
                print("Too high!!")
            else:
                print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()
How to Run
Install Python 3.

Save the script as number_guessing_game.py.

Open a terminal and run:

nginx
Copy code
python number_guessing_game.py
Follow the on-screen instructions to play.

Learning Objectives
This project helps learners understand:

Random number generation in Python

Basic input handling

Error handling using try-except

Logical conditions and loops

Creating simple interactive CLI programs

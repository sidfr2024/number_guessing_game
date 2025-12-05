import random

def number_guessing_game():
    print("Welcome to the number guessing game!!")
    print("I'm thinking of a number. Guess it if you can!")

    target_number= random.randint(1,100)
    attempts=0

    while True:
        try:
            user_input=int(input("Enter your guess:"))
            guess=int(user_input)
            attempts+=1

            if guess <1 or guess >100:
                print("Choose between a number between 1 to 100 ")
                continue
            elif guess < target_number:
                print("Too low!!")

            elif guess> target_number:
                print("Too high!!")

            else:
                print(f"Congratulations!You guessed the number {target_number} in {attempts} attempt. ")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    number_guessing_game()
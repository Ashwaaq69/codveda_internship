# Task_2_Number_Guessing_Game

import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Guess a number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
        
        
if __name__ == "__main__":
    number_guessing_game()
        
        
   
    
    
    
    
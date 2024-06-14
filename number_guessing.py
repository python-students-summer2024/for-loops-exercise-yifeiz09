"""
This file contains an incomplete function definition.  
Your task is to complete the incomplete function definition. so that it behaves as indicated in the documentation.

Do not run this file directly.
Rather, call this function from main.py and run that file.
"""

import random
def guess_number(low, high, num_attempts):
    """
    This function, named 'guess_number', generates a psudo-random integer in a given range, inclusive.
    The user is given a certain number of attempts to guess the correct number.
    The function prints the range to the user and informs the user of how many attempts they have.
    The function asks the user to guess the number the given number of times.
    You must use the random module's randint function to generate the pseudo-random integer.
    You must use a for loop to give the user multiple attempts.
    If the user enters a non-numeric response, the program must not crash, but simply count that as an incorrect answer.
    If the user guesses any attempt correctly, the function immediately exits the loop and returns True.
    If the user enters all attempts incorrectly, the function returns False.

    :param low: The low end of the range in which the pseudo-random number is generated.
    :param high: the high end of the range in which the pseudo-random number is generated.
    :param num_attempts: The number of attempts the user is given to guess the correct number.
    :returns: True if the user answers any attempt correctly, False otherwise.
    """
    correct_number = random.randint(low, high)
    
    print(f"Guess the number between {low} and {high}.")
    print(f"You have {num_attempts} attempts.")
    
    for attempt in range(num_attempts):
        user_input = input(f"Attempt {attempt + 1}: ")
        
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        
        if guess == correct_number:
            print("Congratulations! You guessed the correct number.")
            return True
        
        if guess < correct_number:
            print("Too low!")
        else:
            print("Too high!")
    
    print(f"Sorry, you've used all your attempts. The correct number was {correct_number}.")
    return False

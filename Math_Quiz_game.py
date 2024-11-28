# This program is a math quiz game. It allows the user to choose a level of difficulty (1, 2, or 3), 
# generates ten addition problems based on the chosen level, and quizzes the user on these problems. 
# The user has up to three attempts to answer each problem correctly. At the end, the program displays 
# the user's score out of 10.

import random

def choose_difficulty():
    """Prompt the user to choose a difficulty level (1, 2, or 3).
    Keeps asking until a valid input is provided."""
    while True:
        try:
            # Ask the user for the game level
            difficulty_level = int(input("Level (1, 2, or 3): "))
            # Check if the input is valid
            if difficulty_level in [1, 2, 3]:
                return difficulty_level
        except ValueError:
            # Ignore invalid inputs that can't be converted to an integer
            pass
        print("Invalid level. Please enter 1, 2, or 3.")

def create_math_problem(difficulty_level):
    """Generate two random numbers (X and Y) for an addition problem.
    The numbers have a digit count based on the chosen level."""
    n = difficulty_level  # Number of digits corresponds to the level
    # Calculate the range of numbers for the chosen level
    lower_limit = 10**(n - 1) if n > 1 else 0  # Minimum value for n digits
    upper_limit = 10**n - 1  # Maximum value for n digits
    # Generate random numbers within the range
    x = random.randint(lower_limit, upper_limit)
    y = random.randint(lower_limit, upper_limit)
    return x, y

def quiz_user(x, y):
    """Prompt the user to solve the given addition problem (X + Y).
    The user gets up to three tries to answer correctly."""
    for _ in range(3):  # Allow up to three attempts
        try:
            # Ask the user for their answer to the addition problem
            answer = int(input(f"{x} + {y} = "))
            # Check if the answer is correct
            if answer == x + y:
                return True  # Return True if the answer is correct
            else:
                print("EEE")  # Let the user know their answer is wrong
        except ValueError:
            # Handle cases where the user enters a non-numeric input
            print("EEE")
    # If all attempts fail, show the correct answer
    print(f"The correct answer is {x + y}")
    return False  # Return False if the user didn't get the correct answer

def main():
    """Main function to run the math quiz game."""
    # Get the difficulty level from the user
    difficulty_level = choose_difficulty()
    score = 0  # Initialize the user's score to 0

    # Loop to generate and ask 10 problems
    for _ in range(10):
        # Generate a math problem
        x, y = create_math_problem(difficulty_level)
        # Ask the user to solve the problem and update the score if correct
        if quiz_user(x, y):
            score += 1

    # Display the user's final score
    print(f"Score: {score}/10")

# Entry point of the program
if __name__ == "__main__":
    main()

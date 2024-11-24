import random  # This imports the random library to help us pick a random word
import string  # This imports the string library, which gives us a list of all letters

# Function to load words from the words.txt file
def load_words(filename):
    with open(filename, 'r') as file:  # Open the file in read mode
        words = file.readlines()  # Read all lines in the file and save them in a list
    return [word.strip().lower() for word in words]  # Clean the words (remove extra spaces and make them lowercase)

# Function to pick a random word from the list of words
def choose_word(word_list):
    return random.choice(word_list)  # Randomly choose a word from the list

# Function to check if the player has guessed the entire word correctly
def is_word_guessed(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)  # Check if all letters in the word have been guessed

# Function to show the current state of the word with guessed letters
def get_guessed_word(secret_word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '-' for letter in secret_word)  # Show guessed letters, '-' for not guessed

# Function to show the letters that the player hasn't guessed yet
def get_available_letters(guessed_letters):
    return ''.join([letter for letter in string.ascii_lowercase if letter not in guessed_letters])  # Letters not guessed yet

# Main game function
def hangman():
    # Load words and pick a random secret word
    word_list = load_words("C:\\Users\\user\\Desktop\\words.txt")  # Get the list of words from the file
    secret_word = choose_word(word_list)  # Pick a random word from the list
    unique_letters = len(set(secret_word))  # Count how many different letters are in the word (to calculate score later)

    guesses = 10  # The player starts with 10 guesses
    warnings = 3  # The player starts with 3 warnings
    guessed_letters = []  # List to keep track of the letters the player has already guessed

    print("Welcome to Hangman!")
    print(f"The secret word has {len(secret_word)} letters.")
    
    while guesses > 0:  # The game continues as long as the player has guesses left
        print("-" * 20)  # Just a separator line for better readability
        print(f"Guesses remaining: {guesses}")
        print(f"Warnings remaining: {warnings}")
        print(f"Available letters: {get_available_letters(guessed_letters)}")  # Show letters the player can still guess
        print(f"Word so far: {get_guessed_word(secret_word, guessed_letters)}")  # Show the word with guessed letters and '-' for the rest

        # Ask the player to guess a letter
        guess = input("Please guess a letter: ").lower()  # Get the player's guess and make it lowercase

        # Check if the guess is a valid letter
        if not guess.isalpha():  # If the guess is not a letter
            if warnings > 0:  # If the player has warnings left
                warnings -= 1  # They lose one warning
                print(f"Invalid input! You have {warnings} warning(s) left.")  
            else:  # If no warnings left, they lose a guess instead
                guesses -= 1
                print("Invalid input! You lost a guess.")
            continue  # Go back to the start of the loop and ask for another input

        # If the guess was already made, warn the player
        if guess in guessed_letters:  
            if warnings > 0:  # If warnings are left, they lose a warning
                warnings -= 1
                print(f"You've already guessed that letter! You have {warnings} warning(s) left.")
            else:  # If no warnings left, they lose a guess
                guesses -= 1
                print("You've already guessed that letter! You lost a guess.")
            continue  # Go back to the start and ask for a new guess

        guessed_letters.append(guess)  # Add the guess to the list of guessed letters

        # If the letter is in the word, tell the player it was a correct guess
        if guess in secret_word:
            print("Good guess!")
        else:
            # Vowels (a, e, i, o, u) cost 2 guesses
            if guess in 'aeiou':  
                guesses -= 2
                print(f"Oops! '{guess}' is a vowel and not in the word. You lost 2 guesses.")
            else:  # Consonants cost 1 guess
                guesses -= 1
                print(f"Oops! '{guess}' is not in the word. You lost 1 guess.")

        # Check if the player has won by guessing all letters
        if is_word_guessed(secret_word, guessed_letters):
            print("-" * 20)
            print(f"Congratulations! You guessed the word '{secret_word}'.")
            score = guesses * unique_letters  # Calculate score based on remaining guesses and unique letters
            print(f"Your score is: {score}")
            break  # End the game if the word is guessed correctly

    # If the player runs out of guesses, they lose
    if guesses <= 0:
        print("-" * 20)
        print(f"Sorry, you've run out of guesses. The word was '{secret_word}'.")

# Start the game
hangman()
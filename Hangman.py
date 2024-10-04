import random

# Stage 1: Define the hangman stages as a list of strings
Stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''  
  +---+
  |   |
      |
      |
      |
      |
========='''
]

# Stage 2: List of words to choose from
word_list = ["akdura", "apple", "camel"]

# Stage 3: Initialize the number of lives the player has
lives = 6

# Stage 4: Randomly select a word from the word list
chosen_word = random.choice(word_list)
print(chosen_word)  # Debug: print the chosen word

# Stage 5: Create a placeholder for the word with underscores
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)  # Display the initial placeholder

# Stage 6: Initialize game state variables
game_over = False
correct_letters = []

# Stage 7: Main game loop
while not game_over:
    # Stage 7.1: Get user input for their guess
    guess = input("Guess a letter: ").lower()

    # Stage 7.2: Prepare the display string for the current state of the word
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter  # If the guess is correct, show the letter
            correct_letters.append(guess)  # Add the guess to the list of correct letters
        elif letter in correct_letters:
            display += letter  # If already guessed, show the letter
        else:
            display += "_"  # Otherwise, show an underscore for unguessed letters

    print(display)  # Show the current state of the guessed word

    # Stage 7.3: Check if the guess was incorrect
    if guess not in chosen_word:
        lives -= 1  # Decrease lives if the guess is incorrect
        if lives == 0:
            game_over = True  # End the game if no lives are left
            print("You lose")  # Inform the player they have lost

    # Stage 7.4: Check for a win condition
    if "_" not in display:
        game_over = True  # End the game if the player has guessed the word
        print("You win")  # Inform the player they have won

    # Stage 7.5: Display the current hangman stage based on remaining lives
    print(Stages[lives])  # Show the appropriate hangman stage


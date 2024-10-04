import random
word_list =["akdura" , "apple" , "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a word: ").lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("wrong")

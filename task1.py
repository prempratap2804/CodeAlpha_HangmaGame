# hangman game
import random

words = ["apple", "banana", "grapes", "orange", "mango"]


word = random.choice(words)


guessed_word = ["_"] * len(word)


attempts = 6

guessed_letters = []

print(" Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", guessed_letters)
    print("Remaining Attempts:", attempts)

    guess = input("Enter a letter: ").lower()

  
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue


    guessed_letters.append(guess)

   
    if guess in word:
        print(" Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print(" Wrong guess!")
        attempts -= 1

# Final result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\n Game Over! The word was:", word)

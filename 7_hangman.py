#!/usr/bin/python3
import random
import hangman_wordlist
import hangman_logo
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(hangman_logo.logo)
chosen_word = random.choice(hangman_wordlist.word_list)
display = []
for ch in chosen_word:
    display += "_" 
lenght = len(chosen_word)
lives = 6
print(f"pssst, the solution is {chosen_word}.")
already_guessed = ""
end = False
while end == False:
    guess = input("Guess a letter: ").lower()
    if guess in already_guessed:
        print(f"You have guessed letter {guess}")
        continue
    already_guessed += guess
    for ch in range(0, lenght):
        if guess == chosen_word[ch]:
            display[ch] = chosen_word[ch]
    if guess not in chosen_word:
        print(f"You guessed {guess}, {guess} is not in the word. You lose a life")
        lives -= 1
        print(stages[lives])
    print(f"{' '.join(display)}")
    if "_" not in display:
        end = True
        print("You Win")
    elif lives == 0:
        end = True
        print("You lose")

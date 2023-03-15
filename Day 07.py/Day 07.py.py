import replit
import random


end_of_game = False
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
from hangman_art import logo, stages
print(logo)

empty_list = []

for b in chosen_word:
  empty_list.append("_")



end_of_game = False
while not end_of_game:
  i = 0
  guess = input("Guess a letter: ").lower()
  replit.clear()
  if guess in empty_list:
    print(f"You already guessed {guess}")
  for letter in chosen_word:
    if letter == guess:
      empty_list[i] = guess
      i = i + 1
    else:
      i = i + 1
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life")
    lives = lives - 1
    if lives == 0:
      end_of_game = True
      print("You lose")
      
  print(f"{' '.join(empty_list)}")
  #print(lives)
  if "_" not in empty_list:
    end_of_game = True
    print("You Win")
  
  print(stages[lives])

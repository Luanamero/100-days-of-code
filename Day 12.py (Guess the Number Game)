import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
n = random.randint(1, 100)
game_type = input("Choose a difficulty. Type 'easy' or 'hard': ")

if game_type == 'easy':
  i = 10
elif game_type == 'hard':
  i = 5



def game(ig):
  print(f"You have {ig} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess > n:
    print("Too high.")
    if ig != 1:
      print("Guess again.")
    else:
      print("You've run out of guesses, you lose.")
    return(ig - 1)
  elif guess < n:
    print("Too low.")
    if ig != 1:
      print("Guess again.")
    else:
      print("You've run out of guesses, you lose.")
    return(ig - 1)
  else:
    print(f"You got it! The answer was {n}")
    return(0)

i = game(i)
while i != 0:
  i = game(i)



  

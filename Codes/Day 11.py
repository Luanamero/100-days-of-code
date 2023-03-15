import random
from replit import clear
in_game = True
yes_another_card = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game = input("Do you want to play blackjack? type 'y' or 'n': ")

while in_game:
  if game == 'y':
    yc1 = random.choice(cards)
    yc2 = random.choice(cards)
    cc1 = random.choice(cards)
    cc2 = random.choice(cards)
  
    your_score = yc1 + yc2
    computer_score = cc1 + cc2
    your_list = []
    your_list.append(yc1)
    your_list.append(yc2)
    computer_list= []
    computer_list.append(cc1)
    computer_list.append(cc2)   

    if your_score == 21:
          print(f"Your final hand: {your_list}, final score = {your_score}")
          print(f"Computer's final hand: {cc1} and {cc2}, final score: {computer_score}")
          print("You win")
    else:
      print(f"Your cards are: {your_list}, current score = {your_score}")
      print(f"Computer's first card: {cc1}")
    
    
    
    while yes_another_card: 
      another_card = input("Type 'y' to get another card or 'n': ")
      if another_card == 'y':
        yc3 = random.choice(cards)
        your_score = your_score + yc3
        your_list.append(yc3)
        
        if your_score == 21:
          print(f"Your final hand: {your_list}, final score = {your_score}")
          print(f"Computer's final hand: {cc1} and {cc2}, final score: {computer_score}")
          print("You win")
          yes_another_card = False
        if your_score > computer_score and your_score > 21:
          print(f"Your final hand: {your_list}, final score = {your_score}")
          print(f"Computer's final hand: {cc1} and {cc2}, final score: {computer_score}")
          print("You Lose")
          yes_another_card = False
        else: 
          print(f"Your cards are: {your_list}, current score = {your_score}")
          print(f"Computer's first card: {cc1}")
      if another_card == 'n':
        yes_another_card = False
        
        
    
    if your_score == computer_score:
      print(f"Your final hand: {your_list}, final score = {your_score}")
      print(f"Computer's final hand: {cc1} and {cc2}, final score: {computer_score}")
      print("It's a tie")
    if your_score > computer_score and your_score < 21:
      print(f"Your final hand: {your_list}, final score = {your_score}")
      print(f"Computer's final hand: {cc1} and {cc2}, final score: {computer_score}")
      print("You Win")
    if your_score < computer_score and computer_score <21:
      print(f"Your final hand: {your_list}, final score = {your_score}")
      print(f"Computer's final hand: {cc1} and {cc2}, final score: {computer_score}")
      print("You Lose")
    if your_score < computer_score and computer_score > 21:
      print(f"Your final hand: {your_list}, final score = {your_score}")
      print(f"Computer's final hand: {cc1} and {cc2}, final score: {computer_score}")
      print("You Win")


    
  game = input("Do you want to play blackjack? type 'y' or 'n': ")
  if game == 'y':
    in_game = True
    yes_another_card = True
    clear()
    
  else:
    in_game = False
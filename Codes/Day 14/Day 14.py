#Higher Lower Game
from game_data import data
import random
from replit import clear
print("Welcome to the Higher Lower Game!\n")
in_game = True
score = 0

  
def a_value():
  random_person = random.randint(0, 49)
  choosen_a = data[random_person]
  return choosen_a

def b_value():
  random_person2 = random.randint(0, 49)
  choosen_b = data[random_person2]
  return choosen_b

a = a_value()
b = b_value()


while in_game:
  is_the_same = True
  if a == b:
    random_person2 = random.randint(0, 49)
    b = data[random_person2]
  
  
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}\n")  
  
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}\n")
  choice = input("Who has more followers? Type 'a' or 'b': \n")
  
  if choice == "a" and a['follower_count'] > b['follower_count']:
    score += 1
    print(f"You are right! Your score is: {score}\n")
    a = b
    b = b_value()
    clear()
     
      
  elif choice == "a" and a['follower_count'] < b['follower_count']:
    print(f"You were wrong! Your score is: {score}")
    in_game = False
  
  
  elif choice == "b" and a['follower_count'] < b['follower_count']:
    score = score + 1
    print(f"You are right! Your score is: {score}\n")
    b = a
    a = a_value()
    clear()
    
      
  elif choice == "b" and a['follower_count'] > b['follower_count']:
    print(f"You were wrong! Your score is: {score}")
    in_game = False
  
  
      
  
  
  
  
  

  
  


  

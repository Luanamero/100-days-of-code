rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
draw = [rock, paper, scissors]

user_choise = int(input("What do you choose? type 0 for rock, 1 for paper or 2 for scissors\n"))

computer_choise = random.randint(0, 2)
if user_choise == computer_choise:
  print(f"Your choice:\n {draw[user_choise]}")
  print(f"computer choice:\n {draw[computer_choise]}")
  print("It was a tie")
elif user_choise == 0 and computer_choise == 1:
  print(f"Your choice:\n {draw[user_choise]}")
  print(f"computer choice:\n {draw[computer_choise]}")
  print("The computer won")
elif user_choise == 0 and computer_choise == 2:
  print(f"Your choice:\n {draw[user_choise]}")
  print(f"computer choice:\n {draw[computer_choise]}")
  print("You won")
elif user_choise == 1 and computer_choise == 0:
  print(f"Your choise:\n {draw[user_choise]}")
  print(f"computer choise:\n {draw[computer_choise]}")
  print("You won")
elif user_choise == 1 and computer_choise == 2:
  print(f"Your choice:\n {draw[user_choise]}")
  print(f"computer choice:\n {draw[computer_choise]}")
  print("The computer won")
elif user_choise == 2 and computer_choise == 0:
  print(f"Your choice:\n {draw[user_choise]}")
  print(f"computer choice:\n {draw[computer_choise]}")
  print("The computer won")
elif user_choise == 2 and computer_choise == 1:
  print(f"Your choice:\n {draw[user_choise]}")
  print(f"computer choice:\n {draw[computer_choise]}")
  print("You won")
elif user_choise > 2:
  print("You cant use this number")

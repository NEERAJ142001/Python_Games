import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"ROCK"
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"PAPER"
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"SCISSOR"
'''
items = [rock, paper, scissors]
# user input
user_input = int(input("What do you choose? "
                       "Type 0 for Rock,"
                       " 1 for Paper or"
                       " 2 for Scissors.\n"))
# computer input
computer_choice = random.randint(0, 2)
# printing computer choice
print("Computer chose:")
print(items[computer_choice])
# printing user choice
print("Your choice")
print(items[user_input])
while True:
    if user_input >= 3 or user_input < 0:
        print("You typed an invalid number, you lose!")
    # rock and scissor
    elif user_input == 0 and computer_choice == 2:
        print("You win!")
    # user input =scissor and computer choice=rock win (rock)computer
    elif computer_choice == 0 and user_input == 2:
        print("You lose")
    # paper and scissor
    elif computer_choice == 2 and user_input == 1:
        print("You lose")
    elif computer_choice == 1 and user_input == 2:
        print("You win!")
    # rock and paper
    elif computer_choice == 1 and user_input == 0:
        print("You lose")
    elif computer_choice == 0 and user_input == 1:
        print("You win!")
    elif computer_choice == user_input:
        print("It's a draw")

    choice = input("You wanna play again yes/no : ")
    if choice == "yes" or choice == "Yes" or choice == "Yes" or choice == "y":
        continue
    elif choice == "NO" or choice == "no" or choice == "n":
        break

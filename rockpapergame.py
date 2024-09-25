import random

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
mine_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if mine_choice >= 3 or mine_choice < 0:
    print("You typed an invalid number. Game over!")
else:
    if mine_choice == 0:
        print(rock)
    elif mine_choice == 1:
        print(paper)
    else:
        print(scissors)

    print("computer choose")
    computer_choice = int(random.randint(0,2))
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)

    if mine_choice - computer_choice == 0:
        print("It is a draw")
    elif mine_choice - computer_choice == 2 or mine_choice - computer_choice == -1:
        print("You lose")
    else:
        print("You win")
        
#!/usr/bin/python3
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
game_images = [rock, paper, scissors]
response = input("What do you choose? Type 0 for rock, 1 for Paper or 2 for scissors\n")
response = int(response)

if response > 2 or response < 0:
	print("Invalid")
else:
	print(game_images[response])
	ran = random.randint(0, 2)
	print("Computer chose")
	if ran == 0:
		print(rock)
	elif ran == 1:
		print(paper)
	elif ran == 2:
		print(scissors)

	if response == ran:
		print("It's a draw")
	elif response == 0 and ran == 1:
		print("You Lose")
	elif response == 0 and ran == 2:
		print("You Win")
	elif response == 1 and ran == 0:
		print("You Win")
	elif response == 1 and ran == 2:
		print("You Lose")
	elif response == 2 and ran == 0:
		print("You Lose")
	elif response == 2 and ran == 1:
		print("You Win")

import random

player1 = input("enter player1 choice: ")
player2 = None

ran = random.randint(0, 2)
if ran == 0:
	player2 = 'rock'
	print("com plays "+ player2)
elif ran == 1:
	player2 = 'paper'
	print("com plays "+ player2)
else:
	player2 = 'scissor'
	print("com plays "+ player2)

if player1 == 'rock':
	if player2 == 'scissor':
		print("Shoot! player1 wins")
	elif player2 == 'paper':
		print("Shoot! player2 wins")
elif player1 == 'paper':
	if player2 == 'scissor':
		print("Shoot! player2 wins")
	elif player2 == 'rock':
		print("Shoot! player1 wins")
elif player1 == 'scissor':
	if player2 == 'paper':
		print("Shoot! player2 wins")
	elif player2 == 'rock':
		print("Shoot! player1 wins")

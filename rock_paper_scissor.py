import random

score_player1 = 0
score_player2 = 0

while score_player1 <= 2 and score_player2 <= 2:	
	print("************************\n************************\n************************")
	
	print(f"Your score = {score_player1}\nComputer Score = {score_player2}")

	print("")

	print("Here we go again!!!!!")

	player1 = input("Please enter your move: ")
	player1 = player1.lower()
	player2 = None

	ran = random.randint(0, 2)
	
	if ran == 0:
		player2 = 'rock'
		print("Computer plays "+ player2)
	elif ran == 1:
		player2 = 'paper'
		print("Computer plays "+ player2)
	else:
		player2 = 'scissor'
		print("Computer plays "+ player2)

	print("")

	if player1 == 'rock':
		if player2 == 'scissor':
			print("You win!!!!!!")
			score_player1 += 1
		elif player2 == 'paper':
			print("Shoot! Computer wins")
			score_player2 += 1
		else:
			print("It's a tie")
	elif player1 == 'paper':
		if player2 == 'scissor':
			print("Shoot! Computer wins")
			score_player2 += 1
		elif player2 == 'rock':
			print("You win!!!!!!")
			score_player1 += 1
		else:
			print("It's a tie")
	elif player1 == 'scissor':
		if player2 == 'paper':
			print("Shoot! Computer wins")
			score_player2 += 1
		elif player2 == 'rock':
			print("You win!!!!!!")
			score_player1 += 1
		else:
			print("It's a tie")		
	else: 
		print("Please enter a valid move")

if score_player2 == 3:
	print("Oops! Sorry, Computer wins")
else:
	print("Yay! You win")
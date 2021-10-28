import random

score_player1 = 0
score_player2 = 0

while score_player1 <= 2 and score_player2 <= 2:	#you get to play until one of the player wins three times
	print("************************\n************************\n************************")
	
	print(f"Your score = {score_player1}\nComputer Score = {score_player2}") #prints the scores

	print("")

	print("Here we go again!!!!!")

	player1 = input("Please enter your move: ")    #player playes his/her move
	player1 = player1.lower()     #turns the player move to all lower case
	player2 = None

	ran = random.randint(0, 2)     #we generate a random number(0-2) for the computer to play his move
				       #here 0 is rock, 1 is paper and 2 is scissor
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
	#this is where we check who wins or loses and if it's a tie or not
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
#shows who wins the game
if score_player2 == 3:
	print("Oops! Sorry, Computer wins")
else:
	print("Yay! You win")

#my Tic Tac Toe game
board = ['0','1','2', '3','4','5','6','7','8']
turn = True #true for X and false for O
gameWon = False
winner=[] #If you keep it as a variable you cant assign this values inside a function without using global. Workaround-> use  a mutable structure like list

def print_board(board):
	print()
	print('		'+board[0] +'  ||  ' + board[1] +'  ||  ' + board[2] )
	print('		=================')
	print('		'+board[3] +'  ||  ' + board[4] +'  ||  ' + board[5] )
	print('		=================')
	print('		'+board[6] +'  ||  ' + board[7] +'  ||  ' + board[8] )
	print()
	
def game_prompt(turn):
	if turn == True:
		print("Turn for Player 1. Enter number where you wish to place X: ")
	else:
		print("Turn for Player 2. Enter number where you wish to place 0: ")

def fillboard(pchoice,turn):
	if turn == True:
		board[pchoice] = 'X'
	else:
		board[pchoice] = 'O'

def checkwin(board,turn):
	val = ''
	if turn == True:
		val='X'
	else:
		val='O'
	if (board[0] == board[1] == board[2] == val):
		winner.append(val)
		return True	
	if (board[3] == board[4] == board[5] == val):
		winner.append(val)
		return True	
	if (board[6] == board[7] == board[8] == val):
		winner.append(val)
		return True	
	if (board[0] == board[3] == board[6] == val):
		winner.append(val)
		return True	
	if (board[1] == board[4] == board[7] == val):
		winner.append(val)
		return True	
	if (board[2] == board[5] == board[8] == val):
		winner.append(val)
		return True	
	if (board[0] == board[4] == board[8] == val):
		winner.append(val)
		return True	
	if (board[2] == board[4] == board[6] == val):
		winner.append(val)
		return True	
	return False			

def declare_winner(winner):
	if winner[0] =='X':
		print('''
		========================================
		***** Congrats Player 1! You WIN!! ***** 
		========================================
			''')
	elif winner[0] =='O':
		print('''
		========================================
		***** Congrats Player 2! You WIN!! ***** 
		========================================
				''')
	
def sanitizeInput():
	properinput = False
	while properinput != True:
		try:
			pchoice = int(input("Your choice: "))
			if pchoice>8 or pchoice< 0:
				print("Enter a number from 0 to 8 which corresponds to a position on the board!")
				continue							
		except ValueError:
			print('Enter a single interger!')			
		properinput= True	
	return pchoice	

print(
		''' 
		***** WELCOME TO Tic Tac Toe v0.1 ***** 
		=======================================
		***** Get 3 in a line to win!!	  ***** 
		=======================================
		***** Player 1: X   Player 2: 0	  ***** 
		=======================================
		'''
	)
print_board(board)

while gameWon !=True:
	game_prompt(turn)
	pchoice = sanitizeInput()	
	#game logic
	fillboard(pchoice,turn)
	print_board(board)	
	gameWon = checkwin(board,turn) #check for game win
	turn = not turn #flip boolean, change the turn

declare_winner(winner)


#A basic hangman game.

import random
#dict with keys as movie name and values as a list of clues.
movie_db={'Inception' : ['Sci fi movie','Directed by Chirstopher Nolan'],
			'Spiderman' : ['Superhero movie','Features a friendly neighbourhood guy'],
			'Home Alone' : ['Kids movie']
		}

gameOver= False
themovie = random.choice(list(movie_db.keys()))
mlist= list(themovie)
print(mlist)
mcount= len(mlist)
guesses=7
inputclist=[]
def printchars(cguess):
	dispstr=[] #str as a list where items will be added and then joined at the end
	inputclist.append(cguess)
	for i in range(mcount):
		if mlist[i] not in inputclist:
			dispstr.append('_')
		else:
			dispstr.append(mlist[i])
	s=' '.join([str(x) for x in dispstr])		
	print(s)
	s2=''.join([str(x) for x in dispstr])
	mstr=''.join([str(j) for j in mlist])	
	if s2==mstr:
		global gameOver
		gameOver=True
		print(gameOver)

print(
		''' 
		***** WELCOME TO HANGMAN v0.1 ***** 
		===================================
		***** GUESS THE MOVIE ***** 
		===================================
		'''
	)



while guesses!=0:
	if gameOver == True:
		print("Congrats you guessed it correctly!! You WON!!")
		exit()
	print("You have "+str(guesses)+" guesses remaining!")
	
	char_guess = input("Enter a character: ")
	
	if char_guess in mlist:
		print("Correct!")
		printchars(char_guess)
	else:
		print("Wrong guess! Try again")
		guesses -=1
		continue 
	
print("You couldnt guess the movie. Play again?")


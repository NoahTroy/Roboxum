# # # # #
# Notes for future improvements/ideas:
# Allow for different charsets to be added, so that this game
# can be used to for many other languages.
#
# Add different template options. I.E. one that gives a wordlist, one that gives
# a name/date field, one that provides lines for people to write their found words
# on, a combination of the above, etc.
#
# Allow an answer key to be printed.
#
# On the GUI, allow them to create multiple different versions of the puzzle if they wish.
#
# Add support for rectangular boards.
#
# Add a puzzle generation progress bar.
#
# Add the ability to save past-generated puzzles.
#
# MAKE SURE TO RESET THE GLOBAL VARIABLES, OR TERMINATE THE CODE AFTER GENERATING THE BOARDS, OTHERWISE ERRORS WILL HAPPEN!
# # # # #

#Make all necessary imports:
import random , time , threading , queue
from tkinter import *
from PIL import Image

#Declare any necessary global variables:
letters = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
words = []
wordsDisplayed = '1.)\tDEFAULT'
boardDimensions = []
board = []
boards = []


#Define a function that identifies and returns all possible valid "next moves":
def nextValidLocation(currentBoard , letter , y = 0 , x = 0):
	validMoves = []
	upFine = False
	downFine = False
	rightFine = False
	leftFine = False

	#Move Up One Square:
	if (y > 0):
		upFine = True
		if ((currentBoard[(y - 1)][x] == letter) or (currentBoard[(y - 1)][x] == 'ebce1dd2d40aec3')):
			validMoves.append([(y - 1) , x])
	#Move Down One Square:
	if (y < (len(currentBoard) - 1)):
		downFine = True
		if ((currentBoard[(y + 1)][x] == letter) or (currentBoard[(y + 1)][x] == 'ebce1dd2d40aec3')):
			validMoves.append([(y + 1) , x])
	#Move Right One Square:
	if (x < (len(currentBoard[y]) - 1)):
		rightFine = True
		if ((currentBoard[y][(x + 1)] == letter) or (currentBoard[y][(x + 1)] == 'ebce1dd2d40aec3')):
			validMoves.append([y , (x + 1)])
	#Move Left One Square:
	if (x > 0):
		leftFine = True
		if ((currentBoard[y][(x - 1)] == letter) or (currentBoard[y][(x - 1)] == 'ebce1dd2d40aec3')):
			validMoves.append([y , (x - 1)])

	#Move Diagonally Up and to the Left:
	if (upFine and leftFine):
		if ((currentBoard[(y - 1)][(x - 1)] == letter) or (currentBoard[(y - 1)][(x - 1)] == 'ebce1dd2d40aec3')):
			validMoves.append([(y - 1) , (x - 1)])
	#Move Diagonally Up and to the Right:
	if (upFine and rightFine):
		if ((currentBoard[(y - 1)][(x + 1)] == letter) or (currentBoard[(y - 1)][(x + 1)] == 'ebce1dd2d40aec3')):
			validMoves.append([(y - 1) , (x + 1)])
	#Move Diagonally Down and to the Left:
	if (downFine and leftFine):
		if ((currentBoard[(y + 1)][(x - 1)] == letter) or (currentBoard[(y + 1)][(x - 1)] == 'ebce1dd2d40aec3')):
			validMoves.append([(y + 1) , (x - 1)])
	#Move Diagonally Down and to the Right:
	if (downFine and rightFine):
		if ((currentBoard[(y + 1)][(x + 1)] == letter) or (currentBoard[(y + 1)][(x + 1)] == 'ebce1dd2d40aec3')):
			validMoves.append([(y + 1) , (x + 1)])

	return validMoves


#Define a function that takes the user's input and generates the corresponding board(s):
def genBoards(numBoardsToGen = 1):
	for i in range(0 , numBoardsToGen):
		genedBoards = []
		#Generate 10 boards, then choose the one that managed to fit-in the most words:
		for i in range(0 , 10):
			tempBoard = board[:]
			notFull = True
			wordsNotAdded = []

			#Loop over each word to try to add it to the board:
			for word in words:
				#Detect if the board is already full, then return it as-is if it is:
				for row in tempBoard:
					if ('ebce1dd2d40aec3' in row):
						break
					else:
						continue

					notFull = False

				if (notFull):
					tryCounter = 0
					attemptSuccess = True
					while (True):
						#Allow a maximum of 50 tries to try and place each word (this is a bit overkill, but doesn't take-up too much time. Therefore it'll be nice to have for the larger puzzles):
						if (tryCounter >= 50):
							wordsNotAdded.append(word)
							break

						#Choose a random starting position (and try infinitely until one is found that is available):
						y2 = int(random.random() * boardDimensions[0])
						x2 = int(random.random() * boardDimensions[1])
						if ((tempBoard[y2][x2] == 'ebce1dd2d40aec3') | (tempBoard[y2][x2] == word[0])):
							tryCounter += 1
							usedLocations = []
							if (tempBoard[y2][x2] == 'ebce1dd2d40aec3'):
								tempBoard[y2][x2] = word[0]
								usedLocations.append([y2 , x2])
							firstLetter = True
							for letter in word:
								if (firstLetter):
									firstLetter = False
									continue
								moves = nextValidLocation(tempBoard , letter , y2 , x2)
								if (len(moves) == 0):
									for location in usedLocations:
										tempBoard[location[0]][location[1]] = 'ebce1dd2d40aec3'
									attemptSuccess = False
									break
								else:
									moveToTry = moves[int(random.random() * len(moves))]
									if (not(tempBoard[moveToTry[0]][moveToTry[1]] == letter)):
										tempBoard[moveToTry[0]][moveToTry[1]] = letter
										usedLocations.append([moveToTry[0] , moveToTry[1]])
									y2 = moveToTry[0]
									x2 = moveToTry[1]

							if (attemptSuccess):
								break

						else:
							continue
				genedBoards.append([tempBoard , len(wordsNotAdded)])
		leastWordsNotAdded = genedBoards[0][1]
		bestBoard = genedBoards[0][0]
		for aBoard in genedBoards:
			if (aBoard[1] < leastWordsNotAdded):
				bestBoard = aBoard[0]
				leastWordsNotAdded = aBoard[1]
		boards.append(bestBoard)


#Functions Relating to GUI Interaction:
def addWords():
        pass


def startBoardGen():
        pass


#Run the GUI:
window = Tk()
window.title('Roboxum Puzzle Generator')
window.geometry('800x900')
window.configure(bg = '#5C636E')

originalLogo = Image.open('Roboxum Logo.gif')
logoResized = originalLogo.resize((115 , 115) , Image.ANTIALIAS)
logoResized.save('logoResized1.gif' , 'gif')
logo = PhotoImage(file = 'logoResized1.gif')
logoCanvas = Canvas(window , width = 115 , height = 115 , bg = '#FFFFFF' , bd = 0 , highlightthickness = 0)
logoCanvas.create_image(0 , 0 , image = logo , anchor = 'nw')
logoCanvas.pack(side = 'top' , pady = 5)

heading = Label(window , text = 'Word Finder Puzzle Generator' , bg = '#5C636E' , fg = '#2F0077' , font = ('Times New Roman' , 25))
heading.pack(side = 'top' , pady = 5)

question1 = Label(window , text = 'What are the desired dimensions of the puzzle (Number of rows and columns)?' , bg = '#5C636E' , fg = '#FFFFFF' , font = ('Times New Roman' , 14))
question1.place(x = 5 , y = 175)
xDimenBox = Entry(window , width = 10 , font = ('Times New Roman' , 20) , bg = '#FFFFFF' , fg = '#000000')
xDimenBox.insert(0 , 'Rows')
yDimenBox = Entry(window , width = 10 , font = ('Times New Roman' , 20) , bg = '#FFFFFF' , fg = '#000000')
yDimenBox.insert(0 , 'Columns')
xDimenBox.place(x = 15 , y = 210)
yDimenBox.place(x = 220 , y = 210)

question2 = Label(window , text = 'How many different puzzles would you like to be generated?' , bg = '#5C636E' , fg = '#FFFFFF' , font = ('Times New Roman' , 14))
question2.place(x = 5 , y = 265)
numPuzzleBox = Entry(window , width = 6 , font = ('Times New Roman' , 20) , bg = '#FFFFFF' , fg = '#000000')
numPuzzleBox.insert(0 , '1')
numPuzzleBox.place(x = 15 , y = 300)

addWordsButton = Button(window , text = 'Add A Word To The Puzzle' , bd = 0 , bg = '#6bf442' , fg = '#000000' , activebackground = '#303030' , activeforeground = '#6bf442', font = ('Times New Roman' , 15) , command = addWords)
addWordsButton.place(x = 5 , y = 365)

wordsBelowLabel = Label(window , text = 'Below are the custom words to be added to the puzzle:' , bg = '#5C636E' , fg = '#FFFFFF' , font = ('Times New Roman' , 14))
wordsBelowLabel.place(x = 5 , y = 400)
wordsBelowReminder = Label(window , text = 'Please keep in mind that the first words added take priority over words added later, when it comes to finding placement for them within the puzzle.' , bg = '#5C636E' , fg = '#CCCCCC' , font = ('Times New Roman' , 10))
wordsBelowReminder.place(x = 5 , y = 420)
wordsListLabel = Label(window , text = wordsDisplayed , justify = LEFT , bg = '#5C636E' , fg = '#ce5656' , font = ('Times New Roman bold' , 14))
wordsListLabel.place(x = 10 , y = 450)

genButton = Button(window , text = 'Generate Puzzle(s)' , bd = 0 , bg = '#007BFF' , fg = '#FFFFFF' , activebackground = '#FF5000' , activeforeground = '#000000', font = ('Times New Roman' , 20) , command = startBoardGen)
genButton.pack(side = 'bottom' , pady = 10)

window.mainloop()

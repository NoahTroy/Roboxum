#Make all necessary imports:
import threading , time , random
from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
import os

#Declare any necessary global variables:
defaultCharSet = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
preserveCapsCharSet = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']

colors = ['#1C1C1C' , '#ED0033' , '#FF6200' , '#4EE000' , '#00AB85' , '#7900BC' , '#FFFF00']
wordsToInclude = []
defaultWordDisplayed = '1.)\tDEFAULT'
characterSet = defaultCharSet[:]


### Core Functions ###

#Define a function to save the generated board(s) as a PDF:
def pdfGen(board):
	pdf = FPDF(orientation = 'P' , unit = 'in' , format = 'letter')
	pdf.add_page()

	#Add the title:
	pdf.set_font('Arial' , size = 25)
	pdf.cell(7.5 , 0.5 , txt = 'Word Finder Puzzle' , ln = 1 , align = 'C' , border = 0)

	#Add the cells:
	cellHeight = (9.25 / len(board))
	cellWidth = (7.75 / len(board[0]))
	#There are 72 points in one inch... assume 60 just to make sure there is plenty of extra room:
	smallerOne = 0
	if (cellHeight > cellWidth):
		smallerOne = cellWidth
	else:
		smallerOne = cellHeight

	fontSize = (smallerOne * 60)
	pdf.set_font('Arial' , size = fontSize)
	for row in board:
		for character in row:
			pdf.cell(cellWidth , cellHeight , txt = character , ln = 0 , align = 'C' , border = 1)
		pdf.ln(cellHeight)

	name = 'Puzzle'
	nameWithCounter = 'Puzzle'
	counter = 1
	while True:
		if (os.path.isfile((nameWithCounter + '.pdf'))):
			nameWithCounter = (name + str(counter))
			counter += 1
		else:
			pdf.output((nameWithCounter + '.pdf'))
			break


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
def genBoards(numBoardsToGen , boardDimensions , words):
	boards = []

	for i in range(0 , numBoardsToGen):
		genedBoards = []
		#Generate 10 boards, then choose the one that managed to fit-in the most words:
		for i in range(0 , 10):
			#Generate a base, "blank" board:
			tempBoard = []
			for i in range(0 , boardDimensions[0]):
				row = []
				for i in range(0 , boardDimensions[1]):
					row.append('ebce1dd2d40aec3')
				tempBoard.append(row)
			notFull = True
			wordsNotAdded = []
			loopNotBroken = True
			notAddedYet = True

			#Loop over each word to try to add it to the board:
			finalWord = words[(len(words) - 1)]
			for word in words:
				#Detect if the board is already full, then return it as-is if it is:
				for row in tempBoard:
					if ('ebce1dd2d40aec3' in row):
						notFull = True
						break
					else:
						notFull = False						
						continue

				if (notFull):
					tryCounter = 0
					while (True):
						attemptSuccess = True
						#Allow a maximum of 50 tries to try and place each word (this is a bit overkill, but doesn't take-up too much time. Therefore it'll be nice to have for the larger puzzles):
						if (tryCounter >= 50):
							wordsNotAdded.append(word)
							if (word == finalWord):
								loopNotBroken = True
							else:
								loopNotBroken = False
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
								if (word == finalWord):
									loopNotBroken = True
								else:
									loopNotBroken = False
								break

						else:
							continue
				else:
					genedBoards.append([tempBoard , len(wordsNotAdded)])
					notAddedYet = False
					break
				if (loopNotBroken):
					genedBoards.append([tempBoard , len(wordsNotAdded)])
					notAddedYet = False
					break
				else:
					loopNotBroken = True

			if (notAddedYet):
				genedBoards.append([tempBoard , len(wordsNotAdded)])
				notAddedYet = False

		if (notAddedYet):
			genedBoards.append([tempBoard , 0])

		if (len(genedBoards) == 0):
			continue
		leastWordsNotAdded = genedBoards[0][1]
		bestBoard = genedBoards[0][0]
		for aBoard in genedBoards:
			if (aBoard[1] < leastWordsNotAdded):
				bestBoard = aBoard[0]
				leastWordsNotAdded = aBoard[1]
		boards.append(bestBoard)

	return boards

### End of Core Functions ###

### GUI-Related Functions ###

#Define a function to handle the start of the board generation process, and present a waiting screen:
def startBoardGen():
	#Load the custom character set if there is one:
	global characterSet
	if (characterSet[0] == 'Custom'):
		try:
			charSetFile = open('customCharacterSet.txt' , 'r')
			characters = charSetFile.read()
			characters = characters[0:(len(characters) - 1)]
			charSetFile.close()

			characterSet = []
			for character in characters:
				characterSet.append(character)

		except:
			characterSet = defaultCharSet

	if (int(numPuzzleBox.get()) > 1):
		messagebox.showinfo('Puzzles Being Generated' , 'Your puzzles will now be generated after clicking "OK". You will receive another message once they have been successfully created.')
	else:
		messagebox.showinfo('Puzzle Being Generated' , 'Your puzzle will now be generated after clicking "OK". You will receive another message once it has been successfully created.')

	numberOfPuzzles = int(numPuzzleBox.get())
	boardDimensions = [int(yDimenBox.get()) , int(xDimenBox.get())]

	boardsToUse = genBoards(numberOfPuzzles , boardDimensions , wordsToInclude)

	boardCounter = 0
	for board in boardsToUse:
		rowCounter = 0
		for row in board:
			itemCounter = 0
			for item in row:
				if (item == 'ebce1dd2d40aec3'):
					boardsToUse[boardCounter][rowCounter][itemCounter] = characterSet[int(random.random() * len(characterSet))]
				itemCounter += 1
			rowCounter += 1
		boardCounter += 1

		pdfGen(board)

	messagebox.showinfo('Puzzles Generated' , 'Your puzzle(s) have now been successfully generated and saved in the same directory as this program.\nEnjoy!\n:)')

	window.destroy()


#Define a function to get the inputted words from getWords, and add them to the wordsToInclude list:
def addWords(windowToDestroy , word , characterSet):
	windowToDestroy.destroy()

	word = word.strip()
	word = word.replace(' ' , '')

	if (characterSet == defaultCharSet):
		word = word.upper()

	#Load the custom charset if applicable, for compliance checking:
	if (characterSet[0] == 'Custom'):
		runtimeErrorOccurred = False
		customSet = []
		try:
			charSetFile = open('customCharacterSet.txt' , 'r')
			characters = charSetFile.read()
			characters = characters[0:(len(characters) - 1)]
			charSetFile.close()

			for char in characters:
				if (((len(characters) <= 0) or (char == ' ')) or ((char == '\t') or (char == '\n'))):
					messagebox.showerror('Invalid Character Set File' , 'Please check customCharacterSet.txt to make sure it contains no invalid content (such as new lines, tabs, spaces, etc.).')
					runtimeErrorOccurred = True
					break
				customSet.append(char)
		except:
			messagebox.showerror('Character Set File Error' , 'An error occurred processing your custom character set. Please make sure everything is in order and try again.')
			return

		if (runtimeErrorOccurred):
			return
		else:
			characterSet = customSet

	#Check to make sure the input is valid:
	for char in word:
		if (not(char in characterSet)):
			messagebox.showerror('Invalid Input' , 'The word you have inputted was not valid. Please make sure you only use characters found in the customCharacterSet.txt file.')
			return
		if (len(word) > 20):
			messagebox.showerror('Invalid Input' , 'Please make sure the word you entered is less than 20 characters in length.')
			return
		if (len(word) < 3):
			messagebox.showerror('Invalid Input' , 'Please make sure the word you entered is at least 3 characters in length.')
			return
		if (len(wordsToInclude) >= 20):
			messagebox.showerror('Unable to Accept Input' , 'You have already entered the maximum of 20 words, therefore this word will not be added.')
			return

	#Check to make sure the word hasn't already been added:
	if (word in wordsToInclude):
		messagebox.showerror('Unable to Accept Input' , 'This word has already been entered. Please enter a new word.')
		return

	wordsToInclude.append(word)
	counter = 1
	wordsDisplayed = ''
	for word in wordsToInclude:
		wordsDisplayed += (str(counter) + '.)\t' + word + '\n')
		counter += 1
	wordsListLabel.configure(text = wordsDisplayed)

### End of GUI-Related Functions ###

## GUIs ###

#Define a function to create a pop-up window which allows the user to add custom words:
def getWords():
	getWordWindow = Toplevel()
	getWordWindow.title('Add Custom Words')
	getWordWindow.geometry('450x175')
	getWordWindow.configure(bg = colors[0])

	heading = Label(getWordWindow , text = 'Please Enter A Word Below:' , bg = colors[0] , fg = colors[2] , font = ('Arial' , 16))
	heading.pack(side = 'top' , pady = (5 , 0))

	wordsBelowReminder = Label(getWordWindow , text = '(Words added first are more likely to be able to be fit\ninto the puzzle than words towards the end of the list.)' , bg = colors[0] , fg = colors[2] , font = ('Arial' , 11))
	wordsBelowReminder.pack(side = 'top' , pady = (1 , 2))

	wordBox = Entry(getWordWindow , width = 30 , font = ('Arial' , 18) , bg = colors[0] , fg = colors[4] , bd = 3 , relief = 'groove' , highlightthickness = 0 , insertbackground = colors[5] , highlightbackground = colors[5])
	wordBox.pack(side = 'top' , pady = (2 , 0))
	wordBox.focus_set()

	submitButton = Button(getWordWindow , text = 'Submit' , bd = 0 , bg = colors[3] , fg = colors[0] , activebackground = colors[0] , activeforeground = colors[3] , highlightthickness = 2 , highlightbackground = colors[4] , font = ('Arial bold' , 16) , command = lambda: addWords(getWordWindow , wordBox.get() , characterSet))
	submitButton.place(x = 273 , y = 125)

	cancelButton = Button(getWordWindow , text = 'Cancel' , bd = 0 , bg = colors[1] , fg = colors[0] , activebackground = colors[0] , activeforeground = colors[1] , highlightthickness = 2 , highlightbackground = colors[5] , font = ('Arial bold' , 16) , command = getWordWindow.destroy)
	cancelButton.place(x = 75 , y = 125)

	#Bind the enter keys, so that they may be used instead of having to click the submit button:
	getWordWindow.bind('<Return>' , lambda _: addWords(getWordWindow , wordBox.get() , characterSet))
	getWordWindow.bind('<KP_Enter>' , lambda _: addWords(getWordWindow , wordBox.get() , characterSet))


#Define a function to change the character set:
def changeChosenCharSet(buttonNum):
	global characterSet
	if (buttonNum == 0):
		characterSet = defaultCharSet[:]
		defaultButton.configure(fg = colors[3] , activeforeground = colors[1] , highlightthickness = 2)
		defaultLowerButton.configure(fg = colors[1] , activeforeground = colors[3] , highlightthickness = 0)
		customButton.configure(fg = colors[1] , activeforeground = colors[3] , highlightthickness = 0)
	elif (buttonNum == 1):
		characterSet = preserveCapsCharSet[:]
		defaultButton.configure(fg = colors[1] , activeforeground = colors[3] , highlightthickness = 0)
		defaultLowerButton.configure(fg = colors[3] , activeforeground = colors[1] , highlightthickness = 2)
		customButton.configure(fg = colors[1] , activeforeground = colors[3] , highlightthickness = 0)
	elif (buttonNum == 2):
		characterSet = ['Custom']
		defaultButton.configure(fg = colors[1] , activeforeground = colors[3] , highlightthickness = 0)
		defaultLowerButton.configure(fg = colors[1] , activeforeground = colors[3] , highlightthickness = 0)
		customButton.configure(fg = colors[3] , activeforeground = colors[1] , highlightthickness = 2)
	else:
		characterSet = defaultCharSet[:]
		defaultButton.configure(fg = colors[3] , activeforeground = colors[1] , highlightthickness = 2)
		defaultLowerButton.configure(fg = colors[1] , activeforeground = colors[3] , highlightthickness = 0)
		customButton.configure(fg = colors[1] , activeforeground = colors[3] , highlightthickness = 0)


#Define a function meant to be threaded, and automatically check inputted values for validity:
def validityCheck():
	while True:
		time.sleep(0.25)
		xDimen = xDimenBox.get()
		yDimen = yDimenBox.get()
		numPuzzle = numPuzzleBox.get()
		allValid = [False , False , True]

		if (((xDimen.isdigit()) and (int(xDimen) >= 3)) and (int(xDimen) <= 20)):
			xDimenBox.configure(fg = colors[3])
			allValid[0] = True
		else:
			xDimenBox.configure(fg = colors[1])
			allValid[0] = False

		if (((yDimen.isdigit()) and (int(yDimen) >= 3)) and (int(yDimen) <= 20)):
			yDimenBox.configure(fg = colors[3])
			allValid[1] = True
		else:
			yDimenBox.configure(fg = colors[1])
			allValid[1] = False

		if (((numPuzzle.isdigit()) and (int(numPuzzle) >= 1)) and (int(numPuzzle) <= 50)):
			numPuzzleBox.configure(fg = colors[3])
			allValid[2] = True
			if (int(numPuzzle) > 1):
				genButton.configure(text = 'Generate Puzzles')
			else:
				genButton.configure(text = 'Generate Puzzle')
		else:
			numPuzzleBox.configure(fg = colors[1])
			allValid[2] = False

		if (((allValid[0] and allValid[1]) and allValid[2]) and (len(wordsToInclude) >= 1)):
			genButton.configure(command = startBoardGen)
		else:
			genButton.configure(command = lambda: messagebox.showerror('Invalid Input' , 'Please check your input to ensure it is valid, and try again.'))


#Run the main GUI:
window = Tk()
window.title('Roboxum Puzzle Generator')
window.geometry('800x900')
window.configure(bg = colors[0])

heading = Label(window , text = 'Word Finder Puzzle Generator' , bg = colors[0] , fg = colors[4] , font = ('Arial bold' , 30))
heading.pack(side = 'top' , pady = 5)

question1 = Label(window , text = 'What are the desired dimensions of the puzzle?' , bg = colors[0] , fg = colors[2] , font = ('Arial' , 16))
question1.place(x = 5 , y = 70)
xDimenBox = Entry(window , width = 10 , font = ('Arial bold' , 20) , bg = colors[0] , fg = colors[1] , bd = 0 , relief = 'flat' , highlightthickness = 2 , insertbackground = colors[5] , highlightbackground = colors[5])
xDimenBox.insert(0 , 'Columns')
yDimenBox = Entry(window , width = 10 , font = ('Arial bold' , 20) , bg = colors[0] , fg = colors[1] , bd = 0 , relief = 'flat' , highlightthickness = 2 , insertbackground = colors[5] , highlightbackground = colors[5])
yDimenBox.insert(0 , 'Rows')
xDimenBox.place(x = 5 , y = 100)
yDimenBox.place(x = 210 , y = 100)

question2 = Label(window , text = 'How many different puzzles would you like to generate?' , bg = colors[0] , fg = colors[2] , font = ('Arial' , 16))
question2.place(x = 5 , y = 155)
numPuzzleBox = Entry(window , width = 6 , font = ('Arial' , 20) , bg = colors[0] , fg = colors[1] , bd = 0 , relief = 'flat' , highlightthickness = 2 , insertbackground = colors[5] , highlightbackground = colors[5])
numPuzzleBox.insert(0 , '1')
numPuzzleBox.place(x = 5 , y = 185)

question3 = Label(window , text = 'Choose a character set:' , bg = colors[0] , fg = colors[2] , font = ('Arial' , 16))
question3.place(x = 5 , y = 245)
defaultButton = Button(window , text = 'Default' , font = ('Arial' , 16) , bg = colors[0] , fg = colors[3] , bd = 0 , relief = 'flat' , highlightthickness = 2 , highlightbackground = colors[4] , activebackground = colors[0] , activeforeground = colors[1] , command = lambda: changeChosenCharSet(0))
defaultButton.place(x = 5 , y = 275)
defaultLowerButton = Button(window , text = 'Default Plus Lowercase Letters' , font = ('Arial' , 16) , bg = colors[0] , fg = colors[1] , bd = 0 , relief = 'flat' , highlightthickness = 0 , highlightbackground = colors[4] , activebackground = colors[0] , activeforeground = colors[3] , command = lambda: changeChosenCharSet(1))
defaultLowerButton.place(x = 120 , y = 275)
customButton = Button(window , text = 'Custom' , font = ('Arial' , 16) , bg = colors[0] , fg = colors[1] , bd = 0 , relief = 'flat' , highlightthickness = 0 , highlightbackground = colors[4] , activebackground = colors[0] , activeforeground = colors[3] , command = lambda: changeChosenCharSet(2))
customButton.place(x = 467 , y = 275)

wordsBelowLabel = Label(window , text = 'Word List:' , bg = colors[0] , fg = colors[2] , font = ('Arial' , 20))
wordsBelowLabel.pack(side = 'top' , pady = (255 , 0))

addWordsButton = Button(window , text = 'Add A Word' , bd = 0 , bg = colors[5] , fg = colors[0] , activebackground = colors[0] , activeforeground = colors[5] , highlightthickness = 2 , highlightbackground = colors[5] , font = ('Arial bold' , 15) , command = getWords)
addWordsButton.pack(side = 'top' , pady = 5)

wordsListLabel = Label(window , text = defaultWordDisplayed , justify = LEFT , bg = colors[0] , fg = colors[6] , font = ('Arial' , 12))
wordsListLabel.place(x = 10 , y = 400)

genButton = Button(window , text = 'Generate Puzzle' , bd = 0 , bg = colors[4] , fg = colors[0] , activebackground = colors[0] , activeforeground = colors[4] , highlightthickness = 4 , highlightbackground = colors[5] , font = ('Arial bold' , 20) , command = lambda: messagebox.showerror('Invalid Input' , 'Please check your input to ensure it is valid, and try again.'))
genButton.pack(side = 'bottom' , pady = 15)

#Start the validity checking thread:
validityThread = threading.Thread(target = validityCheck , args = () , daemon = True)
validityThread.start()

window.mainloop()

### End of GUIs ###

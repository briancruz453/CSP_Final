class Hangman():
	def __init__(self):
		print "Welcome to 'Hangman', are you ready to die?" #Text to set the story of the game
		print "(1)Yes, for I am already dead.\n(2)No, get me outta here!" #Text to set the story of the game
		user_choice_1 = raw_input("->")
		
		if user_choice_1 == '1':#Gives the user a choice to back out of the game, or continue playing
			print "Loading nooses, murderers, rapists, thiefs, lunatics..." #Text to set the story of the game
			self.start_game() #starts the game
		elif user_choice_1 == '2': #Gives the user an option to back out of the game
			print "Bye bye now..." #text shown if the user choses to end the game
			exit() #ends the game
		else:
			print "I'm sorry, I'm hard of hearing, could you repeat that?" #If user does not give one of the desired responses (1 or 2) it will re-ask the  user for input
			self.__init__()

	def start_game(self):
		print "A crowd begins to gather, they can't wait to see some real" #Lines 18-24 are just text for the story line
		print "justice. There's just one thing, you aren't a real criminal."
		print "No, no. You're the wrong time, wrong place type. You may think"
		print "you're dead, but it's not like that at all. Yes, yes. You've"
		print "got a chance to live. All you've gotta do is guess the right"
		print "words and you can live to see another day. But don't get so"
		print "happy yet. If you make 6 wrong guess, YOU'RE TOAST! VAMANOS!"
		self.core_game()

	def core_game(self): #defines the core game
		guesses = 0 #initialized guesses to 0
		letters_used = "" #initalizes the letter used to none
		the_word = "pizza" #this is where the word is set for the game
		progress = ["?", "?", "?", "?", "?"] #used as place holders so the user knows how many letters are in the word, and the letters they have correctly guessed
		
		while guesses < 6: #Allows the max guesses to be 5
			guess = raw_input("Guess a letter ->") #asks the user to guess a letter for the word

                        if guess in the_word and guess not in letters_used:#segment of code which is executed once the user correctly guesses the letter in the word
				print "As it turns out, your guess was RIGHT!"
				letters_used += "," + guess #adds the guessed letter to the list
				self.hangman_graphic(guesses) #used for showing the hangman picture
				print "Progress: " + self.progress_updater(guess, the_word, progress) #updates the users progress
				print "Letter used: " + letters_used #add the guess to letters used
			elif guess not in the_word and not(letters_used): #executed when the user guesses a wrong letter
				guesses += 1 #adds one to the guesses variable
				print "Things aren't looking so good, that guess was WRONG!" 
				print "Oh man, that crowd is getting happy, I thought you"
				print "wanted to make them mad?"
				letters_used += "," + guess #adds the guess to letter used
				self.hangman_graphic(guesses) #used for displaying the hangman picture
				print "Progress: " + "".join(progress) #update users progress
				print "Letter used: " + letters_used #adds the guess to letters used
			else: #statement id returned when valid input is not inputed
				print "That's the wrong letter, you wanna be out here all day?"
				print "Try again!"



	def hangman_graphic(self, guesses): #inistalies the hangman_graphic function, which will update the hangman picture to show progress 
		if guesses == 0: #lines 58-110 are used to display the picture of the hanging man when guesses are right/wrong
			print "________      "
			print "|      |      "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
		elif guesses == 1:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|             "
			print "|             "
			print "|             "
		elif guesses == 2:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /       "
			print "|             "
			print "|             "
		elif guesses == 3:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|      "
			print "|             "
			print "|             "
		elif guesses == 4:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|             "
			print "|             "
		elif guesses == 5:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     /       "
			print "|             "
		else:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     / \     "
			print "|             "
			print "The noose tightens around your neck, and you feel the"
			print "sudden urge to urinate."
			print "GAME OVER!"
			self.__init__()

	def progress_updater(self, guess, the_word, progress): #this determines the progress of the user, and will end the game once the word is guessed
		i = 0 #initialized the i varible to 0
		while i < len(the_word):#makes sure the length of i is less than the word
			if guess == the_word[i]:#once the all of the letters are fully guessed, this code will execute telling the program the user has guessed all the letters and to end the game
				progress[i] = guess
				i += 1
			else: #returns this if the user has not guessed all of the letters yet
				i += 1

		return "".join(progress) #reports back to the main program if the user is finished with the game or not

game = Hangman() #ends the game
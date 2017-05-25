# A basic Hangman game.

class Hangman:

    used_chars = set()                                                                  #makes the variable 'used_chars' equal to 'set()'
    chances = 0                                                                         #makes the 'chances' variable equal to 0 at the start
    letter_map = {}                                                                     #Dictionary of chars

    def __init__(self, game_word):                                                      #defines the __init__ variable
        self.game_word = str(game_word).lower()                                         # Stores the word the user needs to solve for
        Hangman.chances = len(self.game_word)                                           #Chances based on the length of the word

        for x in range(len(game_word)):                                                 #Uses a for loop when 'x' is in range of the length of the 'game_word' variable
            if game_word[x] == " ":
                Hangman.letter_map[x] = " "                                             #Make sure the underscores aren't added for spaces.
            else:
                Hangman.letter_map[x] = "_"                                             #Add temp underscores

    def print_letter_map(self):                                                         #defines 'print_letter_map' as 'self'
        spaces = "\n"                                                                   #Sets the variable 'spaces' equal to "\n"
        for v in Hangman.letter_map.values():                                           #Print the spaces
            spaces += v + " "                                                           #Puts the spaces in between the string

        print(spaces + "\n")                                                            #Prints the spaces

    def guess_letter(self, letter):                                                     #defines guess_letter as the letter that you guessed
        if letter not in self.used_chars:                                               #if/else statement for if your letter is in the word being guessed

            if len(letter) != 1:                                                        #If the letter is longer than one character
                print("You must enter a single letter.")                                #Print 'you must enter a single letter'

            elif self.game_word.find(letter) == - 1:                                    #else/if statement for if the letter is wrong
                print("\nWrong!")                                                       #prints 'wrong'
                Hangman.chances -= 1                                                    #Subtract only when the user gets the guess wrong
                self.used_chars.add(letter)                                             #Add the unused letter in the set.
            else:                                                                       x#Else statement
                for x in range(len(self.game_word)):                                    #Go through the whole map and find the matching letter.
                    if self.game_word[x] == letter:     	                        #If it matches, replace _ with the letter
                        Hangman.letter_map[x] = letter                                  #Hangman.letter_map is set equal to the 'letter' variable

                self.used_chars.add(letter)                                             #Add the unused letter in the set.
                print("\nThat was right!")                                              #Print outside the loop to avoid duplicate messages for multiple letters

                                                                                        #Print the number of chances the user has left
            if self.chances != 0 and self.get_num_blanks() != 0:                        #if statement to check the amount of guesses left
                self.print_letter_map()                                                 #prints the letter_map
                print("You have " + str(Hangman.chances) + " guesses left.")            #Prints "you have x guesses left"
        else:                                                                           #Else statement
            print("\nYou already guessed this letter. Please pick a different letter.") #Prints 'You already guessed this letter'



    def start_game(self):                                                               #Defines 'start_game' as the next statement
        self.print_letter_map()                                                         #Display the empty cells

        while self.chances != 0:                                                        #Continue asking for input as long as chances > 0
            if self.get_num_blanks() != 0:                                              #if statement to check if the self.get_num_blanks is not equal
                self.guess_letter(raw_input('Please guess a letter: '))                 #CHANGED the original code to not require the user to have quotations around their guess
            else: break                                                                 #Else statement that breaks the loop

        if self.get_num_blanks() == 0:                                                  #If statement to check if self.get_num_blanks is equal to 0
            self.print_letter_map()                                                     #Prints the letter map
            print("You won the game!")                                                  #Prints 'you won the game'
        else:                                                                           #Else statement
            print("You lost the game.")                                                 #Prints 'you lost the game'
            print("The word was: " + self.game_word)                                    #Prints the word the user failed to guess

    @staticmethod                                                                       #A staticmethod, which changes the way the variables are handled
    def get_num_blanks():                                                               #Defines the "get_num_blanks" variable
        count = 0                                                                       #Sets the 'count' variable to 0
        for v in Hangman.letter_map.values():                                           #Count the number of blank cells
            if v == "_":                                                                #Checks if v equals  '_'
                count += 1                                                              #Adds 1 to the 'count' variable
        return count                                                                    #Returns the 'count' variable for the user to see

                                                                                        #Run the game
hangman =Hangman(raw_input('Please enter the game word: '))                             #CHANGED the original code to not require the user to put quotations around the game word
hangman.start_game()                                                                    #Starts the game


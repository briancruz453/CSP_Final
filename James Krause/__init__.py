# A basic Hangman game.

class Hangman:

    used_chars = set()
    chances = 0
    letter_map = {} # Dictionary of chars

    def __init__(self, game_word):
        self.game_word = str(game_word).lower() # Stores the word the user needs to solve for
        Hangman.chances = len(self.game_word) # Chances based on the length of the word

        for x in range(len(game_word)):
            if game_word[x] == " ":
                Hangman.letter_map[x] = " " # Make sure the underscores aren't added for spaces.
            else:
                Hangman.letter_map[x] = "_" # Add temp underscores

    def print_letter_map(self):
        spaces = "\n"
        for v in Hangman.letter_map.values(): # Print the spaces
            spaces += v + " "

        print(spaces + "\n")

    def guess_letter(self, letter):
        if letter not in self.used_chars:

            if len(letter) != 1:
                print("You must enter a single letter.")

            elif self.game_word.find(letter) == - 1:
                print("\nWrong!")
                Hangman.chances -= 1 # Subtract only when the user gets the guess wrong
                self.used_chars.add(letter)  # Add the unused letter in the set.
            else:
                for x in range(len(self.game_word)): # Go through the whole map and find the matching letter.
                    if self.game_word[x] == letter: # If it matches, replace _ with the letter
                        Hangman.letter_map[x] = letter

                self.used_chars.add(letter)  # Add the unused letter in the set.
                print("\nThat was right!") # Print outside the loop to avoid duplicate messages for multiple letters

            # Print the number of chances the user has left
            if self.chances != 0 and self.get_num_blanks() != 0:
                self.print_letter_map()
                print("You have " + str(Hangman.chances) + " guesses left.")
        else:
            print("\nYou already guessed this letter. Please pick a different letter.")



    def start_game(self):
        self.print_letter_map() # Display the empty cells

        while self.chances != 0: # Continue asking for input as long as chances > 0
            if self.get_num_blanks() != 0:
                self.guess_letter(str(input("Please guess a letter: ")))
            else: break

        if self.get_num_blanks() == 0:
            self.print_letter_map()
            print("You won the game!")
        else:
            print("You lost the game.")
            print("The word was: " + self.game_word)

    @staticmethod
    def get_num_blanks():
        count = 0
        for v in Hangman.letter_map.values():  # Count the number of blank cells
            if v == "_":
                count += 1
        return count

# Run the game
hangman = Hangman(str(input("Please enter the game_word: ")))
hangman.start_game()


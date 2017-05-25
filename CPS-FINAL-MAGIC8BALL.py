import random ## importing 'random' gives you the ability to randomly generate numbers
import time ## importing 'time' gives you the ability to deal with times and dates
responses = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never", ## In lines 3 and 4, you are giving 'responses' a value of a list of strings. This list is full of the responses (strings) that the program will give you.
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]

## Following function asks user question, then returns random results from responses
def answerQuery(): ## This line of code defines 'answerquery', and everything intented within this define will be part of 'answerquery'
    question = input("Ask and you shall receive: ") ## After this program is ran, 'question' is displayed and the user can insert their question into this line. 
    print("Let me dig deep into the waters of life, and find your answer") ## After the input of 'question' is received, this program prints the string "let me dive deep into the waters of life, and find your answers"
    time.sleep(2) ## this line of code uses the imported 'time' ability to be able to wait for (2) seconds.
    print("Hmmm") # This line of code prints the string "Hmmm" after time.sleep(2) is done.
    time.sleep(2) # This line of code uses the imported 'time' ability to be able to wait for (2) seconds.
    print(random.choice(responses)) # This line of code uses 'random.choice' in order to pick out a random string in the list of 'responses'
    print("\n") ## This 'print' command does absolutely nothing for the functioning of the program. I deleted this line, and the program still ran the same.
answerQuery() ## This line of code runs "answerQuery"

## Following asks user if they would like to play again, and loops until user is finished
secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: ")) ## Similar to the line 9 variable 'question', this variable displays a string, and then allows the user to type their response in right next to the string.
while secondQuestion == str("Y"): ## If your input from line 18 "secondQuestion" is "Y", then run line 20
    answerQuery() ## This line of code will run "answerQuery" again.
    secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: ")) ## Although this code is the same as lie=ne 19, it does not serve a function in the program.
else: ## If the input to line 19 is not "Y", then execute line 22
    print(input("Press any key to exit")) ## This line of code prints "Press any key to exit" and then if you pressed any key, it will error out and will end the code!
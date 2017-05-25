#JACOB COMMENT: The code is pretty simple, the code gives a prompt, and you reply in quotes, then it gives a generic answer before giving a response from a list of variables.
#The code will the ask if you want to ask another question, and if yes then type 'Y' which will loop the code, and you can continue to answer. If you type anything else the loop breaks.

import random
import time

#JACOB COMMENT: These contain the responses for the program when you ask a question. It is randomly generated as you will see later.
responses = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never",
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]

## Following function asks user question, then returns random results from responses
def answerQuery():
    question = input("Ask and you shall receive: ")   #JACOB COMMMENT: This line of code is the prompt for you to ask a question, your question must in quotes like, 'do I like chocolate?' for a response
    print("Let me dig deep into the waters of life, and find your answer")
    time.sleep(2)
    print("Hmmm")
    time.sleep(2)
    print(random.choice(responses)) #JACOB COMMENT: The program will wait a while and give generic responses to act as though it was thinking before giving you a response from the variable above.
    print("\n")
answerQuery() #JACOB COMMENT: This is where your prompt would be.

## Following asks user if they would like to play again, and loops until user is finished
secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
while secondQuestion == str("Y"): #JACOB COMMENT: If you type 'Y' back then the code will loop back and ask you again. 
    answerQuery()
    secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: ")) #JACOB COMMENT: This is the prompt you will receieve.
else:
    print(input("Press any key to exit")) #JACOB COMMENT: If you type anything other than 'y' then you leave the loop.
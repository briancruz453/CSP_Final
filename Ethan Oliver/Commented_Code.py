import random
import time
#These are the available responces, obviously, they are not finished and the letters are placeholders.
response=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","Q","R","S","T","U"]

def Input():
    raw_input("Whats on your mind: ") #This is the prompt to start the asking process
    print "let me think about your question" #Prompts user with text
    time.sleep(4) #Takes four seconds before printing a responce
    print random.choice(response) #The random.choice chooses one of the responces randomly
    Answer() #Goes into next part of code: def Awnser()

def Answer():
    print "do you want to ask me again about anything?" #Prompts user
    userchoice=raw_input("yes or no: ") #User inputs yes or no if they want to play agian and that is saved to variable userchoice
    if userchoice =="yes":
        Input() #If user types "yes" they will go through Input() again
    elif userchoice=="no":
        print "ok, have a nice day" #If user types "no" the code will stop with this prompt
    else:
        print "error with the input. answer again"
        Answer() #If user types in anything other then "yes" or "no" they will be prompted with Awnser() again
Input() #Input initializes the code
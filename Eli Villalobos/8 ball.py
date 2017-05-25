import sys #imports system specific parameters and functions
import random #imports module that allows program to use random function

ans = True #boolean function; allows program to function

while ans: #while ans is true
    question = input("Ask the magic 8 ball a question: (press enter to quit) ") #asks user a question

    print ("shaking...") #shows user while random answer loads
    
    answers = random.randint(1,8) #range of random answers algorithim selects from
    
    if question == "": #begins algorithim when user input is under quotation marks
        sys.exit() #shows error message
    
    elif answers == 1: #else if random integer = 1
        print ("It is certain") #shows user printed messsage
    
    elif answers == 2: #else if random integer = 2
        print ("Outlook good") #shows user printed messsage
    
    elif answers == 3: #else if random integer = 3
        print ("You may rely on it") #shows user printed messsage
    
    elif answers == 4: #else if random integer = 4
        print ("Ask again later") #shows user printed messsage
    
    elif answers == 5: #else if random integer = 5
        print ("Concentrate and ask again") #shows user printed messsage
    
    elif answers == 6: #else if random integer = 6
        print ("Reply hazy, try again") #shows user printed messsage
    
    elif answers == 7:#else if random integer = 7
        print ("My reply is no") #shows user printed messsage
    
    elif answers == 8: #else if random integer = 8
        print ("My sources say no") #shows user printed messsage
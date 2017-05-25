# -*- coding: utf-8 -*-
#make a magic 8 ball
import random
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful'] #establishes all possible answers 

print('  __  __          _____ _____ _____    ___  ')     #Prints cool logo for 8-ball (lines 6-15)
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print('')
print('')
print('')
print('Hello World, I am the Magic 8 Ball, What is your name?') 
name = raw_input()  #promts user for name
print('hello ' + name) 

def Magic8Ball(): 
    print('Ask me a question.') #asks user for question
    raw_input()
    print (answers[random.randint(0, len(answers)-1)] ) #finds random int and uses it to determine which answer it will randomly display, each # corresponds with an answer
    print('I hope that helped!')
    Replay() #runs replay function below
    

def Replay():
    print ('Do you have another question? [Y/N] ') #asks if they have another question
    reply = raw_input()
    if reply == 'Y':
        Magic8Ball() #if yes repeats function above
    elif reply == 'N':
        pass #if no it stops program
    else:
        print('I apologise, I did not catch that. Please repeat.') #if neither y or s, repeat this function
        Replay()
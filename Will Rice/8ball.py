import random       #random number generator

ANSWERS = [                                #below are the various answers that the program can output, randomly
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful" ]

def main():      #defines the main and only task
    print(ANSWERS[random.randint(0, len(ANSWERS) - 1)])
    #prints out the actual text answer in console. the program assigns a random integer to each answer above and it uses the import
    #random to choose a random response
    #len(ANSWERS) insures that no matter how many answers are added above the program still works

if __name__ == "__main__":
    main()
#without this the file doesnt work. if this program is ran alone it gets assigned the name "__main__". if this is not true then
#the program will not run. if it is true it will run Main(), which is the defination above. this will then execute that code to 
#run the 8 ball ;)
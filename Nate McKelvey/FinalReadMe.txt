https://github.com/Chennaipy/hangman 

Code Start:
import time
name = raw_input("What is your name? ")
print "Hello, " + name + ", Time to play hangman!\n At any time, type quit to exit"
time.sleep(1)
print "Start guessing..."
time.sleep(0.5)
word = "secret"

guesses = ''

turns = 10
while turns > 0:         

    failed = 0             

    for char in word:      

        if char in guesses:    
    
            print char,    

        else:
    
            print "_",     
       
            failed += 1    

    if failed == 0:        
        print "You won"  

        break              

    print

    guess = raw_input("guess a character:") 

    guesses += guess      
    if guess == "Quit" or guess == "quit":
        sys.exit()
    if guess not in word:  
 
        turns -= 1        
 
        print "Wrong"    
 
        print "You have", + turns, 'more guesses' 
 
if turns == 0:           
    
            print "You Lose" 
^^^Code end
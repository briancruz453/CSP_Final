#!/usr/bin/env python3
# Magic 8 Ball IRC bot
# Created by Lance Brignoni
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import random #imports random module
import time #imports time module
responses = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never",
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"] #creates all the different responses which are possible

## Following function asks user question, then returns random results from responses
def answerQuery(): #defines function 'answer query'
    question = input("Ask and you shall receive: ") #defines what 'question' is, displayed after user inputs answerQuery(), and allows user to input question
    print("Let me dig deep into the waters of life, and find your answer") #after user inputs question, prints this text
    time.sleep(2) #waits 2 seconds before displaying "hmm"
    print("Hmmm") #displays text "hmm"
    time.sleep(2) #waits 2 seconds before printing response
    print(random.choice(responses)) #chooses randomly from the bank of responses, and displays it
    print("\n") #creates new line 
answerQuery()

## Following asks user if they would like to play again, and loops until user is finished
secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: ")) #after first question is over, displays this text and asks for user input
while secondQuestion == str("Y"): #if you choose the string 'Y', runs answer query again, and repeats the loop
    answerQuery()
    secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: ")) 
else:
    print(input("Press any key to exit")) #if you choose 'N', it will display "press any key to exit" and asks for an input, although it is not specified, and program essentially ends after you press a key


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


import random
import time
# responses that the query will answer with when user has asked a questions 
responses = ["Not so sure", "4:20", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never",
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]

## Following function asks user question, then returns random results from responses
def answerQuery():
    question = input("Ask and you shall receive: ")
    print("Let me dig deep into the waters of life, and find your answer")
    #this is a random answer from the response from line 23 that the user gets when user asked question
    time.sleep(2)
    print("Hmmm")
    time.sleep(2)
   #this is a random answer that the user gets when user asked question 
    print(random.choice(responses))
  #this allows user to decicde if user wants to keep going with questions 
    print("\n") 
answerQuery()

## Following asks user if they would like to play again, and loops until user is finished

secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
#lets user pick Y for yes and N for n Had to add in the "N" because before it was only a Y which means you had no potion it would just leave the query
while secondQuestion == str("Y" or "N"):
    answerQuery()
    secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
else: 
   # when user aswered "N" lets user  leave 
    print(input("Press any key to exit"))
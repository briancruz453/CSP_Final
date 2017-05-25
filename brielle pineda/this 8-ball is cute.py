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

# ^ copyright and etc. stuff ^

# imported libraries
import random # random choice (for line 25)
import time # timing (not very necessary anymore but for line 33)

# responses for the 8-ball
responses = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never", "Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]

## Following function asks user question, then returns random results from responses - function answerQuery(): user is prompted to ask a question, and the program picks an answer from like 23 at random.
def answerQuery():
    question = raw_input("Ask and you shall receive: ") # this is where the user will input their question. I changed input() to raw_input() because input required you to put quotations
    print("Let me dig deep into the waters of life, and find your answer.") # this is so it seems like the 8-ball is thinking
    time.sleep(1) # I didn't like how long it took (I thought it broke canopy)
    print("Hmmm, please wait.") # to set the mood of the 8-ball is thinking
    time.sleep(1) # I didn't like how long it took (I thought it broke canopy)
    print(random.choice(responses)) # the program will pick an answer at random from line 23 and print it
    # print("\n") - line break; removed because it was a little unneccessary
answerQuery() # when the program runs, it will run answerQuery()

## Following asks user if they would like to play again, and loops until user is finished - makes the program reusable over and over again
secondQuestion = (raw_input("Would you like to ask the Wise One another question? Y/N: ")) # this is where the user will input whether to ask again
while secondQuestion == str("Y"): # while you keep putting "Y" as the input for the secondQuestion (only capital)
    answerQuery() # go back to line 36 and rinse and repeat
    secondQuestion = (raw_input("Would you like to ask the Wise One another question? Y/N: ")) # so the user can answer the second question again
'''else:
    print(input("Press any key to exit"))''' # unneccessary. now, if you put anything other than "Y", the program stops abruptly

# edited to make it work as dictated in question #3 in the readme
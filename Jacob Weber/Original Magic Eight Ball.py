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
responses = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never",
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]

## Following function asks user question, then returns random results from responses
def answerQuery():
    question = input("Ask and you shall receive: ")
    print("Let me dig deep into the waters of life, and find your answer")
    time.sleep(2)
    print("Hmmm")
    time.sleep(2)
    print(random.choice(responses))
    print("\n")
answerQuery()

## Following asks user if they would like to play again, and loops until user is finished
secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
while secondQuestion == str("Y"):
    answerQuery()
    secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
else:
    print(input("Press any key to exit"))
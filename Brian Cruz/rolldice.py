from __future__ import print_function ## Had to add this in order for line 49 to work properly

'''
This is Assignment 4
for Introduction to Computer Programming
by Kapp Craig @ NYU
Oct 9
'''
'''
Assignment Description:Rolling the dice
'''

# Step1: validate if input is a positive integer

# assume the user enters an improper number
user = False ## sets a variable to false
     
while(user == False):
    # prompt the user to input the number 
    dice = int(input("How many sides on your dice? "))
    # if input is an improper number, enter again.
    if dice <1 or dice > 6:
        user = False
        print("Sorry, that's not a valid size val-",'\n' 
              'ue. Please choose a positive number.')
    else:
        user = True
        print("Thanks! Here we go ...")

# Step2: rolling the dice until snake eyes
import random

# initial counter for times of rolling
t_counter = 0

# initial counter for times of "double"
d_counter = 0

# initial sum for dice #1
sum1 = 0

# initial sum for dice #2
sum2 = 0

# roll dice twice
n1 = random.randint(1,dice)
n2 = random.randint(1,dice)
print('1.',' die number 1 is', n1, 'and die number 2 is', n2, end ='. \n')
while n1 != 1 or n2 != 1:

    # account for times of 'doubles'
    if n1 == n2:
        d_counter += 1
    
      # calculate sum for dice #1
    sum1 = sum1 + n1
    # calculate sum for dice #2
    sum2 = sum2 + n2

    n1 = random.randint(1,dice)
    n2 = random.randint(1,dice)
    t_counter += 1
    print(t_counter,'.',' die number 1 is', n1, 'and die number 2 is', n2, end ='. \n')


   
aver1 = format(sum1/t_counter, ".2f")
aver2 = format(sum2/t_counter, ".2f")
print("You got snake eyes! Finally! On try number ", t_counter,'!')
print("Along the way you rolled doubles", d_counter, 'times')
print("The average roll for die #1 was", aver1)
print("The average roll for die #2 was", aver2)
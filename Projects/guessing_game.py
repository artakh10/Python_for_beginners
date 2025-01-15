'''
Soecifically for python beginners
Author: Arta Khosravi
Last edit: Jan. 2025
'''

from random import randrange
#import a random number first
number = randrange(0,100) 
#now to see if the guess is the number
while True: #if the audience has a guesses, start the loop
    i = int(input('Enter a number (0 - 100): '))
    if i == number:
        print('Yay! The number is ' + str(i))
        break #if the guess was true, dont restart the loop
    elif i < number : 
        print('Your number is lower than our number')
    else:
        print('Your number is greater than our number')
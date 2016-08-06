''''
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to 1000. You have to guess which number I picked.
Continuous loop.
Every time you guess wrong, I'll tell you whether the number is higher or lower.
'''
import random

guess_number = random.randint(1,1000)
keep_guessing = 0

while keep_guessing == 0:
    try:
        user_guess = int(raw_input("Pick a Number: "))
    except:
        print "Invalid Entry"
        continue

    if user_guess < guess_number:
        print "Your guess is LOWER"
    elif user_guess > guess_number:
        print "Your guess is HIGHER"
    else:
        print "Congrats. Your guess" , user_guess , "is CORRECT"
        keep_guessing = 1
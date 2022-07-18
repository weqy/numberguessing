import random # randomizer that we're using
list1 = [1, 2, 3, 4, 5, 6, 8, 9, 10] # all possible numbers

x = (random.choice(list1)) # the number for user to guess

answer=float(input("Guess a number from 1-10 : ")) # instructs user
if answer == x: # criteria for correct answer
    print("You guessed correctly!") # lets the user know they are correct
else: print("Try again! The correct answer was", x) # lets the user know they are incorrect + the correct answer
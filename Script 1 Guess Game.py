#Author Oskar Petersen

#Guess the number

import random
#vardef
minGuess = 1
maxGuess = 6
secretNumber = random.randint(minGuess, maxGuess);
#in the original code the secret number is generated after making a guess
#that seems kinda disingenuous to me

#Ask the user for their name and guess
name = input("What is your name? ");
print("Hi " + name);
while (True):
    print("Enter a number between", minGuess, "and", maxGuess);
    #the user enters their guess
    guess = int(input("What is your guess? "))
    if (guess == secretNumber):
        print("Congratulations! you are correct!");
        break;
    else:
        print("you lose - the number was", secretNumber);
    print("Thank you for playing");
    break;

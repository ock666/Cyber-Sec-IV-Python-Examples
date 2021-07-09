#number guessing game
#ask user for number between 1-10
#if they get it higher than the number we say lower etc.
#Made by Oskar Petersen 19/05/21

#import random number library
import random
num_rand = random.randint(1, 10);
#specify random number range to select from
#print(num_randy)
while (True):
    num_guess = int(input("Guess a number between 1 - 10 > "));
    #user inputs a guess
    if (num_guess == num_rand):
        print("Congrats u are right lmao");
        break;
    if (num_guess > num_rand):
        print("Lower ya goose");
    elif (num_guess < num_rand):
        print("higher ya derro");
print("thank you for playing")

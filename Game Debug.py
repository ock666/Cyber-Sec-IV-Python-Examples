import random
#vardef
minGuess = 1
maxGuess = 6
secret_number = random.randint(minGuess, maxGuess)

Name = input("what is your name? >");
print("Hi!"+ Name)
print("Enter a number between 1 and 6");
print(secret_number)
guess = int(input("What is your Guess? "));
if (guess == secret_number):
    print("Congrats u got it")
else:
    print("YOU LOSE - the number was", secret_number)
print("Thank you for playing")  
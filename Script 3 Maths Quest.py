#Author: Oskar Petersen
#Date: 07/06/2021
#Maths Quest Program 3


#Ask player their name
#Ask player for their choice of times tables in between 1-12
#If player number is out of range or invalid, return error and loop back
#Ask the player if they are ready to begin
#If player is not ready, prmopt again
#Output the time table the player selected
#Ask player if their answers are correct
#If player answered correctly, congratulate them
#If player had incorrect answers, wish better luck next time.


#Welcome the player and ask their name
print("Welcome to Times Tables Maths Quest")
name=input("What is your name? ")
print("Ok", name + ", Lets practise some times tables")

#Ask player for their choice of times table between 1 - 12
number=int(input("What times table do you want to practice today? 1 - 12: "))

#If player number is out of range, ask choice again (this stops the wise guys tryna break the program)
while number <1 or number >12:
    number=int(input("What times table do you want to practice today? 1 - 12: "))

#Ask player if they are ready to begin
inp = input("Are you ready y/n? ")

#If the player is not ready, ask again, and again and again (ad nauseum)
while inp == "n":
    inp = input("Are you ready y/n? ")

#Prints the times table the player selected once they are ready (or having stopped mashing 'N')
for i in range(1, 13):
    print(number, "*", i, "=", number*i)

#ask player if they got their answers correct (defs dont lie bro)
answer = input("Are your answers correct? y/n? ")

#If players answers were correct, congratulate them
if answer == "y":
    print("Nice one Einstein! thanks for playing Maths Quest")
    
#If player had wrong answer wish them better luck next time (and call them a goose)
else:
    print("Better luck next time ya goose")
    exit()
#end of program
#Author Oskar Petersen
#Rock Paper Scissors


#Players input their names here
print("Welcome to rock, paper scissors");
print("Please enter your names:");
Player1 = input("Player 1: What is your name?: ");
Player2 = input("Player 2: What is your name?: ");

print("Hello " + Player1 + " and " + Player2);
print(Player2 + " Look away from the screen!");
#Studies have confirmed that player 2 definitely does not look while Player 1 enters their answer
#Trust me bro

#Here the players inputs their chocie as r, p, or s
Player1Choice = input(Player1 + ": Enter your choice. r p or s: ")
print("Excellent, Cover your answer and ask player two to input their choice");
Player2Choice = input(Player2 + ": Enter your choice. r p or s: ")


#In case of a tied game
if Player1Choice == Player2Choice:
    print("Both Players have selected " + Player1Choice + " Its a tie.");
    
    
#Player 1 Chooses rock    
elif Player1Choice == "r":
    if Player2Choice == "s":
        print("Rock Smashes Scissors! " + Player1 + " Wins!");
        
    else:
        print("Paper Covers Rock! " + Player2 + " Wins!");
        
#Player 1 Chooses paper
elif Player1Choice == "p":
    if Player2Choice == "r":
        print("Paper Covers Rock! " + Player1 + " Wins!")
        
    else:
        print("Scissors Cut Paper! " + Player2 + " Wins!")
        
#Player 1 Chooses Scissors
elif Player1Choice == "s":
    if Player2Choice == "p":
        print("Scissors Cut Paper! " + Player1 + " Wins!");
        
    else:
        print("Rock Smashes Scissors! " + Player2 + " Wins!");
        
#End of Program thank you for playing etc.
print("Thank you for playing!")        
    
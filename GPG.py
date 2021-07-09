import os

print("This program can encrypt and decrypt PGP files \nThus simplifying the process from using commands");

while (True):
    option = input("Do you want to Encrypt or Decrypt?: e or d\n");
    if option == "e":
        print("Okay! We'll now enter the options for encrypting a file!\n");
        rec = input("Please enter the recievers email address\n");
        print("Here are a list of files in the current directory")
        os.system("ls");
        enfilename = input("Please input the name of the file you want to encrypt\n");
        os.system("gpg --encrypt --sign --armor -r "+ rec + " " + enfilename);
        break;
    if option == "d":
        print("Okay! We'll now enter the options for decrypting a file!\n");
        defilename = input("Please enter the name of the file you want to decrypt\n");
        decryptedfilename = input("Please enter the output filename for decryption\n")
        os.system("gpg --decrypt " + defilename + "> " + decryptedfilename);
        break;
    

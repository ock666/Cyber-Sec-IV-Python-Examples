import string
alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"


def decrypt():        
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    print()
    key = int(input("Enter key to decrypt: "))
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("Your decrypted message is:\n")
    print(decrypted_message)



#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

#check the above function

inp = input("Would you like to encrypt or decrypt text? e or d: ");
if inp == ('e'):
    text = input("Text to Encrypt: ");
    s = int(input("Enter a Shift: "));
    print("Text  : " + text);
    print("Shift : " + str(s));
    print("Cipher: " + encrypt(text,s));
    
elif inp == ('d'):
    decrypt()



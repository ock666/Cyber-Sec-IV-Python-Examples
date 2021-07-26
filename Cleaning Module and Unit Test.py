# Author: Oskar Petersen
# Date: 26/07/2021

# Algorithm
# have the user input a string of text
# first the program will convert all lower case characters to uppercase
# then the program will replace any instances of a . (period) with the letter X
# the program will then remove any spaces, symbols or digits.
# then the program will output a cleaned output that is appropriate for the encryption module.


#Module test table
#   INPUT                                        |        OUTPUT

#1  Hello There                                  |     HELLOTHERE                   # spaces removed
#2  beduwy HGB BJK ^%&5678                       |      BEDUWYHGBBJK                # letters uppercased symbols and spaces removed
#3  .........344343dwdewdew                      |     XXXXXXXXXDWDEWDEW            # periods replaced with X, numbers removed.
#4  https://mail.google.com/mail                 |     HTTPSMAILXGOOGLEXCOMMAIL     # symbols removed
#5  Hmm. We’re having trouble finding that site. |     HMMXWEREHAVINGTROUBLEFINDINGTHATSITEX  #spaces removed periods replaced
#6  it is your job to think deviously.           |     ITISYOURJOBTOTHINKDEVIOUSLYX # Spaces remove, periods replaced.
#7  !@#$%^&*()QWERTYUIOPasdfghjkl;''   nuwdiBYU  |     QWERTYUIOPASDFGHJKLNUWDIBYU  # text cleaned perfectly
#8  ASW$ED%XEDR%FGBY&}|{K   GY HB HB HB          |     ASWEDXEDRFGBYKGYHBHBHB       # spaces and symbols removed
#9  10036746328943...5743287034...573428.543     |     XXXXXXX                      # Digits removed. Periods replaced.
#10 :":"*#$(&$*&#*()@$&:":"<>?<><>?              |    " " <blank output>            # all chars removed  

#importing the replacement module
import re


#define the module "clean"
def clean(str):
    cleaned = ""
    uppertext = text.upper() #convert any lowercase characters to uppercase
    nodots = re.sub(r'\.', "X", uppertext) #substitute any dots (periods) with a capital X
    nospa = re.sub(r' ', "", nodots) #substitute any occurances of spaces with no character
    cleaned = re.sub('[^A-Za-z]+', '', nospa) #replace any numbers with no character
    return cleaned #returns the modules output
 

#Unit Tests
#Test1
text = "Hello There"
cleaned = clean("Hello There")
if cleaned == "HELLOTHERE":
    print(cleaned)
    print("Test 1 Okay")
else:
    print("Test 1 FAIL")
    
#Test 2
text = "beduwy HGB BJK ^%&5678"
cleaned = clean("beduwy HGB BJK ^%&5678")
if cleaned == "BEDUWYHGBBJK":
    print(cleaned)
    print("Test 2 Okay")
else:
    print("Test 2 FAIL")
    
#Test 3
text = ".........344343dwdewdew"
cleaned = clean(".........344343dwdewdew")
if cleaned == "XXXXXXXXXDWDEWDEW":
    print(cleaned)
    print("Test 3 Okay")
else:
    print("Test 3 FAIL")

#Test 4
text = "https://mail.google.com/mail"
cleaned = clean("https://mail.google.com/mail")
if cleaned == "HTTPSMAILXGOOGLEXCOMMAIL":
    print(cleaned)
    print("Test 4 Okay")
else:
    print("Test 4 FAIL")

#Test 5
text = "Hmm. We’re having trouble finding that site."
cleaned = clean("Hmm. We’re having trouble finding that site.")
if cleaned == "HMMXWEREHAVINGTROUBLEFINDINGTHATSITEX":
    print(cleaned)
    print("Test 5 Okay")
else:
    print("Test 5 FAIL")
    
#Test 6
text = "it is your job to think deviously."
cleaned = clean("it is your job to think deviously.")
if cleaned == "ITISYOURJOBTOTHINKDEVIOUSLYX":
    print(cleaned)
    print("Test 6 Okay")
else:
    print("Test 6 FAIL")
    
#Test 7
text = "!@#$%^&*()QWERTYUIOPasdfghjkl;''   nuwdiBYU"
cleaned = clean("!@#$%^&*()QWERTYUIOPasdfghjkl;''   nuwdiBYU")
if cleaned == "QWERTYUIOPASDFGHJKLNUWDIBYU":
    print(cleaned)
    print("Test 7 Okay")
else:
    print("Test 7 FAIL")
    
#Test 8
text = "ASW$ED%XEDR%FGBY&}|{K   GY HB HB HB"
cleaned = clean("ASW$ED%XEDR%FGBY&}|{K   GY HB HB HB")
if cleaned == "ASWEDXEDRFGBYKGYHBHBHB":
    print(cleaned)
    print("Test 8 Okay")
else:
    print("Test 8 FAIL")
    
#Test 9
text = "10036746328943...5743287034...573428.543"
cleaned = clean("10036746328943...5743287034...573428.543")
if cleaned == "XXXXXXX":
    print(cleaned)
    print("Test 9 Okay")
else:
    print("Test 9 FAIL")
    
#Test 10
text = "::*#$(&$*&#*()@$&::<>?<><>?"
cleaned = clean("::*#$(&$*&#*()@$&::<>?<><>?")
if cleaned == "":
    print(cleaned)
    print("Test 10 Okay")
else:
    print("Test 10 FAIL") 

    

#API user input for uncleaned text
#user string will be run through the clean module
#and return a string which will function with the encryption module
text = input("enter some lowercase text: ");
cleaned = clean(str(text))
print(cleaned)
    

    
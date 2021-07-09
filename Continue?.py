str_response = ""
#str_response = input("do you want to continue? (y/n)? >");
while (True):
    str_response = input("do you want to continue? (y/n)? >");
    if ((str_response != "y") or (str_response != "n")):
        print("try again");
        if (str_response != "y"):
            print("the end");
            break;

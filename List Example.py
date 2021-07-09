#this program will make my name upper and lowercase
str_name = "Jizz Emporer"
num_strlen = len(str_name)
#OsKaR
#print(str_name[num_strlen])
for count in range(num_strlen):
    if ((count % 2) == 0):
        print(str_name[count].upper(),end="");
    else:
        print(str_name[count].lower(),end="");

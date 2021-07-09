import subprocess # For executing shell commands
str_address = str(input("Whats IP you wanna ping bruh? >"));
subprocess.call("ping{}".format(str_address))

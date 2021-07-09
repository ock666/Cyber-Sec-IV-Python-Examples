import os

network = input ("Enter first 3 numbers of IP network, e.g. 1.2.3: ")
print(network)

for host in range (1, 254):
    print("pinging " + network + "." + str(host))
    os.system("ping -n 2 " + network + "." + str(host))
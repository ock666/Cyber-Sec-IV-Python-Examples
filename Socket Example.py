import socket
a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = str(input("what is the ip address to scan? >"));

for i in range(1, 65535):
    port = i;
    location = (host,port);
    
    result_of_check = a_socket.connect_ex(location)
    if result_of_check == 0:
        print("Port",port,"is open")
    else:
        print("Port",port,"Is not open")

a_socket.close()
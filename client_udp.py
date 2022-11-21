from socket import *

# Use AF_INET for IPv4 and SOCK_DGRAM for UDP
client_socket = socket(AF_INET, SOCK_DGRAM)

server_name = "localhost"
server_port = 12000
message = input("Enter a lowercase string:")

client_socket.sendto(message.encode(), (server_name, server_port))

modified_message, server_address = client_socket.recvfrom(2048)
print(modified_message.decode())

client_socket.close()

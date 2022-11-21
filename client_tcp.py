from socket import *

# Use AF_INET for IPv4 and SOCK_STREAM for TCP
client_socket = socket(AF_INET, SOCK_STREAM)

server_name = "localhost"
server_port = 12000
message = input("Enter a lowercase string:")

client_socket.connect((server_name, server_port))
client_socket.send(message.encode())

modified_message = client_socket.recv(1024)
print(modified_message.decode())

client_socket.close()

from socket import *

# Use AF_INET for IPv4 and SOCK_DGRAM for UDP
server_socket = socket(AF_INET, SOCK_DGRAM)

server_port = 12000
server_socket.bind(("", server_port))

print("Server ready...")

while True:
    encoded_message, client_address = server_socket.recvfrom(2048)
    modified_message = encoded_message.decode().upper()
    server_socket.sendto(modified_message.encode(), client_address)

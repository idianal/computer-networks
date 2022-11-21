from socket import *

# Use AF_INET for IPv4 and SOCK_STREAM for TCP
welcome_socket = socket(AF_INET, SOCK_STREAM)

welcome_port = 12000
welcome_socket.bind(("", server_port))
welcome_socket.listen(1)

print("Server ready...")

while True:
    connection_socket, connection_address = welcome_socket.accept()

    encoded_message = connection_socket.recv(1024)
    modified_message = message.decode().upper()
    connection_socket.send(modified_message.encode())

    connection_socket.close()

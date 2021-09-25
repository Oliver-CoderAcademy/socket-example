import socket
from classes import Message

# create socket:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# because we are the server, we need to bind and listen
server_socket.bind(("127.0.0.1", 65432))
server_socket.listen()

# once the client requests, we need to accept it:
connection, address = server_socket.accept()

while True:
    # receive some data
    data=connection.recv(1024)
    
    # if it's blank, break the loop
    if not data:
        break

    message = Message(repr(data))
    # otherwise, print it to screen
    print(message)

    # and then bounce it back to the client in uppercase
    connection.sendall(bytes(str(message).upper(), "utf-8"))

server_socket.close()
import socket
from classes import Message

# create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# because we are the client we need to connect to a listening server
client_socket.connect(("127.0.01", 65432))

# get some string as input
message_to_send = Message(input("What would you like to send to the server? \n"))

# send the message
client_socket.sendall(bytes(str(message_to_send), "utf-8"))

# get a response
received_message = Message(repr(client_socket.recv(1024)))

# print message
print(received_message)

client_socket.close()
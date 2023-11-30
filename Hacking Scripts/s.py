import socket

#create a tcp packet
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to a specific addresss and port
server_address = ('localhost', 1234)
server_socket.bind(server_address)

#listen for income communications
server_socket.listen(5)


while True:
    #accept a client connection
    client_socket, client_address = server_socket.accept()

    #receive and send data
    data = client_socket.recv(1024)
    client_socket.send(b"Received: " + data)

    #close the client socket
    client_socket.close()
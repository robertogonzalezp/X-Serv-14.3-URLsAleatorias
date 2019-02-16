#!/usr/bin/python3

"""
Roberto González Pérez.
r.gonzalezperez@alumnos.urjc.es
Programa que construye una aplicación web como server que devolverá URLs aleatorias.

"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Let the port be reused if no process is actually using it

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
# (in an infinite loop, almost you can stop the loop with Ctrl+C)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')

        # Generate a random number
        rndnumber = random.randrange(9999999)

        url = "<a href='http://localhost:1234/" + str(rndnumber) + "'>Dame otra</a>"

        recvSocket.send(bytes(b"HTTP/1.1 200 OK\r\n\r\n" +
                              b"<html><body><h1>Hello World!</h1>" +
                              url.encode() +
                              b"</body></html>" +
                              b"\r\n"))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
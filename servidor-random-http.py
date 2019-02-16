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
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
# (in an infinite loop, almost you can stop the loop with Ctrl+C)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print(recvSocket.recv(1024))
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')

        # Generate a random number
        rndnumber = random.randrange(1000000000)

        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                              "<html><body><h1>Hola. " +
                              "<a href=http://localhost:1234/" +
                              str(rndnumber) + ">Dame otra</a>" +
                              "</h1></body></html>" + "\r\n", "utf-8"))
    recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
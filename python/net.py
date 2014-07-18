#!/usr/bin/python

#Server

import socket
import sys
import pdb

#Send a string to a client
def sendMessage(csock, message):
	print('Transmitting', sys.getsizeof(message), "bytes")
	csock.send(bytes(str(sys.getsizeof(message)), "utf-8"))
	csock.send(bytes(message, "utf-8"))
	print("Transmission complete.")

#Initialize the server socket
print('Initializing...')
s = socket.socket()
host = socket.gethostname()
port = 32253
s.bind((host, port))
s.listen(5)
print('Ready.')

while True:
	#Connect to the client
	csock, addr = s.accept()
	print('\nGot connection from', addr)
	#Send banner message
	sendMessage(csock, 'Connected.\n\n')
	sendMessage(csock, 'Welcome to Blacklight Decrypto!')
	userInput = "initUserInput"
	userInput = input()
	while userInput != "quit" and userInput != "q" and userInput != "":
		sendMessage(csock, userInput)
		userInput = input()
	sendMessage(csock, '@end')
	#Close the connection
	csock.close()
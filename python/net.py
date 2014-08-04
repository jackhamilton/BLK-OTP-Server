#!/usr/bin/python

#Server

import socket
import sys
from rsa import *
from Crypto.Cipher import AES
import threading
import pdb
import time

#Send a string to a client
def sendMessage(csock, message):
	print('Transmitting', sys.getsizeof(message), "bytes")
	csock.send(bytes(str(sys.getsizeof(message)), "utf-8"))
	csock.recv(4)
	csock.send(bytes(message, "utf-8"))
	csock.recv(4)
	print('Transmission complete.')
def genRSAKeys():
	global generating
	generating = True
	global rsa
	rsa = generateKeyPairs(512)
	print('Keys generated.')
	generating = False
	
#Initialize the server socket
print('Initializing Blacklight OTP Server build 72...')
global rsa
print('Generating RSA keys...')
genRSAKeys()
s = socket.socket()
host = socket.gethostname()
port = 32253
s.bind((host, port))
s.listen(5)
print('Ready.')

while True:
	#Connect to the client
	if(generating):
		print('\nPlease wait for new RSA keys to be generated.')
		while(generating):
			time.sleep(.2)
	csock, addr = s.accept()
	print('\nGot connection from', addr)
	#Send banner message
	sendMessage(csock, 'Connected.\n')
	sendMessage(csock, 'Welcome to Blacklight OTP Server!')
	sendMessage(csock, '@end')
	sendMessage(csock, str(rsa[0][0]))
	sendMessage(csock, str(rsa[0][1]))
	len = csock.recv(16)
	aesKey = csock.recv(int(len.decode(encoding="utf-8")))
	aesKey = aesKey.decode(encoding="utf-8")
	print(rsadecrypt(int(aesKey), rsa[1]))
	aesKey = rsadecrypt(int(aesKey), rsa[1])
	csock.send(bytes('y', "utf-8"))
	length = csock.recv(16)
	input = csock.recv(int(length.decode(encoding="utf-8")))
	decrypt(
	#csock.send(bytes('y', "utf-8"))
	#print(pic)
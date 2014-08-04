#!/usr/bin/python

#Client

import socket
import sys

#Parse command line arguments
useFile = False;
file = "";
useIP = False;
ip = "";
for arg in sys.argv:
	if arg == "-f":
		useFile = True;
	elif useFile and file == "":
		file = arg;
	elif len(arg) >= 11 and len(arg) <= 15:
		useIP = True;
		ip = arg;
		
print("Initializing...")
#Socket initialization
s = socket.socket()
host = socket.gethostname()
if useIP:
	host = ip
port = 32253
print("Initialized on", host, ":", port)

#Connect and receive the banner messages
s.connect((host, port))
msg = 'initMsg'
while msg != '@end':
	length = int(s.recv(8))
	s.send(bytes('y', "utf-8"))
	msg = s.recv(length)
	msg = msg.decode(encoding="utf-8")
	s.send(bytes('y', "utf-8"))
	if msg != '@end':
		print(msg)
print("Connection closed.")
s.close()
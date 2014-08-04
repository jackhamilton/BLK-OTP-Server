#!/usr/bin/python
import hashlib

def sha1(msg):
	return hashlib.sha1(msg).hexdigest()
	
def sha224(msg):
	return hashlib.sha224(msg).hexdigest()

def sha256(msg):
	return hashlib.sha256(msg).hexdigest()

def sha384(msg):
	return hashlib.sha384(msg).hexdigest()

def sha512(msg):
	return hashlib.sha512(msg).hexdigest()
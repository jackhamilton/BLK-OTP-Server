#!/usr/bin/python

from prime import *
from fractions import gcd

__publicKey = [0,0]
__privateKey = [0,0]

def getPublicKey():
	return __publicKey
	
def getPrivateKey():
	return __privateKey

#Generate a pair of RSA keys of the given bitlength. Returns a multidimensional array [Public key],[Private Key] formatted as [n, e] and [n, d] respectively.
def generateKeyPairs(bits):
	p = genPrime(bits, 20)
	q = genPrime(bits, 20)
	n = p*q
	phi = (p-1)*(q-1)
	e = genPrime(bits-1, 20)
	while (not gcd(e, phi) == 1):
		e = genPrime(bits-1, 20)
	d = modinv(e, phi)
	global __publicKey
	global __privateKey
	__publicKey = [n, e]
	__privateKey = [n, d]
	return [__publicKey, __privateKey]

#Encrypt a given integer with the given public key, formatted as the array of [n, e].
def rsaencrypt(msg, publicKey):
	return pow(msg, publicKey[1], publicKey[0])

#Decrypt a given integer with the given private key, formatted as the array of [n, d].
def rsadecrypt(msg, privateKey):
	return pow(msg, privateKey[1], privateKey[0])
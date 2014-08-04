#!/usr/bin/python

#A collection of functions related to the determination of massive prime numbers.

import random
import math

def genRandInRange(min, max):
	return random.SystemRandom().randint(min, max)
		
def fermat(p):
	a = genRandInRange(2, p - 1)
	if (pow(int(a),int(p-1), p) == 1):
		return True
	else:
		return False
		
def millerRabin(n, k):
	s = n - 1
	d = 0
	while (s % 2 == 0):
		d += 1
		s //= 2
	for _ in range(k):
		a = genRandInRange(2, n - 1)
		x = pow(a, s, n)
		if (x == 1 or x == n-1):
			continue
		for _ in range(d - 1):
			x = pow(x, 2, n)
			if x == n-1:
				break
		else:
			return False
	return True
	
def genPrime(bits, rabinIterations):
	seed = random.SystemRandom().getrandbits(bits)
	while (int(math.log(seed, 2)) + 1 != bits or seed % 2 == 0 or seed <= 2):
		seed = random.SystemRandom().getrandbits(bits)
	passesRabin=False;
	while (not passesRabin):
		while (not fermat(seed)):
			seed -= 2
		if (millerRabin(seed, rabinIterations)):
			passesRabin = True
		else:
			seed -= 2
	return seed
		
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('Modular inverse does not exist.')
	else:
		return x % m
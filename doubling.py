#!/usr/bin/python
#acleetus

def doubling(rate):
	low = 0.
	high = 10000.
	guess = 5000.
	guess_error = 5000.
	p =1.

	while (guess_error>0.001):
		if ((p*((1+rate)**(guess)))-2*p)>=0:
			high = guess
		else:
			low = guess
		guess = (high+low)/2.
		guess_error = (high-low)/2.
	return guess

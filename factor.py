#!/usr/bin/python
#acleetus

def factor(n):
	dividend = n
	possible_factor = 2 
	factors = []

	while(dividend != 1):
		if (dividend%possible_factor == 0):
			factors.append(possible_factor)
			dividend = (dividend/possible_factor) 
		else: 
			possible_factor+=1
	return factors


#!/usr/bin/python
#acleetus

def triangle(n):
	for x in range(n):
		for y in range(n-x):
			print " ",
		for z in range(2*x-1):
			print "*",
		print ""

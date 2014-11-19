#!/usr/bin/python
#acleetus

def generateMultiples(number, start):
	value = start
	while True:
		yield value
		value += number

g = generateMultiples(3, 27)

for x in range (0, 19):
	print next(g)

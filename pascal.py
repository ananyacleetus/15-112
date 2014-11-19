#!/usr/bin/python
#acleetus 

from factorial import factorial 


def pascal(n):
	triangle = []
	currentRow=[]
	for i in range(1,n):
		for j in range(1,n):
			val = (factorial(i)) / ((factorial(j)) * factorial((i-j)))
			if val !=0:		
				currentRow.append(val)
		triangle.append(currentRow)
		currentRow =[1]
	for row in triangle:
	     print("{: >3} {: >3} {: >3}".format(*row))

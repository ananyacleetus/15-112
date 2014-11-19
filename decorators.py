#!/usr/bin/python
#acleetus 

class LessThanZero(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):	
		return repr(self.value)

def nonNegative(function):
	 #this is just like the example one
	def checkZero(*numbers):
		for x in numbers:
			if x < 0:
				raise LessThanZero("ERROR! This is less than zero")
		return function(*numbers)
	return checkZero

def allCaps(function):
	def caps(*words):
		#same but with words
		w = []
		for word in words:
			w.append(word.upper())
			#needs list because returning list of capitalized words
		return function(*w)
	return caps
			
def testingDecorators():
	print "Testing Decorators..."
	try: 
		nonNegative(3,6,-2,5)
	except LessThanZero:
		print "Exception caught. This works."
	setA = set(allCaps("mother", "kitten", "pizza"))
	setB= set("MOTHER", "KITTEN", "PIZZA")
   if(setA==setB):
		print "All tests passed!"
	else: 
		print "AllCaps failed"

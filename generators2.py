#!/usr/bin/python
#acleetus

def wordsFromFile(fileName):
	openedFile = open(fileName)
	for line in openedFile.readlines():
		#omg please work
		for word in line.split():
			#default splits by space
			yield word

def noPunctuation(wordGenerator):
	while True:
		word = wordGenerator.next()
		#generator
		word = word.replace(",", "")
		word = word.replace(".", "")
		word = word.replace("-", "")
		#all of these replace with nothingness
		word = word.replace(":", "")
		word = word.replace(";", "")
		yield word

def allCaps(wordGenerator):
	while True:
		word = wordGenerator.next()
		word = word.upper()
		yield word

pl = allCaps(noPunctuation(wordsFromFile("words.txt")))
#takes words, removes punctuation, THEN capitalizes

s = set()
for word in pl:
	s.add(word)
	#adds it to set
print s

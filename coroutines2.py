#!/usr/bin/python
#acleetus

words = set()
#i dont like initializing sets

def getWordsfromUser():
	while True:
		words.add((yield))
		#give me a word

def noPunctuation(w):
	while True:
		word = (yield)
        word = word.replace(",", "")
		word = word.replace(".", "")
		word = word.replace("-", "")
		#all of these replace with nothingness
		word = word.replace(":", "")
		word = word.replace(";", "")
		w.send(word)

def allCaps(w):
	while True:
		word = (yield)
		word = word.upper()
		#same as generator
		w.send(word)


g = addWord()
g.next()

caps = allCaps(g)
caps.next()

punct = noPunctuation(caps)
punct.next()
	
for line in open("words.txt").readlines():
	for word in line.split():
		punct.send(word)

print words

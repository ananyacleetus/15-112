#!/usr/bin/python
#acleetus

def capitalize():
	while True:
		word = (yield)
		word = word.upper()
		print word

c = capitalize()
c.next()
c.send("The quick brown fox jumped over the lazy old dog.")
#lol isnt it jumps not jumped?



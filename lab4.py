#!/usr/bin/python
#acleetus


import collections 
from collections import Counter

def readBook(string):
	book=tuple(string.split(','))
	if len(book) !=5:
		raise ValueError("This book has the wrong number of items")
	return book

def readBooks(filename):
	bookList = []
	for line in open(filename):
		book = readBook(line.strip())
		bookList.append(book)
	return bookList

def builtIndex(list):
	index = {}
	bookList = []
	for book in list:
		title = tuple(book[2].lower().split())
		for x in xrange(len(title)):
			word = title[x]
			if (word is not "a" and word is not "an" and word is not "the"):
				if word in index.keys():
					index[word].append(book[2])
				else: 
					index[word]=[book[2]]
	return index

def lookupKeyword(dictionary, string):
	keywordMatch ={}
	keywords = tuple(string.lower().split(','))	
	for x in xrange(len(keywords)):
		word = keywords[x]
		if word in dictionary.keys():
			keywordMatch[word] = dictionary[word]
	allTitles = []
	allTitles.append(keywordMatch.values())
	titles=[]
	for x in allTitles:
  	  for y in x:
		titles.append(y)
	counter = collections.Counter(titles)	
	counter.most_common()
	if len(titles) == 0:
		raise NoResultsError('No results. Please try again.')
	else:
		return books

def presentMenuAndGetChoice():
	while (True):
		option =raw_input("Press 'i' to initialize an index, press 's' to query and index, or 'q' to quit ")
		if (option == 'Q') or (option == 'q'):
			print "Bye bye"
			break
		elif (option == 'i') or (option == 'I'):
			fileName = raw_input("Enter file name: ")
			try:
					fileRead = readBooks(fileName)
					print "Index has been created." 
			except IOError:
					print "File not found. Please try again."
			except ValueError as ve:	
					print ve.value
		elif (option == 's') or (option == 'S'):
			search =raw_input("Type search keywords")
			try:
					print lookupKeyword(buildIndex(fileRead), search)
			except NoResultsError as nre:
					print nre.value
		else:
			print "This is not an option. Please try again."
 
anan= readBooks('books.txt')
presentMenuAndGetChoice




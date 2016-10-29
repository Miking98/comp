'''
	Michael Wornow
	Crimson Tech Comp
	Asst 1
'''

import collections

def swapchars(string):
	mostCommon = ""
	leastCommon = ""
	for c in collections.Counter(string.lower()).most_common():
		if c[0].isalpha():
			mostCommon = c[0]
	for c in reversed(collections.Counter(string.lower()).most_common()):
		if c[0].isalpha():
			leastCommon = c[0]
	newString = ""
	for index, char in enumerate(string):
		if char.lower()==mostCommon:
			if char.islower():
				newString += leastCommon.lower()
			else:
				newString += leastCommon.upper()
		elif char.lower()==leastCommon:
			if char.islower():
				newString += mostCommon.lower()
			else:
				newString += mostCommon.upper()
		else:
			newString += char
	return newString

def sortcat(n, *args):
	strings = sorted(args)
	if n==-1:
		n = len(strings)

	newString = ""
	for i, s in enumerate(strings):
		if i==n:
			break
		else:
			newString += s

	return newString

def genStatesDict(file):
	states = {}
	with open(file) as f:
		for line in f:
			info = line.rstrip().split(",")
			states[info[1]] = info[0]
	return states

def bluesclues(abbr, file):
	states = genStatesDict(file)
	return states[abbr]

def bluesbooze(state, file):
	states = genStatesDict(file)
	for key, value in states.iteritems():
		if value == state:
			return key

print swapchars('I\'m just a chi-town coder with a nice flow.')
print sortcat(1, 'abc', 'bc')
print sortcat(2, 'bc', 'c', 'abc')
print bluesclues('AL', 'states.txt')
print bluesbooze('Nebraska', 'states.txt')
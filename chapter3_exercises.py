# Exercises for chapter 3:

# Name: Stephanie Frias

#3.1 The script results in the following error: NameError: name 'repeat_lyrics' is not defined

#3.2 Despite switching the order of the definitions, the script still produces the correct results and prints the lyrics twice. 

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

repeat_lyrics()

#3.3

def right_justify (s):
	print ' '*(70-len(s)) + s

right_justify ('allen')

#3.4.1 

def do_twice(f):
	f()
	f()

def  print_spam():
	print 'spam'

do_twice(print_spam)

#3.4.2 - #3.4.5

def do_twice(f,value):
	f(value)
	f(value)

def print_twice(string):
	print string
	print string

do_twice(print_twice,'spam')

def do_four(f,value2):
	do_twice(f,value2)
	do_twice(f, value2)
	
do_four(print_twice,'spam')
# Python Review Part 1 - Strings and string-slicing.
# See the file HW1_QuickPythonReview.pdf for additional commentary, sample output and hints.


print "\n\nLet's check our version of Python and your Platform"
import sys;
print('Python %s on %s' % (sys.version, sys.platform))

print "\nWhat is the prefix used to find the python library?"
print sys.prefix

print("\nLet's get more info on our version.")
print sys.subversion

print("\nIs there a subversion?")
print sys.subversion

print("\nWhat are the built-in modules?")
print sys.builtin_module_names

print("\nWhat is the executable?")
print sys.executable

print "\nWhat are the loaded modules. This is a dynamic object!"
print sys.modules


# ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~


print "\n\nPython Review Part 1 - Strings and string-slicing."
print "See the file HW1_QuickPythonReview.pdf for additional commentary, sample output and hints."

import string
print "\nUncomment the next line to see help showing the functions available from the string module."
# help(string)


print "EXERCISES Part 1 of Review - Strings and String Slicing"
s = 'catfish hatchery'
# Tip: Use repr() when you print, so we can see the enclosing quotes.
# This will help verify there are no extraneous spaces.

print "\n1. Using string-slicing, print out just the  word 'cat' from the larger phrase '%s'" % s
print "Answer:\t\t",

# 1. Add code here to extract 'cat' and print it here. Use repr() so we can see your answer in quotes.
repr(s[0:2])
print s[0:3]

print "\n2. Using string-slicing, print out just the  word 'fish'."
print "Answer:\t\t",
# 2. Add code here to extract 'fish' and print it here. Use repr() so we can see your answer in quotes.
repr(s[3:6])
print s[3:7]

print "\n3. Using string-slicing in the form s[m:], print out just the  word 'hatchery'."
m = s.find('hatch')
print 'The desired index is:', m
print "Answer:\t\t",
# 3. Add code here to extract 'hatchery' and print it here. Use repr() so we can see your answer in quotes.
print s[m:]

print "\n4. Count the number of h's in s, defined above. Use the count() method. "
print "Answer:\t\t",
# 4. Add your code here and be sure to print out the answer using a full sentence.
b = s.count('h')
print b


print "\n5. Count the number of vowels in 'catfish hatchery', using a for loop. Do not use the count() method."
print "Answer:\t\t",
s = 'catfish hatchery'
counter = 0
target = 'aeiouAEIOU'

# 5. Add your code here using a for loop to step through each character ch in the  string, and an if statement
# to see if that character is in the target string. If it is, increase counter by 1.
for n in range(len(s)):
	for t in range(len(target)):
		if target[t] in s[n]:
			counter = counter + 1
print counter



print "\n6. Use the upper() method to convert these initials to all upper case."
# Print out "I live in the USA." using the result and a %s format flag.
country = "usa"
# 6. Add your code here for exercise 6.
country = country.upper()
print 'I live in the %s', country



print '\n7. Convert the country below to the more proper form: "United States of America" using title().'
# Then use replace() to convert the resulting big 'O' back to a small 'o'.
country = "united states of america"
# 7. Add two lines here, first using title() and then using replace() to make 'O' small again.
country = country.title()
print country
country = country.replace('O','o',1)
print country

print "\n8. Find out which of these words startswith() 'dog', endswith() 'fish' or contains() 'cat'."
word1 = "dogcatcher"
word2 = "dogfish"
word3 = "dogberry"
word4 = "berryfish"
word5 = "dogcatfish"
words = [word1, word2, word3, word4, word5]
# A. Find the words that start with 'dog' here. Use a for loop.
# Add your code for exercise 8A here.
list = []
for x in range(len(words)):
	v = words[x]
	if v[0:3] == 'dog':
		list.append(v)

print 'These words begin with dog'
for p in list: print p


# B. Find the words that end with 'fish' here. Use a for loop.
list2 = []
for z in range(len(words)):
	c = words[z]
	m = c.find('fish')
	if m >0:
		if c[m:] == 'fish':
			list2.append(c)

print 'These words end with fish'
for p in list2: print p


# C. Find the words that contain 'cat' here. Use the "in" operator.
list3 = []
for r in range(len(words)):
	m = words[r]
	if 'cat' in m:
		list3.append(m)

print "These words contain 'cat'"
for p in list3: print p




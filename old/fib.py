#!/usr/bin/python
import time
print " --------------------------------"
print "| Fibonaacci Sequence Generator  |"
print " --------------------------------"
n = input("Please enter a number of terms: ")
a, b, c = 0, 1, 1
if c <= n:
	print c, ". ", a
	a, b, c = b, a+b, c+1
else:
	time.sleep(5)
	exit()

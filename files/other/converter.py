#!/usr/bin/env python

"""
A very messy TUI programme which allowed for converting between
lots of different types of units. Tried porting this to Android
via the API mentioned in `android.py` at one point, but that was
never finished.
"""

import time
print " ---------------"
print "| The Converter |"
print " ---------------"
print "Welcome to the Converter!"
print ""
print "To navigate the interface, simply type in the"
print "number that coresponds to what you wish to do."
print ""
print "To go back to the main menu, simply type anything"
print "which isn't a command into the entry space."
print ""
a = 1
while a == 1:
    try:
	print ""
	print "Please select what type of units you wish to convert today"
	print ""
	print "1.  Length"
	print "2.  Area"
	print "3.  Volume"
	print "4.  Mass"
	print "5.  Speed"
	print "6.  Temperature"
	print "7.  Time"
	print ""
	n = int(raw_input("Choose a catagory : "))
	if n == 1:
		b = 1
		while b == 1:	
			print ""
			print ""
			print "What is the unit you wish to convert from?"
			print ""
			print "1.  Kilometre"
			print "2.  Metre"
			print "3.  Centimetre"
			print "4.  Millimetre"
			print "5.  Mile"
			print "6.  Inch"
			print "7.  Foot"
			print "8.  Yard"
			print ""
			n = int(raw_input("Choose a unit : "))
			if n == 1:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Metre"
					print "2.  Centimetre"
					print "3.  Millimetre"
					print "4.  Mile"
					print "5.  Inch"
					print "6.  Foot"
					print "7.  Yard"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilometres : ")
							print "Metres:", n * 1000
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilometres : ")
							print "Centimetres:", n * 100000
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilometres : ")
							print "Millimetres:", n * 1000000
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilometres : ")
							print "Miles:", n * 0.6214
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilometres : ")
							print "Inches:", n * 39370
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilometres : ")
							print "Feet:", n * 3281
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilometres : ")
							print "Yards:", n * 1094
					else:
						c = c+1
			if n == 2:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Kilometre"
					print "2.  Centimetre"
					print "3.  Millimetre"
					print "4.  Mile"
					print "5.  Inch"
					print "6.  Foot"
					print "7.  Yard"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Metres : ")
							print "Kilometres:", n * 0.001
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Metres : ")
							print "Centimetres:", n * 100
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Metres : ")
							print "Millimetres:", n * 1000
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Metres : ")
							print "Miles:", n * 0.0006214
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Metres : ")
							print "Inches:", n * 39.37
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Metres : ")
							print "Feet:", n * 3.281
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Metres : ")
							print "Yards:", n * 1.094
					else:
						c = c+1
			if n == 3:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Kilometre"
					print "2.  Metre"
					print "3.  Millimetre"
					print "4.  Mile"
					print "5.  Inch"
					print "6.  Foot"
					print "7.  Yard"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Centimetres : ")
							print "Kilometres:", n * 0.00001
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Centimetres : ")
							print "Metres:", n * 0.01
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Centimetres : ")
							print "Millimetres:", n * 10
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Centimetres : ")
							print "Miles:", n * 0.000006214
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Centimetres : ")
							print "Inches:", n * 0.3937
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Centimetres : ")
							print "Feet:", n * 0.03281
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Centimetres : ")
							print "Yards:", n * 0.01094
					else:
						c = c+1
			if n == 4:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Kilometre"
					print "2.  Metre"
					print "3.  Centimetre"
					print "4.  Mile"
					print "5.  Inch"
					print "6.  Foot"
					print "7.  Yard"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Millimetres : ")
							print "Kilometres:", n * 0.000001
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Millimetres : ")
							print "Metres:", n * 0.001
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Millimetres : ")
							print "Centimetres:", n * 0.1
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Millimetres : ")
							print "Miles:", n * 0.0000006214
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Millimetres : ")
							print "Inches:", n * 0.03937
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Millimetres : ")
							print "Feet:", n * 0.003281
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Millimetres : ")
							print "Yards:", n * 0.001094
					else:
						c = c+1
			if n == 5:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Kilometre"
					print "2.  Metre"
					print "3.  Centimetre"
					print "4.  Millimetre"
					print "5.  Inch"
					print "6.  Foot"
					print "7.  Yard"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Miles : ")
							print "Kilometres:", n * 1.609
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Miles : ")
							print "Metres:", n * 1609
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Miles : ")
							print "Centimetres:", n * 160900
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Miles : ")
							print "Millimetres:", n * 1609000
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Miles : ")
							print "Inches:", n * 63360
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Miles : ")
							print "Feet:", n * 5280
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Miles : ")
							print "Yards:", n * 1760
					else:
						c = c+1
			if n == 6:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Kilometre"
					print "2.  Metre"
					print "3.  Centimetre"
					print "4.  Millimetre"
					print "5.  Mile"
					print "6.  Foot"
					print "7.  Yard"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Inches : ")
							print "Kilometres:", n * 0.0000254
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Inches : ")
							print "Metres:", n * 0.0254
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Inches : ")
							print "Centimetres:", n * 2.54
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Inches : ")
							print "Millimetres:", n * 25.4
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Inches : ")
							print "Miles:", n * 0.00001578
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Inches : ")
							print "Feet:", n * 0.08333
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Inches : ")
							print "Yards:", n * 0.2777
					else:
						c = c+1
			if n == 7:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Kilometre"
					print "2.  Metre"
					print "3.  Centimetre"
					print "4.  Millimetre"
					print "5.  Mile"
					print "6.  Inch"
					print "7.  Yard"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Feet : ")
							print "Kilometres:", n * 0.0003048
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Feet : ")
							print "Metres:", n * 0.3048
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Feet : ")
							print "Centimetres:", n * 30.48
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Feet : ")
							print "Millimetres:", n * 304.8
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Feet : ")
							print "Miles:", n * 0.0001894
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Feet : ")
							print "Inches", n * 12
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Feet : ")
							print "Yards:", n * 0.3334
					else:
						c = c+1
			if n == 8:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Kilometre"
					print "2.  Metre"
					print "3.  Centimetre"
					print "4.  Millimetre"
					print "5.  Mile"
					print "6.  Inch"
					print "7.  Feet"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Yards : ")
							print "Kilometres:", n * 0.0009144
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Yards : ")
							print "Metres:", n * 0.9144
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Yards : ")
							print "Centimetres:", n * 91.44
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Yards : ")
							print "Millimetres:", n * 914.4
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Yards : ")
							print "Miles:", n * 0.0005682
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Yards : ")
							print "Inches", n * 36
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Yards : ")
							print "Feet:", n * 3
					else:
						c = c+1
	if n == 2:
		b = 1
		while b == 1:
			print ""
			print ""
			print "What is the unit you wish to convert from?"
			print ""
			print "1.  Square Kilometre"
			print "2.  Square Metre"
			print "3.  Square Centimetre"
			print "4.  Acre"
			print "5.  Square Mile"
			print "6.  Square Foot"
			print "7.  Square Inch"
			print ""
			n = int(raw_input("Choose a unit : "))
			if n == 1:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Square Metre"
					print "2.  Square Centimetre"
					print "3.  Acre"
					print "4.  Square Mile"
					print "5.  Square Foot"
					print "6.  Square Inch"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Kilometre : ")
							print "Square Metres:", n * 1000000
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Kilometre : ")
							print "Square Centimetres:", n * 10000000000
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Kilometre : ")
							print "Acres:", n * 247.1
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Kilometre : ")
							print "Square Miles:", n * 0.3861
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Kilometre : ")
							print "Square Feet:", n * 10760000
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Kilometre : ")
							print "Square Inches:", n * 1550000000
					else:
						c = c+1
			if n == 2:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Square Kilometre"
					print "2.  Square Centimetre"
					print "3.  Acre"
					print "4.  Square Mile"
					print "5.  Square Foot"
					print "6.  Square Inch"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Metre : ")
							print "Square Kilometres:", n * 0.000001
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Metre : ")
							print "Square Centimetres:", n * 10000
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Metre : ")
							print "Acres:", n * 0.0002471
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Metre : ")
							print "Square Miles:", n * 0.0000003861
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Metre : ")
							print "Square Feet:", n * 10.76
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Metre : ")
							print "Square Inches:", n * 1550
					else:
						c = c+1
			if n == 3:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Square Kilometre"
					print "2.  Square Metre"
					print "3.  Acre"
					print "4.  Square Mile"
					print "5.  Square Foot"
					print "6.  Square Inch"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Centimetre : ")
							print "Square Kilometres:", n * (10 ** -10)
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Centimetre : ")
							print "Square Metres:", n * 0.0001
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Centimetre : ")
							print "Acres:", n * 2.471 * (10 ** -8)
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Centimetre : ")
							print "Square Miles:", n * 3.861 * (10 ** -11)
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Centimetre : ")
							print "Square Feet:", n * 0.001076
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Centimetre : ")
							print "Square Inches:", n * 0.1550
					else:
						c = c+1
			if n == 4:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Square Kilometre"
					print "2.  Square Metre"
					print "3.  Square Centimetre"
					print "4.  Square Mile"
					print "5.  Square Foot"
					print "6.  Square Inch"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Acres : ")
							print "Square Kilometres:", n * 0.004047
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Acres : ")
							print "Square Metres:", n * 4047
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Acres : ")
							print "Square Centimetres:", n * 2.471 * 40470000
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Acres : ")
							print "Square Miles:", n * 0.001562
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Acres : ")
							print "Square Feet:", n * 43560
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Acres : ")
							print "Square Inches:", n * 6273000
					else:
						c = c+1
			if n == 5:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Square Kilometre"
					print "2.  Square Metre"
					print "3.  Square Centimetre"
					print "4.  Acre"
					print "5.  Square Foot"
					print "6.  Square Inch"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Miles : ")
							print "Square Kilometres:", n * 2.590
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Miles : ")
							print "Square Metres:", n * 2590000
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Miles : ")
							print "Square Centimetres:", n * 25900000000
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Miles : ")
							print "Acres:", n * 640
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Miles : ")
							print "Square Feet:", n * 27878400
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Miles : ")
							print "Square Inches:", n * 4014489600
					else:
						c = c+1
			if n == 6:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Square Kilometre"
					print "2.  Square Metre"
					print "3.  Square Centimetre"
					print "4.  Acre"
					print "5.  Square Mile"
					print "6.  Square Inch"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Feet : ")
							print "Square Kilometres:", n * 9.29 * (10 ** -8)
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Feet : ")
							print "Square Metres:", n * 0.09290
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Feet : ")
							print "Square Centimetres:", n * 929
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Feet : ")
							print "Acres:", n * 0.00002296
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Feet : ")
							print "Square Miles:", n * 3.587 * (10 ** -8)
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Feet : ")
							print "Square Inches:", n * 144
					else:
						c = c+1
			if n == 7:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Square Kilometre"
					print "2.  Square Metre"
					print "3.  Square Centimetre"
					print "4.  Acre"
					print "5.  Square Mile"
					print "6.  Square Foot"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Inches : ")
							print "Square Kilometres:", n * 6.4516 * (10 ** -10)
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Inches : ")
							print "Square Metres:", n * 0.00064516
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Inches : ")
							print "Square Centimetres:", n * 6.4516
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Inches : ")
							print "Acres:", n * 0.0000001594
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Inches : ")
							print "Square Miles:", n * 2.491 * (10 ** -10)
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Square Inches : ")
							print "Square Feet:", n * 0.006944
					else:
						c = c+1
	if n == 3:
		b = 1
		while b == 1:	
			print "Volume - InDev"
			print ""
			print ""
			break
	if n == 4:
		b = 1
		while b == 1:	
			print ""
			print ""
			print "What is the unit you wish to convert from?"
			print ""
			print "1.  Tonne"
			print "2.  Kilogram"
			print "3.  Gram"
			print "4.  Long Ton"
			print "5.  Short Ton"
			print "6.  Pound"
			print "7.  Ounce"
			print "8.  Stone"
			print ""
			n = int(raw_input("Choose a unit : "))
			if n == 1:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Kilogram"
					print "2.  Gram"
					print "3.  Long Ton"
					print "4.  Short Ton"
					print "5.  Pound"
					print "6.  Ounce"
					print "7.  Stone"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Tonnes : ")
							print "Kilograms:", n * 1000
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Tonne : ")
							print "Grams:", n * 1000000
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Tonne : ")
							print "Long Ton:", n * 0.9842
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Tonne : ")
							print "Short Ton:", n * 1.1023
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Tonne : ")
							print "Pound:", n * 2204
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Tonne : ")
							print "Ounces:", n * 35274
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Tonne : ")
							print "Stone:", n * 157.5
					else:
						c = c+1
			if n == 2:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Tonne"
					print "2.  Gram"
					print "3.  Long Ton"
					print "4.  Short Ton"
					print "5.  Pound"
					print "6.  Ounce"
					print "7.  Stone"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilograms : ")
							print "Tonnes:", n * 0.001
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilograms : ")
							print "Grams:", n * 1000
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilograms : ")
							print "Long Ton:", n * 0.0009842
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilograms : ")
							print "Short Ton:", n * 0.0011023
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilograms : ")
							print "Pound:", n * 2.205
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilograms : ")
							print "Ounces:", n * 35.274
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilograms : ")
							print "Stone:", n * 0.1575
					else:
						c = c+1
			if n == 3:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Tonne"
					print "2.  Kilogram"
					print "3.  Long Ton"
					print "4.  Short Ton"
					print "5.  Pound"
					print "6.  Ounce"
					print "7.  Stone"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Grams : ")
							print "Tonnes:", n * 0.000001
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Grams : ")
							print "Kilograms:", n * 0.001
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Grams : ")
							print "Long Ton:", n * 0.0000009842
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Grams : ")
							print "Short Ton:", n * 0.0000011023
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Grams : ")
							print "Pound:", n * 0.0022046
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Grams : ")
							print "Ounces:", n * 0.03527
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Grams : ")
							print "Stone:", n * 0.000157
					else:
						c = c+1
			if n == 4:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Tonne"
					print "2.  Kilogram"
					print "3.  Grams"
					print "4.  Short Ton"
					print "5.  Pound"
					print "6.  Ounce"
					print "7.  Stone"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Long Ton : ")
							print "Tonnes:", n * 1.016
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Long Ton : ")
							print "Kilograms:", n * 1016
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Long Ton : ")
							print "Grams:", n * 1016047
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Long Ton : ")
							print "Short Ton:", n * 1.12
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Long Ton : ")
							print "Pound:", n * 2240
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Long Ton : ")
							print "Ounces:", n * 35840
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Long Ton : ")
							print "Stone:", n * 160
					else:
						c = c+1
			if n == 5:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Tonne"
					print "2.  Kilogram"
					print "3.  Gram"
					print "4.  Long Ton"
					print "5.  Pound"
					print "6.  Ounce"
					print "7.  Stone"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Short Ton : ")
							print "Tonnes:", n * 0.9072
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Short Tons : ")
							print "Kilograms:", n * 907.2
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Short Tons : ")
							print "Grams:", n * 907185
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Short Tons : ")
							print "Long Tons:", n * 0.8929
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Short Tons : ")
							print "Pounds:", n * 2000
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Short Tons : ")
							print "Ounces:", n * 32000
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Short Tons : ")
							print "Stones:", n * 142.857
					else:
						c = c+1
			if n == 6:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Tonne"
					print "2.  Kilogram"
					print "3.  Gram"
					print "4.  Long Ton"
					print "5.  Short Ton"
					print "6.  Ounces"
					print "7.  Stone"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Pounds : ")
							print "Tonnes:", n * 0.0004536
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Pounds : ")
							print "Kilograms:", n * 0.4536
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Pounds : ")
							print "Grams:", n * 453.59
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Pounds : ")
							print "Long Tons:", n * 0.0004464
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Pounds : ")
							print "Short Tons:", n * 0.0005
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Pounds : ")
							print "Pounds:", n * 16
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Pounds : ")
							print "Stones:", n * 0.071428
					else:
						c = c+1
			if n == 7:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Tonne"
					print "2.  Kilogram"
					print "3.  Gram"
					print "4.  Long Ton"
					print "5.  Short Ton"
					print "6.  Pound"
					print "7.  Stone"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Ounces : ")
							print "Tonnes:", n * 0.00002835
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Ounces : ")
							print "Kilograms:", n * 0.02835
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Ounces : ")
							print "Grams:", n * 28.35
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Ounces : ")
							print "Long Tons:", n * 0.0000279
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Ounces : ")
							print "Short Tons:", n * 0.00003125
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Ounces : ")
							print "Pounds:", n * 0.0625
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Ounces : ")
							print "Stones:", n * 0.004464
					else:
						c = c+1
			if n == 8:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Tonne"
					print "2.  Kilogram"
					print "3.  Gram"
					print "4.  Long Ton"
					print "5.  Short Ton"
					print "6.  Pound"
					print "7.  Ounce"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Stone : ")
							print "Tonnes:", n * 0.00635029
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Stone : ")
							print "Kilograms:", n * 6.35029
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Stone : ")
							print "Grams:", n * 6350.29
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Stone : ")
							print "Long Tons:", n * 0.00625
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Stone : ")
							print "Short Tons:", n * 0.01
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Stone : ")
							print "Pounds:", n * 14
					if n == 7:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Stone : ")
							print "Ounces:", n * 224
					else:
						c = c+1
	if n == 5:
		b = 1
		while b == 1:	
			print ""
			print ""
			print "What is the unit you wish to convert from?"
			print ""
			print "1.  Kilometres/hour"
			print "2.  Metres/second"
			print "3.  Miles/hour"
			print ""
			n = int(raw_input("Choose a unit : "))
			if n == 1:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Metres/second"
					print "2.  Miles/hour"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilometres/hour : ")
							print "Metres/second:", n * 0.2777777777778
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kilometres/hour : ")
							print "Miles/hour:", n * 0.62137
					else:
						c = c+1
			if n == 2:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Kilometres/hour"
					print "2.  Miles/hour"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Metres/second : ")
							print "Kilometres/hour:", n * 3.6
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Metres/second : ")
							print "Miles/hour:", n * 2.2369
					else:
						c = c+1
			if n == 3:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Kilometres/hour"
					print "2.  Metres/second"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Miles/hour : ")
							print "Kilometres/hour:", n * 1.609344
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Miles/hour : ")
							print "Metres/second:", n * 0.44704
					else:
						c = c+1
	if n == 6:
		b = 1
		while b == 1:	
			print ""
			print ""
			print "What is the unit you wish to convert from?"
			print ""
			print "1.  Celsius"
			print "2.  Fahrenheit"
			print "3.  Kelvin"
			print ""
			n = int(raw_input("Choose a unit : "))
			if n == 1:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Fahrenheit"
					print "2.  Kelvin"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Celsius : ")
							print "Fahrenheit:", (n * 1.8) + 32
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Celsius : ")
							print "Kelvins:", n + 273.15
					else:
						c = c+1
			if n == 2:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Celsius"
					print "2.  Kelvin"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Fahrenheit : ")
							print "Celsius:", (n - 32) / 1.8
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Fahrenheit : ")
							print "Kelvins:", (n + 459.7) / 1.8
					else:
						c = c+1
			if n == 3:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Celsius"
					print "2.  Fahrenheit "
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kelvins : ")
							print "Celsius:", n + 273.15
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Kelvins : ")
							print "Fahrenheit:", (n * 1.8) - 459.7
					else:
						c = c+1
	if n == 7:
		b = 1
		while b == 1:	
			print ""
			print ""
			print "What is the unit you wish to convert from?"
			print ""
			print "1.  Year"
			print "2.  Month"
			print "3.  Week"
			print "4.  Day"
			print "5.  Hour"
			print "6.  Minute"
			print "7.  Second"
			print ""
			n = int(raw_input("Choose a unit : "))
			if n == 1:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Month"
					print "2.  Week"
					print "3.  Day"
					print "4.  Hour"
					print "5.  Minute"
					print "6.  Second"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							nn = input("Years : ")
							print "Months:", n * 12
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							nn = input("Years : ")
							print "Weeks:", n * 52.1775
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							nn = input("Years : ")
							print "Days:", n * 365.2425
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							nn = input("Years : ")
							print "Hours:", n * 8765.82
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							nn = input("Years : ")
							print "Minutes:", n * 525949.2
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							nn = input("Years : ")
							print "Seconds:", n * 31556952
					else:
						c = c+1
			if n == 2:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Year"
					print "2.  Week"
					print "3.  Day"
					print "4.  Hour"
					print "5.  Minute"
					print "6.  Second"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Months : ")
							print "Years:", n * 0.08333333333333333333
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Months : ")
							print "Weeks:", n * 4.348125
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Months : ")
							print "Days:", n * 30.436875
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Months : ")
							print "Hours:", n * 730.485
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Months : ")
							print "Minutes:", n * 43829.1
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Months : ")
							print "Seconds:", n * 2629746
					else:
						c = c+1
			if n == 3:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Year"
					print "2.  Month"
					print "3.  Day"
					print "4.  Hour"
					print "5.  Minute"
					print "6.  Second"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Weeks : ")
							print "Years:", n * 0.0191165
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Weeks : ")
							print "Months:", n * 0.22998
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Weeks : ")
							print "Days:", n * 7
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Weeks : ")
							print "Hours:", n * 168
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Weeks : ")
							print "Minutes:", n * 10080
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Weeks : ")
							print "Seconds:", n * 604800
					else:
						c = c+1
			if n == 4:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Year"
					print "2.  Month"
					print "3.  Week"
					print "4.  Hour"
					print "5.  Minute"
					print "6.  Second"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Days : ")
							print "Years:", n * 0.0027379
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Days : ")
							print "Months:", n * 0.032855
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Days : ")
							print "Weeks:", n * 0.14286
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Days : ")
							print "Hours:", n * 24
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Days : ")
							print "Minutes:", n * 1440
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Days : ")
							print "Seconds:", n * 86400
					else:
						c = c+1
			if n == 5:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Year"
					print "2.  Month"
					print "3.  Week"
					print "4.  Day"
					print "5.  Minute"
					print "6.  Second"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Hours : ")
							print "Years:", n * 0.00011408
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Hours : ")
							print "Months:", n * 0.00136895
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Hours : ")
							print "Weeks:", n * 0.00595238
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Hours : ")
							print "Days:", n * 0.041666666666666667
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Hours : ")
							print "Minutes:", n * 60
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Hours : ")
							print "Seconds:", n * 3600
					else:
						c = c+1
			if n == 6:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Year"
					print "2.  Month"
					print "3.  Week"
					print "4.  Day"
					print "5.  Hour"
					print "6.  Second"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Minutes : ")
							print "Years:", n * 0.000001901324
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Minutes : ")
							print "Months:", n * 0.0000228159
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Minutes : ")
							print "Weeks:", n * 0.000099206
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Minutes : ")
							print "Days:", n * 0.00069444444444444
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Minutes : ")
							print "Hours:", n * 0.0166666666666666667
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Minutes : ")
							print "Seconds:", n * 60
					else:
						c = c+1
			if n == 7:
				c = 1
				while c == 1:
					print ""
					print ""
					print "What is the unit you wish to convert to?"
					print ""
					print "1.  Year"
					print "2.  Month"
					print "3.  Week"
					print "4.  Day"
					print "5.  Hour"
					print "6.  Minute"
					print ""
					n = int(raw_input("Choose a unit : "))
					if n == 1:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Seconds : ")
							print "Years:", n * 3.1689 * (10 ** -8)
					if n == 2:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Seconds : ")
							print "Months:", n * 0.000000380265
					if n == 3:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Seconds : ")
							print "Weeks:", n * 0.000001653439
					if n == 4:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Seconds : ")
							print "Days:", n * 0.00001157407
					if n == 5:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Seconds : ")
							print "Hours:", n * 0.00027777777778
					if n == 6:
						d = 1
						while d == 1:
							print ""
							print "Input Values:"
							n = input("Seconds : ")
							print "Minutes:", n * 0.0166666667
					else:
						c = c+1
    except ValueError:
	print ""	
	print "Returning to main menu..."
	print ""
	time.sleep(1)

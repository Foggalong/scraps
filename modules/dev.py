#!/usr/bin/python3

# Module Information
# ----------------------
# This module contains all the function which are used in
# the development process. These will only be used in the
# game until it's final beta then they will be removed ( 
# appart from the snapshot releases)


def error(code, message):
	"""The dev. error command"""
	print("ERROR %d: %s" % (code, message))
	print("Please report this problem")

def mes(message):
	"""The dev. message command"""
	print("DEV: %s" % message)
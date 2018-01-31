#!/usr/bin/python3

# Module Information
# ----------------------
# This module contains all the function which are used as
# standard throughout the game.

def usr_input():
	"""The standard user input command"""
	var = input("\n> ").lower().strip()
	return var

def pause():
	"""The standard pause command"""
	pause = input()

def mes(message):
	"""The standard messaging command"""

def mistake(command):
	"""User has inputed an incorrect command"""
	print("Sorry, \"%s\" is not a valid command" % command)
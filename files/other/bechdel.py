#!/usr/bin/python3

# License:  This  program  is  free  software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the  Free Software Foundation; either version 3 of the License, or (at your
# option)  any later version. This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.



"""
This is program which checks whether a given script passes
the Betchel test. The requirements to pass the test are:

    1. The cast must contain at least 2 females
    2. Two females must at some point have a conversation
    3. The conversation cannot be about a male

A derived test (Mako Mori) also has too additional conditions
which will serve here as bonus points:

    4. One female has their own narrative arc
    5. The arc is not about supporting a male’s story
    
For this program scripts which fufil 1, 2, and 3 will be
given as "Pass", those which then pass 4 will be given a
"Merit", and those which pass all 5 are marked "Distinction".
    
While these requirements are not by any means the definition
of a good script they are an interesting measure of how male
dominated a piece of media can be.

To use the program run it in the same directory as the
script with the command "./betchel.py script.txt". Please
not that to get accurate results from the script you may
have to modify some of the config variables below. 
"""



""" SCRIPT LOADING """

from sys import argv
if len(argv) != 2:
    print("Must be run with exactly one argument")
    exit(0)
elif argv[1].split(".")[len(argv[1].split("."))-1] != "txt":
    print("Script must be in .txt format")
    exit(0)
else:
    try:
        with open(argv[1], "r") as file:
            script = [line for line in file]
        print("Loaded", argv[1].replace(".txt.", ""))
    except:
        print("Error loading file")



""" CONFIG """

# Are speaker names in block capitals
speaker_caps = True

# Identifies when a line is a speaker name
speaker_tabs = "            "



""" VARIABLES """

# These identity strings assign a gender automatically
# if an obviousvword appears in the to-be cast name
male_ident = ["dad", "father", "brother", "son", "boyfriend", "boy", "man", "male"]
female_ident = ["mum", "mom", "mother", "sister", "daughter", "girlfriend", "girl", "woman", "female"]

if speaker_caps == True:
     male_ident = [item.upper() for item in male_ident]
     female_ident = [item.upper() for item in female_ident]


""" CAST LOADING """

# Creates cast list
cast, rejects = [], []
for line in script:
     if speaker_tabs in line:
         line = line.strip()
         if (line.isupper() and speaker_caps) == True:
             cast_names = [name[0] for name in cast] 
             if line not in cast_names + rejects:
                 line_parts = line.replace("'S", "").replace("'", "").split(" ")
                 # Gender identificattion
                 if any(part in male_ident for part in line_parts):
                     cast.append([line, "m"])
                 elif any(part in female_ident for part in line_parts):
                     cast.append([line, "f"])
                 else:
                     # Existing identifiction
                     if any(part in cast_names for part in line_parts):
                         rejects.append(line)
                     else:
                         gender = input("What gender is {0}? ".format(line))
                         if gender in ["m", "f", "o"]:
                             cast.append([line, gender])
                         else:
                             rejects.append(line)
             else:
                 pass
         else:
             pass
     else:
         pass

# Works out proportions
female = 0
for member in cast:
    if member[1] == "m":
        male += 1
    elif member[1] == "f":
        female += 1
    else:
        other += 1
total = male + female + other
if total == 0:
    total += 1
print("M:", male, (male/total)*100)
print("F:", female, (female/total)*100)
print("O:", other, (other/total)*100)
#!/usr/bin/python3

# Needed modules (all default)
import csv, codecs
from random import choice, randint
from os import chdir, system, rename

""" Other depends...
Programs: Python 3.x, Mozilla Thunderbird, git, unix system
Accounts: email, access to DP git repos
Data: voter_data.csv, results from the last survey
Directory structure;

Hub
|-- info
|	|
|   `-- [contents of info git repo]
| 
`-- vote-data
|	|
|   |-- Codes
|   |	|
|   |   |-- 1.txt
|   |	|-- 2.txt
|   |   `-- [previous session codes]
|   |
|   |-- Results
|   |   |
|   |   |-- 1.csv
|   |	|-- 2.csv
|   |   `-- [previous session results]
|   |
|   `-- register.csv
|
|-- codes.csv
|-- mail-bot.py
`-- voter_data.csv

PROBLEMS
+ random line at the bottom of voter-data.csv

"""


session = 3
print("Running script for session {0}...".format(session))


print("Pushing results to repo...")
chdir("vote-data/Results/")
system("git add {0}.csv".format(str(session-1)))
system("git commit -m \"Added session {0} results\"".format(str(session-1)))
system("git push origin master")
chdir("../../")


print("Check which codes were submitted...")
with open('vote-data/Results/{0}.csv'.format(str(session-1)), newline='') as csvfile:
	csv_list = csv.reader(csvfile, delimiter=',', quotechar='|')
	used_codes = []
	for line in csv_list:
		print(line)
		used_codes.append(line[1])


print("Preparing user data...")
with open('voter_data.csv', newline='', encoding="utf-16-le") as csvfile:
	csv_list = csv.reader(csvfile, delimiter=',', quotechar='|')
	name_list, email_list, old_code_list = [], [], []
	for line in csv_list:
		name_list.append(line[0])
		email_list.append(line[1])
		old_code_list.append(line[2])


print("Saving old codes to file...")
code_file, temp_codes = open("vote-data/Codes/{0}.txt".format(str(session-1)), "w"), old_code_list
while len(temp_codes) != 0:
	code = choice(temp_codes)
	if code == "Last ID":
		pass
	else:
		code_file.write(code+"\n")
	temp_codes.remove(code)
code_file.close()


print("Pushing old codes to repo...")
chdir("vote-data/Codes/")
system("git add {0}.txt".format(str(session-1)))
system("git commit -m \"Added session {0} codes\"".format(str(session-1)))
system("git push origin master")
chdir("../../")


print("Prepare data for writing to register...")
checklist = []
for code in old_code_list:
	if code in used_codes:
		checklist.append("✔")
	else:
		checklist.append("✘")


print("Updating register...")
register = open('vote-data/register.csv', 'r+')
register_lines = []
for line in register:
	register_lines.append(line.split(","))
for x in range(0, len(checklist)):
	register_lines[x].insert(1, checklist[x])
register.seek(0); register.truncate()
for line in register_lines:
	register.write(",".join(line))
register.close()


print("Pushing register to repo...")
chdir("vote-data/")
system("git add register.csv")
system("git commit -m \"Updated register\"")
system("git push origin master")
chdir("../")


print("Generating new codes...")
new_codes = []
for nul in range(0, len(name_list)): # while len(new_codes) != len(name_list)?
	code = ""
	while code == "":
		# List of 6 random hex digits
		chars,code=[chr(i) for i in range(65, 71)]+[chr(i) for i in range(48, 58)],[]
		for x in range(0, 6): code.append(chars[randint(0,len(chars)-1)])
		if "".join(code) in new_codes:
			pass
		else:
			code = "".join(code)
			new_codes.append(code)


print("Saving new codes to file...")
voter_file = open("voter_data.csv", "r+", encoding="utf-16-le")
voter_lines = []
for line in voter_file:
	voter_lines.append(line.split(","))
for x in range(0, len(voter_lines)):
	voter_lines.pop(len(voter_lines)-1)
	voter_lines.append(new_codes[x])
voter_file.seek(0); voter_file.truncate()
for line in voter_lines:
	voter_file.write(",".join(line))
voter_file.close()


print("Preparing email...")
for x in range(1, len(name_list)):
	body = """Hey {0},

Last session we had our first two passed votes! The
thunderbird icons are now set to branded by default
and "Country Grass" is now available from the wall-
paper collection.

New vote: http://democracy-project.github.io/vote.html
Voter ID: {1}

Thanks,
Josh""".format(name_list[x], new_codes[x])

	print("Sending email to {0}...".format(name_list[x]))
	system("thunderbird -compose \"to='{0}',subject='DP Session #{1}',body='{2}'\"".format(email_list[x], session, body))

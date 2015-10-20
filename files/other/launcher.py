#!/usr/bin/env python3

# This was created in response to this program by the ModuloProject which
# aims to make a command line app launcher. The method they were using to
# get data from launchers seemed sub-optimal so I reworked it to be a bit
# more efficient. Their original version is found at: http://git.io/vWJcm

from os import listdir, path
from subprocess import call


def clear():
    call(["clear"])

home = path.expanduser("~")
locations = [
    "/usr/share/applications/",
    "/usr/share/applications/kde4/",
    "/usr/local/share/applications/",
    "/usr/local/share/applications/kde4/",
    home + "/.local/share/applications/",
    home + "/.local/share/applications/kde4/",
]

name_list = []
exec_list = []
file_list = []

for location in locations:
    if path.isdir(location):
        for filename in listdir(location):
            if ".desktop" in filename:
                with open(location + filename, "r") as file:
                    namecheck, execcheck = False, False
                    for line in file:
                        if ("Name=" in line) and (not namecheck):
                            namecheck = True
                            name_list.append(line.split("=")[1].strip())
                        elif ("Exec=" in line) and (not execcheck):
                            execcheck = True
                            exec_list.append(line.split("=")[1].strip())
                        else:
                            # Not interested in other lines
                            pass
                    if namecheck and execcheck:
                        # Only use complete launchers
                        file_list.append(location + filename)
            else:
                # Not interested in non-launchers
                pass
    else:
        # Not all locations exist
        pass

# Makes mega-list and then sorts list alphabetically by app name
data = sorted(zip(name_list, exec_list, file_list), key=lambda x: x[0].lower())

clear()
for line in data:
    print("Name:", line[0])
    print("Exec:", line[1], "\n")
choice, i = input("What do you want to run? ").lower().strip(), 0
if choice not in [item.lower() for item in name_list]:
    # Case of zero options
    print("'" + choice + "' is not an option!")
    exit(0)

options, toprint = [], []
for line in data:
    if line[0].lower() == choice:
        toprint.append("Code: " + str(i))
        toprint.append("Name: " + line[0])
        toprint.append("Exec: " + line[1] + "\n")
        options.append(line[1])
        i += 1

if i != 1:
    # Case of multiple options
    clear()
    for line in toprint:
        print(line)
    toexec = input("Which code? ")

    try:
        # Makes sure chosen option exists
        if 0 <= int(toexec) <= len(options):
            cmd = options[int(toexec)].split(" ")
        else:
            raise ValueError
    except ValueError:
        print("'" + toexec + "' is not an option!")
        exit(0)
else:
    # Case of exactly one option
    cmd = options[0].split(" ")

clear()
try:
    call(cmd)
except FileNotFoundError:
    print("ERROR: command not found!")
    exit(1)

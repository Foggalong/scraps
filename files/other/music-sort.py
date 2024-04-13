#!/usr/bin/env python3

from os import listdir, mkdir, rename
from os.path import exists, isfile, join

path = "."
files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith(".mp3")]
print(files)


for f in listdir(path):
    # we only want to look at MP3 files
    if not f.endswith(".mp3"): pass

    # extract meta data from filename
    parts = f.split(" - ")
    artist, album = parts[0], False
    if len(parts) >= 4:
        album = parts[1]
        song = " - ".join(parts[2:])
    elif len(parts) == 3:
        album = parts[1]
        song = parts[2]
    elif len(parts) == 2:
        song = parts[1]
   
    # create a folder for the artist
    destination = artist
    if destination == '':
        print(f)
        continue
    elif not exists(destination):
        mkdir(destination)

    # if an album, create a subdir for that
    if album:
        destination += f"/{album}"
        if not exists(destination):
            mkdir(destination)

    # try:
        destination += f"/{song}"
    # except:
    #     print(f)
    #     continue

    try:
        rename(f, destination)
    except:
        print("NotADirectoryError\n", f, "\n", destination, "\n")

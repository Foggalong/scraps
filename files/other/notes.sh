#!/bin/bash

# Small script I use to sync my notes between my Copy account,
# todo.txt on my phone and my desktop which uses XFCE4-notes.

# Locations
copy_dir="/home/josh/Copy/Notes/Desktop"
note_dir="/home/josh/.local/share/notes/Notes/*"

# Between desktop and Copy
for file in $note_dir
do
	echo "${copy_dir}/${filename}.txt"
	echo -e "$file\n"
	filename=$(basename "${file}")
	echo "Processing ${file} notes..."
	if [ -f "${copy_dir}/${filename}.txt" ]
	then
		note_time=$(stat -c %Y "${file}")
		copy_time=$(stat -c %Y "${file}.txt")
		if [ ${copy_time} -lt ${note_time} ]
		then
			echo -e "Updated local version\n"
		elif [ ${note_time} -lt ${copy_time} ]
		then
			cp "${file}" "${file}.txt"
			echo -e "Updated Copy version\n"
		else
			echo -e "Already up to date\n"
			cp "${file}.txt" "${file}"
		fi
	else
		cp "${file}" "/home/josh/.local/share/notes/Notes/*"
		echo -e "Adding to Copy\n"
	fi
done
echo "All done!"
#!/bin/bash

# This script converts formats to sync
# between ownCloud and XFCE4 notes

# Default ownCloud notes location
server="/home/${SUDO_USER:-$USER}/ownCloud/Notes/*"
server_clean="${server//\//\\/}"

# Default XFCE4 notes location
desktop="/home/${SUDO_USER:-$USER}/.local/share/notes/Notes/*"
desktop_clean="${desktop//\//\\/}"

# Syncs desktop to server
for file in "${desktop}*"
do
	file_name=$(echo $file | sed -e "s/${desktop_clean}//g")
	echo $file_name
	if [ -f "${server}${file_name}.txt" ]
	then
		: # pass
	else
		mv $file "${server}${file_name}.txt"
	fi
done

# Syncs server to desktop
for file in $server
do
	file_name=$(echo $file | sed -e "s/${server_clean}//g")
	file_name=$(echo $file_name | sed -e "s/.txt//g")
	echo $file_name
	if [ -f "${desktop}${file_name}" ]
	then
		: # pass
	else
		ln -s ${file} "${desktop}${file_name}"
	fi
done

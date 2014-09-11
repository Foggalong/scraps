#!/bin/bash

# Orphaned code from the bash version of Wren
# I may one day get around to sorting it out.



echo -e "$error_msg"	# GitHub git type
	elif [ "$type" == "ghgit" ]
	then
		while true; do
			read -p "What is your GitHub username? " answer
			if [ -z "$answer"]
			then
				echo -e "Please enter your GitHub username."
			else
				no_ghpage_err="Please enter a valid GitHub username with\na GitHub pages repo (username.github.io)."
				git clone https://github.com/$answer/$answer.github.io.git || echo -e "$no_ghpage_err"
			fi
		done
			rootdir="$inputline"
		done
		if [ -d "$inputline/.git" ] && [[ "$inputline" == *.github.io* ]]
		then
			: # pass
		else
			echo -e "Please enter the location of a cloned GitHub Pages"
			echo -e "directory with a '.git' subdirectory and a name of"
			echo -e "the form $USERNAME.github.io to proceed.\n"
			sleep 3
			exit 1
		fi


						# GitHub Username
				ghuser="$answer"
				ghpage="$ghuser.github.io"

				# Cloning repo
				git clone "https://github.com/$ghuser/$ghpage.git" || error="True"
				if [ "$error" == True ]; then
					echo -e "An error has occured, which could be because"
					echo -e "of one of two reasons:"
					echo -e "  1. The given GitHub account"
				if wget "" >/dev/null 2>&1 ; then


					
		if [ -d "$inputline/.git" ] && [[ "$inputline" == *.github.io* ]]; then
			: # pass
		else
			echo -e "Please enter the location of a cloned GitHub Pages"
			echo -e "directory with a '.git' subdirectory and a name of"
			echo -e "the form $USERNAME.github.io to proceed.\n"
			sleep 3
			exit 1
		fi

#!/bin/bash

# This script manages the installing, upgrading and removal of Wren
# installations. Before running this script please consult the
# GitHub documentation repo (https://github.com/wren-blog/install)
# for more information on the options presented in this script.

# Copyright (C) 2014
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3+) as
# published by the Free Software Foundation. You should have received
# a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

version="0.1-alpha"  # version number
mode="install"       # default mode

# Deals with the flags
if [ -z $1 ]
then
	: # pass
else
	case $1 in
		-i|--install)
			mode="install"; break;;
		-u|--upgrade)
			mode="upgrade"; break;;
		-r|--remove)
			echo "This will completely remove a Wren installation."
			while true; do
				read -p "Are you sure you want to continue? " answer
				case $answer in
					[Yy]* ) mode="remove"; break;;
					[Nn]* ) exit;;
					* ) echo "Please answer [Y/y]es or [N/n]o.";;
				esac
			done;;
		-h|--help)
			echo -e "Usage: ./$(basename -- $0) [OPTION]"
			echo -e "A lightweight blogging platform."
			echo -e ""
			echo -e "Currently supported options:"
			echo -e "  -i, --install \t Install Wren (default)"
			echo -e "  -u, --upgrade \t Upgrade a Wren installation"
			echo -e "  -r, --remove \t Remove a Wren installation"
			echo -e "  -h, --help \t\t Displays this help menu"
			echo -e "  -v, --version \t Displays program version"
			exit 0 ;;
		-v|--version)
			echo "$(basename -- $0) $version\n"
			exit 0 ;;
		*)
			echo -e "$(basename -- $0): invalid option -- '$1'"
			echo -e "Try '$(basename -- $0) --help' for more information."
			exit 0 ;;
	esac
fi

# Deals with unsupported modes
if [ "$mode" == "upgrade" ]
then
	echo -e "Upgrading will not be available until late beta."
	echo -e "This is because the changes from version to version"
	echo -e "are to great to ensure that the process will work."
elif [ "$mode" == "remove" ]
then
	echo -e "Removing will not be available until late alpha."
	echo -e "This is because the installation mode is still"
	echo -e "under heavey development and is constantly changing."
fi

# Installation method
echo -e "The following installation methods are available.\n"
echo -e "    1.  As a stand-alone website"
echo -e "    2.  Alongside an existing website"
echo -e "    3.  Using GitHub pages and git"
echo -e "    4.  Using GitHub pages (web-only)"

while true; do
	read -p "\nWhich installation method do you want to use? " answer
	case $answer in
		[1]* ) type="alone"; break;;
		[2]* ) type="along"; break;;
		[3]* ) type="ghgit"; break;;
		[4]* ) type="ghweb"; break;;
		* ) echo "Please choose an option from above (1-4)";;
	esac
done;;

# Checks dependencies installed
if [ "$type" == "ghgit" ]
then
	# Verifies if 'git' is installed
	if type "git" >> "/dev/null 2>&1"
	then
		: # pass
	else
		echo -e "This method requires 'git' to be installed. If"
		echo -e	"you wish to use GitHub pages without using git"
		echo -e	"please use the web-only option. Otherwise, please"
		echo -e	"install it and rerun this install script."
		sleep 3
		exit 1
	fi
elif [ "$type" == "alone" ] || [ "$type" == "along" ] || [ "$type" == "ghgit" ]
then
	# Verifies if 'wget' is installed
	if type "wget" >> "/dev/null 2>&1"
	then
		: # pass
	else
		echo -e "This method requires 'wget' to be installed. This"
		echo -e	"is so that the installer can fetch the source for"
		echo -e	"Wren from GitHub."
		sleep 3
		exit 1
	fi
	# Verifies if 'tar' is installed
	if type "tar" >> "/dev/null 2>&1"
	then
		: # pass
	else
		echo -e "This method requires 'tar' to be installed. This"
		echo -e	"is so that the installer can unzip the source it"
		echo -e	"downloads from GitHub. Please install it and rerun."
		sleep 3
		exit 1
	fi
fi

# GitHub web type
if [ "$type" == "ghweb" ]
then
	echo -e "This method is designed for web use only and so"
	echo -e "doesn't require any installation. Go to the wiki"
	echo -e "for more information on this method.\n"
	sleep 3 # Enables error timeout when launched via 'Run in Terminal' command.
	exit 1
# GitHub git type
elif [ "$type" == "ghgit" ]
then
	echo -e "Enter the location of your cloned GitHub Pages" 
	echo -e "directory (can either be absolute or relative)"
	while read inputline
	do
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
# Website type
elif [ "$type" == "alone" ] || [ "$type" == "along" ]
then
	echo -e "Please enter the root location for your website" 
	echo -e "directory (can either be absolute or relative)."
	echo -e "The path default is taken as '/var/www/html/'."
	while read inputline
	do
		rootdir="$inputline"
		if [ -z "${what}" ]
		then
			if [ -d "/var/www/html" ]
			then
				echo -e "Default accepted."
			else
				echo -e "ERROR: default location doesn't exist"
				echo -e "Please file this issue on the GitHub."
				sleep 3
				exit 1
			fi
		else
			if [ -d "$rootdir" ]
			then
				echo -e "Using $rootdir"
			else
				echo -e "The directory you entered doesn't seem to exist" 
				echo -e "Please enter a different directory upon rerun."
				sleep 3
				exit 1
			fi
		fi
	done
fi

# Checks write permissions
if [ -w "$rootdir" ]
then 
	: # pass
else
	echo -e "You do not have write permissions for the"
	echo -e "directory you entered. This could be because"
	echo -e "it requires root permissions so try running"
	echo -e "this script as root when trying again."
	sleep 3
	exit 1
fi

# Moved to rootdir
cd "$rootdir"

# Downloads latest Wren release
wget "https://github.com/wren-blog/wren/archive/v$version.tar.gz"
tar xf "v$version.tar.gz"
rm "v$version.tar.gz"

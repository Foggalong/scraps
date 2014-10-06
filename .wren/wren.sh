#!/bin/bash

# This is Wren. A super simple, open source blogging platform, written
# in bash and all contained in this one script. From it's various flags
# it manages the installation, upgrading, removing, and blog creation.

# Copyright (C) 2014
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3+) as
# published by the Free Software Foundation. You should have received
# a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

version="0.1-alpha"



# Deals with the flags
# ====================

# If no flag given
if [ -z "$1" ]; then
    if [ -d ".wren" ]; then
        mode="blog"
    else
        mode="install"
    fi
# If flag given
else
    case $1 in
        -b|--blog)
            if [ -d ".wren" ]; then
                mode="blog"; break
            else
                echo -e "To write a blog you must first install Wren."
                echo -e "Run ./wren.sh -i and follow the instructions"
                exit 1
            fi;;
        -i|--install)
            if [ -d ".wren" ]; then
                echo -e "The current directory already contains a Wren"
                echo -e "instance. Check it out and then try again."
                exit 1
            else
                mode="install"; break
            fi;;
        -u|--upgrade)
            if [ -d ".wren" ]; then
                echo -e "Upgrading will not be supported until late beta"
                echo -e "for stability reasons. Please try again later."
                exit 0
                mode="install"; break
            else
                echo -e "The current directory doesn't contain a Wren"
                echo -e "instance. Check it out and then try again."
                exit 0
            fi;;
        -r|--remove)
            echo "This will completely remove a Wren instance."
            while true; do
                read -p "Are you sure you want to continue? " answer
                case $answer in
                    [Yy]* )
                        echo -e "Removing will not be supported until late alpha"
                        echo -e "for stability reasons. Please try again later."
                        exit 0
                        mode="remove"; break;;
                    [Nn]* ) exit;;
                    * ) echo "Please answer [Y/y]es or [N/n]o.";;
                esac
            done;;
        -h|--help)
            echo -e "Usage: ./$(basename -- $0) [OPTION]"
            echo -e "A lightweight blogging platform."
            echo -e ""
            echo -e "Currently supported options:"
            echo -e "  -b, --blog \t Write a blog (default)"
            echo -e "  -i, --install \t Install Wren"
            echo -e "  -u, --upgrade \t Upgrade a Wren instance"
            echo -e "  -r, --remove \t Remove a Wren instance"
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



# Checks Dependencies
# ===================

# List of dependencies
depends=(wget tar date wc)

# Verifies if each is installed
for package in "${depends[@]}"; do
    if type "$package" >> "/dev/null 2>&1"; then
        : # pass
    else
        echo -e "Using wren requires '$package' to be installed. Please"
        echo -e    "install it and then run this script again."
        sleep 3
        exit 1
    fi
done

# If needed, verifies if 'git' is installed
if [ "$type" == "ghgit" ]; then
    if type "git" >> "/dev/null 2>&1"
    then
        : # pass
    else
        echo -e "This method requires 'git' to be installed. If"
        echo -e    "you wish to use GitHub pages without git please"
        echo -e "use the web-only option. Otherwise, install it"
        echo -e "and rerun this script."
        sleep 3 # Enables error timeout when launched via 'Run in Terminal' command.
        exit 1
    fi
fi



# Blog Creator
# ============

if [ "$mode" == "blog" ]; then
    # Creating New Blog
    # -----------------

    # Writer
    echo -e "Please write your blog below, using HTML for"
    echo -e "formatting and adding 'EOF' as the last line.\n"
    while [ "$line" != "EOF" ]; do
        read -p "> " line
        if [ "$line" == "EOF" ]; then
            break
        else
            blog_body+="$line\n"
        fi
    done

    # Reading length - using 250 WPM
    blog_length=$(($(echo "$blog_body" | wc -w) / 250))

    # Meta Data
    echo -e "\nWe will now ask for the blogs meta data."
    echo -e "Enter each piece of information as prompted."

    # Blog title
    while true; do
        read -p "\nGive a post title:\n" answer
        if [ "$answer" == "" ]; then
            echo -e "Please enter a title"
        else
            blog_title="$answer"
            break
        fi
    done

    # Blog date
    blog_date=$(date +%F)      # 2014-06-17
    blog_date_long=$(date +%c) # Tue, 17 Jun 2014 13:20:00
    # Notes, RSS asks for 'Tue, ...' but %c gives no ','

    # Blog catagories
    echo -e "\nList the catagories this post falls into,"
    echo -e "seperating each by using a space."
    read -p "" answer
    blog_catagories=($answer)

    # Blog summary
    while true; do
        read -p "\nGive a brief summary of the post:\n" answer
        if [ "$answer" == "" ]; then
            echo -e "Please enter a summary"
        else
            blog_summary="$answer"
            break
        fi
    done

    # Correct information checker
    echo -e "\nGIVEN INFORMATION"
    echo -e "Title: $blog_title"
    echo -e "Date: $blog_date"
    echo -e "Catagories:"
    for catagory in "${blog_catagories[@]}"; do
        echo -e "    * $catagory"
    done
    echo -e "Summary: $blog_summary\n"
    while true; do
        read -p "Are you happy with the above? " answer
        case $answer in
            [Yy]* ) echo -e "Blog data rejected"; break;;
            [Nn]* ) echo -e "Blog data accepted"; exit;;
            * ) echo "Please answer [Y/y]es or [N/n]o.";;
        esac
    done


    # Writing blog to file
    # --------------------

    # Creating tmp file
    cp "blog_template.html" "blog.tmp"

    # Adds meta 
    sed -i "s/BLOG_TITLE_GOES_HERE/$blog_title/g" blog.tmp
    sed -i "s/BLOG_DATE_GOES_HERE/$blog_date/g" blog.tmp
    sed -i "s/BLOG_BODY_GOES_HERE/$blog_body/g" blog.tmp

    # Checks reading time
    if [ "$blog_length" -lt 4 ]; then
        sed -i "/READING_TIME_GOES_HERE/d" blog.tmp
    else
        sed -i "s/READING_TIME_GOES_HERE/~$blog_length minutes/g" blog.tmp
    fi

    # Moving into position
    blog_location="$(date +%Y)/$(date +%m)/$(date +%d)/$(echo $blog_title | sed "s/[^a-zA-Z0-9]//g")"
    mv "blog.tmp" "../blogs/$blog_location"


    # Managing Catagories
    # -------------------
    
    for catagory in "${blog_catagories[@]}"; do
        # Adding to cloud
        echo $catagory >> cloud.txt

        # Existence Dependent Additions
        if [ -f "../blogs/Catagories/$catagory" ]; then
            # Catagory found
            identifier="\t\t\t<!-- List Begins Here -->\n"
            sed -i "s/$identifier/$identifier\t\t\t<li><a href=\"..\/$blog_location\">$blog_date - $blog_title<\/a><\/li>\/g" "../blogs/Catagories/$catagory"
            # sed -i "THING WITH RSSS"            
        else
            # Catagory Not Found 
            cp "blog_template.html" "catagory.tmp"
            sed -i "s/CATAGORY_NAME_GOES_HERE/$catagory/g" catagory.tmp
            sed -i "s/BLOG_TITLE_GOES_HERE/$blog_title/g" catagory.tmp
            sed -i "s/BLOG_DATE_GOES_HERE/$blog_date/g" catagory.tmp
            # Handling feeds
            cp "rss_template.xml" "catagory.xml"
            sed -i "s/CATAGORY_NAME_GOES_HERE/$catagory/g" catagory.tmp
            sed -i "s/BLOG_TITLE_GOES_HERE/$blog_title/g" blog.tmp
            sed -i "s/FULL_BLOG_DATE_GOES_HERE/$blog_date_long/g" catagory.tmp
            sed -i "s/BLOG_LOCATION_GOES_HERE/$blog_location/g" catagory.tmp
            sed -i "s/BLOG_SUMMARY_GOES_HERE/$blog_summary/g" catagory.tmp
        fi
    done

    # Adding to general catagory files
    # add to catagory_all and rss_all files
fi



# Installer
# =========

if [ "$mode" == "install" ]; then
    # Installation method
    echo -e "The following installation methods are available.\n"
    echo -e "  1.  As a stand-alone website"
    echo -e "  2.  Alongside an existing website"
    echo -e "  3.  Using GitHub pages and git"
    echo -e "  4.  Using GitHub pages (web-only)"

    while true; do
        read -p "\nWhich installation method do you want to use? " answer
        case $answer in
            [1]* ) type="alone"; break;;
            [2]* ) type="along"; break;;
            [3]* ) type="ghgit"; break;;
            [4]* ) type="ghweb"; break;;
            * ) echo "Please choose an option from above (1-4)";;
        esac
    done


    # GitHub Web Type
    # ---------------

    if [ "$type" == "ghweb" ]; then
        echo -e "This method is designed for web use only and so"
        echo -e "doesn't require any instance. Go to the wiki"
        echo -e "for more information on this method.\n"
        sleep 3
        exit 1
    fi


    # GitHub Git Type
    # ---------------

    if [ "$type" == "ghgit" ]; then
        while true; do
            # Asks for username
            read -p "What is your GitHub username? " answer
            if [ -z "$answer"] || wget "https://github.com/$answer" >/dev/null 2>&1 
            then
                echo -e "GitHub user does not exist!"
            else
                break
            fi
        done

        # GitHub Username
        ghuser="$answer"
        ghpage="$ghuser.github.io"

        # Cloning repo
        git clone "https://github.com/$ghuser/$ghpage.git" || error="True"
        if [ "$error" == True ]; then
            echo -e "An error occured! Check the above git output"
            echo -e "for more information as to what went wrong."
            sleep 3
            exit 1
        else
            cd "$ghpage"
        fi

        # Checking repo
        if [ -d ".wren" ]; then
            : #pass
        else
            cd ../ && rm -r "$ghpage"
            echo -e "The repo does not appear to be a fork of the"
            echo -e "Wren repo. Please verify it is and then rerun"
            sleep 3
            exit 1
        fi
    fi


    # Website type
    # ------------

    # Gets web root
    if [ "$type" == "alone" ] || [ "$type" == "along" ]; then
        echo -e "Please enter the root location for your website" 
        echo -e "directory (can either be absolute or relative)."
        echo -e "The path default is taken as '/var/www/html/'."
        while read inputline; do
            rootdir="$inputline"
            if [ -z "${what}" ]; then
                if [ -d "/var/www/html" ]; then
                    echo -e "Default accepted."
                else
                    echo -e "ERROR: default location doesn't exist"
                    echo -e "Please file this issue on the GitHub."
                    sleep 3
                    exit 1
                fi
            else
                if [ -d "$rootdir" ]; then
                    echo -e "Using $rootdir"
                else
                    echo -e "The directory you entered doesn't seem to exist" 
                    echo -e "Please enter a different directory upon rerun."
                    sleep 3
                    exit 1
                fi
            fi
        done

        # Checks write permissions
        if [ -w "$rootdir" ]; then 
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

        # Moves files into root
        mv "wren-$version/*" .
        rm -r "wren-$version"

        # DOOES REST OF STUFF
    fi
fi
#!/bin/bash

# This script used ot be part of Wren, which had installing, upgrading
# and removal built into it. This has been dropped now in favour of
# packaging being done externally.

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

# Functions
# =========

function gerror() {
    echo -e "$1"
    sleep 3
    exit 1
}


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
                gerror "To write a blog you must first install Wren"
            fi;;
        -i|--install)
            if [ -d ".wren" ]; then
                gerror "The current directory already contains a Wren instance"
            else
                mode="install"; break
            fi;;
        -u|--upgrade)
            if [ -d ".wren" ]; then
                gerror "Upgrading will not be supported until late beta"
                mode="upgrade"; break
            else
                gerror "The current directory doesn't contain a Wren instance"
            fi;;
        -r|--remove)
            echo "This will completely remove a Wren instance."
            while true; do
                read -p "Are you sure you want to continue? " answer
                case $answer in
                    [Yy]* )
                        gerror "Removing will not be supported until late alpha"
                        mode="remove"; break;;
                    [Nn]* ) exit;;
                    * ) echo "Please answer [Y/y]es or [N/n]o.";;
                esac
            done;;
        -h|--help)
            echo -e \
                "Usage: ./$(basename -- $0) [OPTION]\n" \
                "\rA lightweight blogging platform.\n\n" \
                "\rCurrently supported options\n:" \
                "\r  -b, --blog \t Write a blog (default)\n" \
                "\r  -i, --install \t Install Wren\n" \
                "\r  -u, --upgrade \t Upgrade a Wren instance\n" \
                "\r  -r, --remove \t Remove a Wren instance\n"
                "\r  -h, --help \t\t Displays this help menu\n"
                "\r  -v, --version \t Displays program version\n"
            exit 0 ;;
        -v|--version)
            echo "$(basename -- $0) $version\n"
            exit 0 ;;
        *)
            echo -e "$(basename -- $0): invalid option -- '$1'"
            gerror "Try '$(basename -- $0) --help' for more information." ;;
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
        gerror "Using wren requires '$package' to be installed"
    fi
done

# If needed, verifies if 'git' is installed
if [ "$type" == "ghgit" ]; then
    if type "git" >> "/dev/null 2>&1"
    then
        : # pass
    else
        echo -e \
            "This method requires 'git' to be installed. If\n"
            "\ryou wish to use GitHub pages without git please\n"
            "\ruse the web-only option. Otherwise, install it\n"
            "\rand rerun this script."
        gerror
    fi
fi



# Blog Creator
# ============

if [ "$mode" == "blog" ]; then
    # Creating New Blog
    # -----------------

    # Writer
    echo -e \
        "Please write your blog below, using HTML for\n"
        "\rformatting and adding 'EOF' as the last line.\n"
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
    echo -e \
        "\nWe will now ask for the blogs meta data.\n"
        "\rEnter each piece of information as prompted."

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
    echo -e \
        "\nList the catagories this post falls into,\n"
        "\rseperating each by using a space."
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
    echo -e \
        "\nGIVEN INFORMATION\n"
        "\rTitle: $blog_title\n"
        "\rDate: $blog_date\n"
        "\rCatagories:"
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
        echo "$catagory" >> cloud.txt

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
    echo -e \
        "The following installation methods are available.\n"
        "\r  1.  As a stand-alone website\n"
        "\r  2.  Alongside an existing website\n"
        "\r  3.  Using GitHub pages and git\n"
        "\r  4.  Using GitHub pages (web-only)"

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
        echo -e \
            "This method is designed for web use only and so\n"
            "\rdoesn't require any instance. Go to the wiki\n"
            "\rfor more information on this method.\n"
        gerror
    fi


    # GitHub Git Type
    # ---------------

    if [ "$type" == "ghgit" ]; then
        while true; do
            # Asks for username
            read -p "What is your GitHub username? " answer
            if [ -z "$answer"] || wget "https://github.com/$answer" >/dev/null 2>&1 
            then
                echo "GitHub user does not exist!"
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
            gerror "An error occured! Check above for more info"
        else
            cd "$ghpage"
        fi

        # Checking repo
        if [ -d ".wren" ]; then
            : #pass
        else
            cd ../ && rm -r "$ghpage"
            gerror "The repo does not appear to be a fork of the Wren repo"
        fi
    fi


    # Website type
    # ------------

    # Gets web root
    if [ "$type" == "alone" ] || [ "$type" == "along" ]; then
        echo -e \
            "Please enter the root location for your website\n" 
            "\rdirectory (can either be absolute or relative).\n"
            "\rThe path default is taken as '/var/www/html/'."
        while read inputline; do
            rootdir="$inputline"
            if [ -z "${what}" ]; then
                if [ -d "/var/www/html" ]; then
                    echo "Default accepted."
                else
                    mkdir /var/www/html/
                    echo "Created default directory"
                fi
            else
                if [ -d "$rootdir" ]; then
                    echo -e "Using $rootdir"
                else
                    gerror "The directory you entered doesn't seem to exist" 
                fi
            fi
        done

        # Checks write permissions
        if [ -w "$rootdir" ]; then 
            : # pass
        else
            echo -e \
                "You do not have write permissions for the\n"
                "\rdirectory you entered. This could be because\n"
                "\rit requires root permissions so try running\n"
                "\rthis script as root when trying again."
            gerror
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

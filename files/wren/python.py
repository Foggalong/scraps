#!/usr/bin/python3

# THis is the old version of wren

print("Wren Blog Updater")

# Importing Modules
from os import chdir, getcwd, listdir
from datetime import datetime

# Standardised error
def error(message):
	print("ERROR: %s" % message)
	exit()

# Changing working directory
chdir("../")



""" BLOG WRITER """
# Currently only supports plain text

blog_body = ""
usr_input = ""

while usr_input != "EOF":
	blog_body += usr_input + "\n"
	usr_input = input("> ")

print(blog_body)
exit()

""" METADATA """

# Blog title
blog_title = input("\nPlease give a post title:\n")

# Blog date
blog_date = datetime.now().date()

# Blog catagories
blog_catagories = input("\nPlease list the catagories this post falls into, seperating by space:\n").split(" ")
for item in blog_catagories: item = item.strip()

# Blog summary
blog_summary = input("\nPlease give a summary of the post:\n")

# Correct information checker
print("\nGIVEN INFORMATION")
print("Title:",blog_title)
print("Date:",blog_date)
print("Catagories:",blog_catagories)
print("Summary:",blog_summary,"\n")
trying = True
while trying:
	ans = input("Are you happy with the above? (y/n) ").lower()
	if ans == "y":
		trying = False
		pass
	elif ans == "n":
		error("blog data rejected")
	else:
		pass
print("Blog data accepted")



""" MANAGING NEW CATAGORIES """

for entry in new_catagories:
	# Creating New Lists
	entry_list = open(getcwd()+"/blogs/Catagories/"+entry, 'w')
	entry_list.write(open("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/template").read())
	entry_list.close()
	with open("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/"+entry, 'r+') as file:
		new_list = [line for line in file]
	for line in new_list:
		if "[template]" in line:
			old_line, n = line, new_list.index(line)
			new_list.pop(n)
			new_list.insert(n, old_line.replace("[template]", entry))
	entry_list = open("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/"+entry, 'w')
	entry_list.truncate()
	for line in new_list:
		entry_list.write(line)
	entry_list.close()
	print("Created %s catagory" % entry)

# Adding to word cloud - untested
for entry in blog_catagories:
    with open("//home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/cloud.txt", 'r') as file:
        cat_list = [line for line in file]
    cat_list.append(entry+"\n")
    cloud_file = open("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/cloud.txt", 'w')
    for line in cat_list:
        cloud_file.write(line)
    cloud_file.close()
    print("Added %s catagory to word cloud file" % entry)


# Adding Blog to Catagory Lists
for entry in (blog_catagories+["all"]):
	with open("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/"+entry, 'r+') as file:
		file_list = [line for line in file]
	for line in file_list:
		if "<!-- List Begins Here -->" in line:
			n = file_list.index(line)
			file_list.insert(n+1, '			<li><a href="../'+blog_date+'_'+blog_title.replace(' ','')+'">'+blog_date+'     '+blog_title+'</a></li>\n')
	entry_list = open("/home/josh/Programs/Web/HTML/fogg.me.uk/blogs/Catagories/"+entry, 'w')
	entry_list.truncate()
	for line in file_list:
		entry_list.write(line)
	entry_list.close()
	print("Added blog to %s catagory list" % entry)


# Adding blog to Recent Blogs page
with open("/home/josh/Programs/Web/HTML/fogg.me.uk/blog", 'r+') as file:
	file_list = [line for line in file]
for line in file_list:
	if "<!-- Recent Blogs Begin Here -->" in line:
		n = file_list.index(line)
		file_list.insert(n+1, '		<article>\n')
		file_list.insert(n+2, '			<h3> <a href="blogs/'+blog_date+'_'+blog_title.replace(' ','')+'">'+blog_title+'</a> - '+blog_date+'</h3>\n')
		file_list.insert(n+3, '			<p>'+blog_summary+'</p>\n')
		file_list.insert(n+4, '		</article>\n')
		file_list.insert(n+5, '\n')
		file_list.insert(n+6, '		<br class="small">\n')
		file_list.insert(n+7, '\n')
entry_list = open("/home/josh/Programs/Web/HTML/fogg.me.uk/blog", 'w')
entry_list.truncate()
for line in file_list:
	entry_list.write(line)
entry_list.close()
print("Added blog to recent blogs page")


# Removing the least recent blog from Recent Blogs page
with open("/home/josh/Programs/Web/HTML/fogg.me.uk/blog", 'r+') as file:
	file_list = [line for line in file]
for line in file_list:
	if "<!-- Recent Blogs End Here -->" in line:
		n = file_list.index(line)
		for x in range(1, 8):
			file_list.pop(n-x)
entry_list = open("/home/josh/Programs/Web/HTML/fogg.me.uk/blog", 'w')
entry_list.truncate()
for line in file_list:
	entry_list.write(line)
entry_list.close()
print("Removed least recent blog from recent blogs page")


# Program is finished!
print("Done!\n")


# #!/usr/bin/python3

# from math import floor

# text = input("Paste text...\n").strip().split(" ")
# if len(text)/200 < 1:
#     print("~%d seconds reading" % (float(len(text))*0.3))
# else:
#     print("~%d minutes %d seconds reading" % (floor(len(text)/float(200)), ((len(text)/float(200))-floor(len(text)/float(200)))*60))

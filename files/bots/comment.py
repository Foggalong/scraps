#!/usr/bin/python3

# This code was from the reddit bot /u/upmo I wrote for /r/unixporn.
# It checked for comments that were just a single '.' and removed
# them. I've since removed this from the main bot repo as I thought
# it was a bit excessive for such a rare event. Function was invoked
# with 'comments_check(post)' between 'for post in posts' and 'if 
# post.id in oldposts:' in the main bot function.

def comments_check(post):
	print("Checking comments...")
	comments = helpers.flatten_tree(post.comments)
	with open("oldposts", "r") as file:
		oldposts = [line.strip() for line in file]
	for comment in comments:
		# Comment Properties
		cid = "t3_" + comment.id
		if cid in oldposts:
			pass
		else:
			cbody = comment.body
			try:
				cauthor = comment.author.name
			except AttributeError:
				cauthor = "[deleted]"
			# Checking Comment
			if cbody == ".":
				print("\tFound dot comment")
				r.send_message(cauthor, "Comment in /r/" + SUBREDDIT, USESAVEPM, captcha=None)
				if TRUSTME == False: comment.report()
				comment.remove(spam=False)
				with open("oldposts","a+") as file:
					file.write(cid + "\n")
				print("\tComment removed")
			else:
				pass

# This is a simple program which creates a dialogue box with one button. Pressing the button will send the text in the textbox
# as a tweet to the @Foggalong twitter user, provided it is between 1 and 140 characters in length. At the minute the GUI code
# is largely copypasta but as I hope this quickly changes as I become more familiar with combining python code with a GUI. For
# the next few updates I intend to make some major updates such as diaglgue boxes for invalid tweet warnings, automatic use of
# the dft.ba link shortner (or possibly the native twitter link shortner if possible) for entered URLs and finall in a one big
# update movment of the entire GUI over to Glade.

from Tkinter import *
import twitter
api = twitter.Api(consumer_key = 'CONSUMER_KEY', consumer_secret = 'CONSUMER_SECRET', access_token_key = 'ACCESS_KEY', access_token_secret = 'ACCESS_SECRET')

class mywidgets:
	def __init__(self,root):
		frame = Frame(root)
		frame.pack()
		self.txtfr(frame)
		return

	def txtfr(self,frame):

		#define a new frame and put a text area in it
		textfr = Frame(frame)
		self.text = Text(textfr, height = 4, width = 35, background = 'white')
		self.text.pack(side = TOP, padx = 10, pady = 12)

		#puts the tweet button in place
		def test():
			print "test"

		def click(key):
			if key == 'Tweet':
				update = self.text.get(1.0, END)
				if len(update) == 0:
					print "You can't send an empty tweet!"
				elif len(update) > 140:
					print "Exceeded 140 characters."
				elif 0 < len(update) < 140:
					status = api.PostUpdate(update)
					print "Tweeting:", update
					self.text.delete(1.0, END)
		cmd = lambda x='Tweet': click(x)
		self.button = Button(textfr, text = "Tweet", command = cmd)
		self.button.pack(side = BOTTOM, padx = 10, pady = 10)
		
		#pack everything
		self.text.pack(side = LEFT)
		self.button.pack(side = LEFT)
		textfr.pack(side = TOP)
		return

def main():
	root = Tk()
	root.title("PyTweet")
	s = mywidgets(root)
	root.mainloop()

main()

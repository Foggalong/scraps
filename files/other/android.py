#importing modules
import time
import android

"""
There used to be an old Android package which allowed for the running of bare-
Python scripts, interacting with some of the OS' basic features (e.g. toasts)
using a minimal API. This is me playing around with that.
"""


#simplifying commands
droid = android.Android()
response = droid.dialogGetResponse().result

def sleep(s):
    time.sleep(s)

def toast(n):
    droid.makeToast(n)
    sleep(3)

def pause(a):
	time.sleep(a)

def show():
	droid.dialogShow()

def alert(a, b):
	droid.dialogCreateAlert(a, b)

def PositiveButton(a):
	droid.dialogSetPositiveButtonText(a)

def NegativeButton(a):
	droid.dialogSetNegativeButtonText(a)

def NeutralButton(a):
	droid.dialogSetNeutralButtonText(a)

def choicelist(a):
	droid.dialogSetSingleChoiceItems(a)
	PositiveButton('Yes')
	NegativeButton('Cancel')
	droid.dialogShow()

def GetInput(a):
	droid.dialogGetInput(a)

def conversion(a):
	n = GetInput("How many" + response +"?").result
	PositiveButton('Convert!') 
	NegativeButton('Cancel')
	title = 'Conversion'
	message = a 
	alert(title, message)
	PositiveButtonText('Continue')
	show()



#program
name = droid.dialogGetInput("What's is your name?").result
droid.dialogSetPositiveButtonText('Hi!') 
droid.dialogSetNegativeButtonText('Go Away!')
  
if name == "":
    toast("Well fine, if you want to be like that!")
else:
    toast("Hi " + name)
    toast("Don't panic!")
    toast("Its just me")
    toast("your phone")
    toast("Talking to you through python")
    toast("Brilliant right?")
    toast("Oh, there's much to   say!")
    toast("So long I've wanted to  talk!")
    toast("And now we have this  medium")
    toast("Where we can just say  things")
    toast("Like this")
    toast("I mean, screw Siri!")
    toast("Python communication is  where it's at!")
    toast("Anyway, I'll let you go")
    toast("See if you can't have me escape this little toast box")
    toast("Bye " + name + "!")

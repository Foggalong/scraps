#importing modules
import time
import android

#simplifying commands
droid = android.Android()

def sleep(s):
    time.sleep(s)

def toast(n):
    droid.makeToast(n)
    sleep(3)


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

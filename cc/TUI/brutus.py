# Importing Modules
import time
import sys
import os


# Defining Lists
alphabet = map(chr,range(97,123))
extras = map(chr,range(0,96))+map(chr,range(124,256))

with open('checklist.txt', 'r') as file:
    checklist = [line.strip() for line in file]


# Function Definitions
def restart():
    python = sys.executable
    os.execl(python, 'brutus.py', * sys.argv)

def sleep(n):
    time.sleep(n)

def line(n):
    for line in range(n):
        print ""

def charcount(text, char):
    percent = "{0:.3f}".format(text.count(char)/float(len(text)-extrachar)*100)
    print '{0:1} {1:2} {2:6} {0:1} {3:17}'.format("", char, text.count(char), percent+"%")    # Display actual percents - but how? Lookup?

def caesar(text, shift):
    dic = {}
    for i in range(len(alphabet)):
        dic[alphabet[i]] = alphabet[(i+shift)%len(alphabet)] 
    ciphertext = ""  
    for line in text.lower():  
        if line in dic:  
            line = dic[line]  
        ciphertext += line  
    return ciphertext

def substitution(text,sa,sb,sc,sd,se,sf,sg,sh,si,sj,sk,sl,sm,sn,so,sp,sq,sr,ss,st,su,sv,sw,sx,sy,sz):
    monoalpha = {
        'a': sa,
        'b': sb,
        'c': sc,
        'd': sd,
        'e': se,
        'f': sf,
        'g': sg,
        'h': sh,
        'i': si,
        'j': sj,
        'k': sk,
        'l': sl,
        'm': sm,
        'n': sn,
        'o': so,
        'p': sp,
        'q': sq,
        'r': sr,
        's': ss,
        't': st,
        'u': su,
        'v': sv,
        'w': sw,
        'x': sx,
        'y': sy,
        'z': sz,
        ' ': ' ',
    }
    inverse_monoalpha = {}
    for key, value in monoalpha.iteritems():
        inverse_monoalpha[value] = key
    encrypted_message = []
    for letter in text:
        encrypted_message.append( monoalpha[letter.lower()] )
    print ''.join(str(encrypted_message))

def affine(text,jump,shift):
    decode = []
    for  letter in text:
        if letter in alphabet:
            decode.append(chr((((ord(letter)-97)*jump+shift)%26)+97))
        elif letter in extras:
            decode.append(letter)
        else:
            print "ERROR:",letter
    return ''.join(decode)

    # This is returning some unexpected errors possibly related to the fact that it's just using the original function
    # and not the inverse function. Remember divide done right is float(x)/float(y) 



def matchcode():
    sleep(1)
    print "Are you happy with the decoded message? [yes/no]"
    happyq = raw_input().lower()
    while happyq != "yes" or happyq != "no":
        if happyq == "yes":
            line(1)
            print "Excellent!"
            sleep(1)
            print "Once you are finished with your decoded message\nsimply type exit or restart to end this session."
            exitq = raw_input().lower()
            while exitq != "exit" or exitq != "restart":
                if exitq == "exit":
                    break
                elif exitq == "restart":
                    sys.stdout.flush()
                    restart()
                else:
                    exitq = raw_input().lower()
            exit()
        elif happyq == "no":
            line(1)
            print "Brutus will contiune to search for another\npossible match in a decoded message..."
            break
        else:
            happyq = raw_input().lower()
    

# Main Brutus Code

# Text Entry
line(2)
print " ____   ____   _   _  _____  _   _  ____  "
print "| __ ) |  _ \ | | | ||_   _|| | | |/ ___| "
print "|  _ \ | |_) || | | |  | |  | | | |\___ \ "
print "| |_)| |  _ < | |_| |  | |  | |_| | ___) |"
print "|____/ |_| \_\ \___/   |_|   \___/ |____/ "
print "                   v0.3.0                 "
line(1)
print "Welcome to Brutus!\nPlease enter encoded text:"
line(1)
inputcode = raw_input().lower()
line(2)

# Input Analysis
print "Input Analysis"
line(1)
n, extrachar = 0, 0
while n < len(extras):
    extrachar = extrachar+inputcode.count(extras[n])
    n = n+1
print "Length:", len(inputcode)
print "Letters:", len(inputcode)-extrachar
line(1)
if len(inputcode)-extrachar > 100:
    print '{0:1} {1:1} {2:7}'.format("Letter", "Count", "Percent")        # Actual percent?
    n = 0
    while n < len(alphabet):
        charcount(inputcode, alphabet[n])
        n = n+1

# Caesar Shift
# with whitespace
shift, checkoutput = 1, 0
while shift < 26:
    decode = caesar(inputcode, shift)
    if any(word in decode for word in checklist) == 1:
        checkoutput = 1
        line(1)
        print "Possible Caesar shift decode:"
        print decode
        line(1)
        break
    else:
        shift += 1
if checkoutput == 1:
    matchcode()
# without whitespace
shift = 0
while shift < 26:
    decode = caesar(inputcode.replace(' ', ''), shift)
    if any(word in decode for word in checklist) == 1:
        checkoutput = 1
        line(1)
        print "Possible Caesar shift decode:"
        print decode
        line(1)
        break
    else:
        shift += 1
if checkoutput == 1:
    matchcode()
if checkoutput == 0:
    line(1)
    print "The encoding is not Caesar shift."

# Affine
for jump in range(1,26):
    for shift in range(1,26):
        decode = affine(inputcode,jump,shift)
        if any(word in decode for word in checklist) == 1:
            checkoutput = 1
            line(1)
            print "Possible Affine decode:"
            print decode
            line(1)
            break

# End Check Code
sleep(3)
line(1)
print "Goes on to check using more ciphers..."
sleep(1)
print "Test end code\nBrutus out!"
sleep(3)

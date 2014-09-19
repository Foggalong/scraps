#################################
# Generic Brainfuck Interpreter #
#    Alex Rosslyn  10/2/2011    #
#################################
#
#Brainfuck:
#Array size: 100 spaces (99)
#Commands
# + increases current cell
# - decreasess current
# > next
# < previous
# . output
# , input
# [ loop begin
# ] loop end
# ! quit

tape = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
position = 0
openbracketAppear = 0
closebracketAppear = 0

def panic():
        exit()

def outputdata():
        print "#:", position, " ", tape[position], " \n"

def readindata():
        tape[position] = raw_input("@")

def eval():
        global tape
        global position
        global openbracketAppear
        global closebracketAppear
        userposition = 0
        print tape
        userin = raw_input(">>>")
        while userposition < len(userin):
                if userin[userposition] == "+":
                        tape[position] += 1
                elif userin[userposition] == "-":
                        if tape[position] > 0:
                                tape[position] -= 1
                        else:
                                tape[position] == 0
                elif userin[userposition] == ">":
                        position += 1
                elif userin[userposition] == "<":
                        position -= 1
                elif userin[userposition] == ".":
                        outputdata()
                elif userin[userposition] == ",":
                        readindata()
                #Mind you, this command is not part of the actual brainfuck specification. Consider it a universal 'fuck it' button
                elif userin[userposition] == "!":
                        panic()
                elif userin[userposition] == "[":
                        openbracketAppear += 1
                elif userin[userposition] == "]":
                        closebracketAppear +=1
                        if tape[position] != 0:
                                countdown = 0
                                while countdown < closebracketAppear:
                                        userposition -= 1
                                        if userin[userposition] == "[":
                                                countdown += 1
                                        if countdown == closebracketAppear:
                                                break
                                closebracketAppear = 0
                        if tape[position] == 0:
                                if userposition < len(userin):
                                        userposition += 1
                                else:
                                        print "\nEVALUATION TERMINATED.\n"
                else:
                        print "\nINVALID.\n"
                userposition += 1
        if userposition == len(userin):
                print "\nEVALUATION TERMINATED.\n"
        openbracketAppear = 0
        closebracketAppear = 0
        loopbackAppear = 0
        userin = ''
        userposition = 0
        countdown = 0
        eval()
        
eval()

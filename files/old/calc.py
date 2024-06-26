#! /usr/bin/env python

# a tiny/simple Tkinter calculator (improved v.1.1)
# if you enter a number with a leading zero it will be an octal number!
# eg. 012 would be a decimal 10 (0.12 will not be affected)
# used a more modern import to give Tkinter items a namespace
# tested with Python24 vegaseat 08dec2006

"""Subject to quick developing change"""
"""calculator has a layout like this ...
< display >
7 8 9 * C
4 5 6 / M->
1 2 3 - ->M
0 . = + neg
"""

import time
import Tkinter as tk

def pause(n):
	time.sleep(n)

def click(key):
	global memory
	if key == '=':
		# avoid division by integer
		if '/' in entry.get() and '.' not in entry.get():
			entry.insert(tk.END, ".0")
		# guard against the bad guys abusing eval()
		str1 = "-+0123456789."
		if entry.get()[0] not in str1:
			entry.insert(tk.END, "Non number input!")
		# here comes the calculation part
		try:
			result = eval(entry.get())
			entry.insert(tk.END, " = " + str(result))
		except:
			entry.delete(0, tk.END) # clear entry
			entry.insert(tk.END, "Error!")
	elif key == 'C':
		entry.delete(0, tk.END) # clear entry
	elif key == '->M':
		memory = entry.get()
		# extract the result
		if '=' in memory:
			ix = memory.find('=')
			memory = memory[ix+2:]
		root.title('M=' + memory)
	elif key == 'M->':
		entry.insert(tk.END, memory)
	elif key == 'neg':
		if '=' in entry.get():
			entry.delete(0, tk.END)
		try:
			if entry.get()[0] == '-':
				entry.delete(0)
			else:
				entry.insert(0, '-')
		except IndexError:
			pass
	else:
		# previous calculation has been done, clear entry
		if '=' in entry.get():
			entry.delete(0, tk.END)
		entry.insert(tk.END, key),

root = tk.Tk()
root.title("Simple Calculator")

btn_list = [
'7', '8', '9', '*', '(', 'C',
'4', '5', '6', '/', ')', 'M->',
'1', '2', '3', '-', 'j', '->M',
'0', '.', '=', '+', '**', 'neg' ]

# create all buttons with a loop
r = 1
c = 0
for b in btn_list:
	rel = 'ridge'
	cmd = lambda x=b: click(x)
	tk.Button(root,text=b,width=1,relief=rel,command=cmd).grid(row=r,column=c)
	c += 1
	if c > 5:
		c = 0
		r += 1

# use Entry widget for an editable display
entry = tk.Entry(root, width=25, bg="gray")
entry.grid(row=0, column=0, columnspan=6)

root.mainloop()

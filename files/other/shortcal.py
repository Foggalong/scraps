#!/usr/bin/env python

# an even more basic calculator than included in calc.py

import Tkinter as tk
def click(key):
	global memory
	global answer
	if key == '=':
		if '/' in entry.get() and '.' not in entry.get():
			entry.insert(tk.END, ".0")
		try:
			entry.insert(tk.END, " = " + str(eval(entry.get())))
			answer = entry.get()
			if '=' in answer:
				answer = answer[answer.find('=')+2:]
		except:
			entry.delete(0, tk.END)
			entry.insert(tk.END, "= Error!")
	elif key == 'AC':
		entry.delete(0, tk.END)
	elif key == 'ANS':
		entry.insert(tk.END, answer)
	elif key == '->M':
		memory = entry.get()
		if '=' in memory:
			memory = memory[memory.find('=')+2:]
	elif key == 'M->':
		entry.insert(tk.END, memory)
	elif key == 'CLR':
		answer, memory = '', ''
		entry.delete(0, tk.END)
		entry.insert(tk.END, "= Memory Cleared!")
	else:
		if '=' in entry.get():
			entry.delete(0, tk.END)
		entry.insert(tk.END, key),
root = tk.Tk()
btn_list = ['(', ')', '->M', 'M->', 'CLR', '7', '8', '9', '**', 'AC', '4', '5', '6', '*', '/', '1', '2', '3', '+', '-', '0', '.', 'j', '=', 'ANS' ]
r, c = 1, 0
for b in btn_list:
	tk.Button(root, text=b, width=1, relief='ridge', command=lambda x=b: click(x)).grid(row=r, column=c)
	c += 1
	if c > 4:
		c = 0
		r += 1
entry = tk.Entry(root, width=20, bg="gray")
entry.grid(row=0, column=0, columnspan=5)
root.mainloop()

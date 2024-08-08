with open('checklist.txt', 'r') as file:
		checklist = [line.strip() for line in file]

with open('4list.txt', 'r') as file:
		wordlist = [line.strip() for line in file]

def hill(text,word):
	lst = []
	otpt = []
	key = []
	
	for char in word:
		key.append(ord(char)-97)
		
	for letter in text:
		lst.append(str(ord(letter)-97))
		
	n = 0
	while n < len(text):
		det = float(key[0]*key[3]-key[1]*key[2])
		indet = 1
		for w in range(1,26):
			if w*det % 26 == 1:
				indet = w
				
		x = int(lst[n])
		y = int(lst[n+1])
		a = (key[3] % 26)*indet % 26
		b = (-key[1] % 26)*indet % 26
		c = (-key[2] % 26)*indet % 26
		d = (key[0] % 26)*indet % 26
		otpt.append(chr(((a*x+b*y) % 26)+97))
		otpt.append(chr(((c*x+d*y) % 26)+97))
		n+=2
		
	return ''.join(otpt)


text = input("Text: ").lower().replace(' ','')
for word in wordlist:
	print(word)
	decode = hill(text,word)
	count = 0
	for x in range(0,len(checklist)):
		if checklist[x] in decode:
			count+=1
	if count >= 3:
		print(decode)
		check = 0
		while check == 0:
			q = input("Happy? ").lower()
			if q == 'yes':
				exit()
			elif q == 'no':
				break
			else:
				pass

end = input("\nThe program has exhausted the list of key words\nand no matches have been found. Would you like\nto launch the manual hill decoder (manual) or\ntry complete exhaustion (complete)?\n")
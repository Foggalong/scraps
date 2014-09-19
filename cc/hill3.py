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
		det = float(key[0]*(key[4]*key[8]-key[5]*key[7])-key[1]*(key[8]*key[3]-key[5]*key[6])+key[2]*(key[3]*key[7]-key[4]*key[6]))
		indet = 1
		for w in range(1,26):
			if w*det % 26 == 1:
				indet = w

		x = int(lst[n])
		y = int(lst[n+1])
		z = int(lst[n+2])
		a = (key[4]*key[8]-key[5]*key[7] % 26)*indet % 26
		b = (key[2]*key[7]-key[1]*key[8] % 26)*indet % 26
		c = (key[1]*key[5]-key[2]*key[4] % 26)*indet % 26
		d = (key[5]*key[6]-key[3]*key[8] % 26)*indet % 26
		e = (key[0]*key[8]-key[2]*key[6] % 26)*indet % 26
		f = (key[2]*key[3]-key[0]*key[5] % 26)*indet % 26
		g = (key[3]*key[7]-key[4]*key[6] % 26)*indet % 26
		h = (key[6]*key[1]-key[0]*key[7] % 26)*indet % 26
		i = (key[0]*key[4]-key[1]*key[3] % 26)*indet % 26
		otpt.append(chr(((a*x+b*y+c*z)%26)+97))
		otpt.append(chr(((d*x+e*y+f*z)%26)+97))
		otpt.append(chr(((g*x+h*y+i*z)%26)+97))
		n+=3

	return ''.join(otpt)

text = input("Text: ").lower().replace(' ', '')
word = list(input("Key: ").lower())
print(hill(text,word))

#it's probably fabulists
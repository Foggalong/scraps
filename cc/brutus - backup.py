alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
with open('checklist.txt','r') as file:
	checklist=[line.strip() for line in file]
def caesar(p,s):
	dic,ciphertext={},""
	for i in range(len(alphabet)):
		dic[alphabet[i]]=alphabet[(i+s)%len(alphabet)]  
	for l in p.lower():  
		if l in dic:  
			l=dic[l]  
		ciphertext+=l  
	return ciphertext	
while alphabet != 0:
	print "Message:";inputcode=raw_input().lower();s,checkoutput=1,0
	while s < 26:
		decode=caesar(inputcode,s)
		if any(word in decode for word in checklist)==1:
			checkoutput=1;print "\nPossible Decode:\n",decode,"\n\n\n";break
		else:
			s+=1
	if checkoutput==0:
		print "\nERROR 404:\nDECODE NOT FOUND\n\n\n"

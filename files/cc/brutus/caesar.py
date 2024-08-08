#!/usr/bin/python
# A test of grammar retaining with Caesar shift

alphabet = map(chr, range(97, 123))

def caesar(text, shift):
	lista = list(text)
	listb = []
	for x in range(0, len(text)):
		if lista[x] in alphabet:
			listb.append(chr((((ord(lista[x])-97)+shift)%26)+97))
		else:
			listb.append(lista[x])
	return ''.join(listb)

text = raw_input('Text: ').lower().strip()
shift = int(raw_input('Shift: '))
print caesar(text, shift)
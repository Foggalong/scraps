#!/usr/bin/python
o,b,u=0,int(raw_input("L:")),int(raw_input("U:"))
def AD(l):
 t=0
 for n in l:
  t+=int(n)
 return t
for n in range(b,u+1):
 o,l=0,list(str(n))
 while int(o)<int(n):
  l.append(AD(l));l.pop(0);o=l[len(str(n))-1]
  if int(o)==int(n):
   print n
n=raw_input().lower();s,o=1,0
for s in range(1,26):
 a,d,t=map(chr,range(97,123)),{},""
 for i in range(len(a)):
  d[a[i]]=a[(i+s)%len(a)]
 for l in n:
  if l in d:
   l=d[l]
  t+=l
 print t

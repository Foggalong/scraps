n=9
while n>8:
 n+=1;l=[int(d)for d in str(n)]
 while sum(l)<n:l.append(sum(l));l.pop(0);print(n) if sum(l)==n else''
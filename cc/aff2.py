def affine(a, b):
    for i in range(26):
        print(chr(i+65) + ": " + chr(((a*i+b)%26)+65))

#Complete List
count = 0
for a in range(1,26):
    for b in range(0,26):
        count+=1
        print("Affine",str(count)+":",str(a)+","+str(b))
        affine(1, b)
        print("")

print("Finished")
end = 0
while end != 'exit':
    end = input("Press Ctrl+C to quit") 

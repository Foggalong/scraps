# in sixth form I got obsessed with the generalisation of the
# formula for inverting a matrix, computing them by hand all the
# way up to five-by-five. here's one I wrote for three by three
# matrices while learning Python.

inpt = input("Matrix: ").split()
mat = []
for char in inpt:
    mat.append(int(char))

det = mat[0]*(mat[4]*mat[8]-mat[5]*mat[7])-mat[1]*(mat[8]*mat[3]-mat[5]*mat[6])+mat[2]*(mat[3]*mat[7]-mat[4]*mat[6])
a = mat[4]*mat[8]-mat[5]*mat[7]
b = mat[2]*mat[7]-mat[1]*mat[8]
c = mat[1]*mat[5]-mat[2]*mat[4]
d = mat[5]*mat[6]-mat[3]*mat[8]
e = mat[0]*mat[8]-mat[2]*mat[6]
f = mat[2]*mat[3]-mat[0]*mat[5]
g = mat[3]*mat[7]-mat[4]*mat[6]
h = mat[6]*mat[1]-mat[0]*mat[7]
i = mat[0]*mat[4]-mat[1]*mat[3]

print("\n",det)
print(a,b,c)
print(d,e,f)
print(g,h,i)
print()

#chr(((a*1+b)%26)+65),chr(((a*2+b)%26)+65),chr(((a*3+b)%26)+65),chr(((a*4+b)%26)+65),chr(((a*5+b)%26)+65),chr(((a*6+b)%26)+65),chr(((a*7+b)%26)+65),chr(((a*8+b)%26)+65),chr(((a*9+b)%26)+65),chr(((a*10+b)%26)+65),chr(((a*11+b)%26)+65),chr(((a*12+b)%26)+65),chr(((a*13+b)%26)+65),chr(((a*14+b)%26)+65),chr(((a*15+b)%26)+65),chr(((a*16+b)%26)+65),chr(((a*17+b)%26)+65),chr(((a*18+b)%26)+65),chr(((a*19+b)%26)+65),chr(((a*20+b)%26)+65),chr(((a*21+b)%26)+65),chr(((a*22+b)%26)+65),chr(((a*23+b)%26)+65),chr(((a*24+b)%26)+65),chr(((a*25+b)%26)+65))

import time

def substitution(text,a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,n1,o1,p1,q1,r1,s1,t1,u1,v1,w1,x1,y1,z1):
    monoalpha = {
        'a': a1,
        'b': b1,
        'c': c1,
        'd': d1,
        'e': e1,
        'f': f1,
        'g': g1,
        'h': h1,
        'i': i1,
        'j': j1,
        'k': k1,
        'l': l1,
        'm': m1,
        'n': n1,
        'o': o1,
        'p': p1,
        'q': q1,
        'r': r1,
        's': s1,
        't': t1,
        'u': u1,
        'v': v1,
        'w': w1,
        'x': x1,
        'y': y1,
        'z': z1,
        ' ': ' ',
    }
    inverse_monoalpha = {}
    for key, value in monoalpha.iteritems():
        inverse_monoalpha[value] = key
    encrypted_message = []
    for letter in text:
        encrypted_message.append( monoalpha[letter.lower()] )
    print ''.join( str(encrypted_message)) )  

def affine(text,jump,shift):
    def f(n):
        chr(((jump*n+shift)%26)+65)
    a,b,c,d,e,f2,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25
    substitution(text,f(a),f(b),f(c),f(d),f(e),f(f2),f(g),f(h),f(i),f(j),f(k),f(l),f(m),f(n),f(o),f(p),f(q),f(r),f(s),f(t),f(u),f(v),f(w),f(x),f(y),f(z))

text = raw_input("Text:").lower()
jump = int(raw_input("Jump:"))
shift = int(raw_input("Shift:"))
affine(text,jump,shift)
time.sleep(10)

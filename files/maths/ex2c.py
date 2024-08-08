import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

for x in range(2, 100):
    if is_prime(x) and (x % 4 == 1):
        print(x, x*x)

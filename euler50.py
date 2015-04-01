# What is the longest sequence of primes that add to a prime below 1,000,000.
import math

N = 1000000
primes = list(range(2, N))

# sieve
i = 0
cutoff = int(math.ceil(math.sqrt(N)))
while True:
    p = primes[i]
    if p > cutoff:
        break
    primes = [n for n in primes if n == p or n%p != 0]
    i += 1

#print(primes)

def gen():
    for i in range(len(primes)):
        t = 0
        for j in range(i+1, len(primes)):
            if t >= N:
                break 
            if t in primes:
                yield j-i, t, primes[i:j]
            t += primes[j]
print(max(gen()))
                

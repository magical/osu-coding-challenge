# Find the sub of all even numbers in the fibonacci sequence below 4,000,000

a, b = 1, 1
t = 0
while b < 4000000:
    if b&1 == 0:
        t += b
    a, b = b, a+b
print(t)
# 4613732

# find the largest palindromic number made from the product of two 3-digit numbers

numbers = list(range(100, 1000))

def gen():
    for x in range(100, 1000):
        for y in range(100, x):
            n = str(x*y)
            if n == "".join(reversed(n)):
                yield n, x, y

print(max(gen()))
# 99999

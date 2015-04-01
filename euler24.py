import itertools
#it = itertools.permutations("012", 3)
it = itertools.permutations("0123456789", 10)
for i, p in enumerate(it):
    if i == 999999:
        print("".join(p))
        break
# 2783915460

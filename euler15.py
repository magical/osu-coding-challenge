import functools

@functools.lru_cache(maxsize=None)
def paths(x, y):
    if x < 0 or y < 0:
        return 0
    if y < x:
        return paths(y, x)
    if x == 0 and y == 0:
        return 1# 0?
    return paths(x-1, y) + paths(x, y-1)
        
#print(paths(6, 6))
print(paths(20, 20))
# 137846528820

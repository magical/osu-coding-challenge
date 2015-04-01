import sys
import re
vowels = "AEIOUaeiou"
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
for line in sys.stdin:
    out = []
    for word in re.split(r'([A-Za-z]*)', line):
        cap = False
        if word and word[0].isupper() and (len(word) == 1 or word[1:].islower):
            word = word[0].lower() + word[1:]
            cap = True
        if word and word[0] in vowels:
            word = word + "way"
        elif word and word[0] in alpha:
            word = word[1:] + word[0] + "ay"
        if cap:
            word = word[0].upper() + word[1:]
        out.append(word)
    print("".join(out), end="")

#!/usr/bin/python3
import random

# print 2 sets of lottery 539
print()
for a in range(2):

    lottery = []
    # make lottery[] contains 5 random number
    while len(lottery) < 5:
        n = random.randint(1,39)
        lottery.append(n)
        if lottery.count(n) > 1:
            lottery.pop()       # remove duplicated

    # sort and print
    lottery.sort()
    print('   ', lottery)

print()     # one more space line

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import PyQt6
import random

def mod_exp(x, y, n):
    x = int(x)
    y = int(y)
    n = int(n)

    if y == 0:
        return 1
    z = mod_exp(x, y/2, n)
    if y % 2 == 0:
        return (z**2) % n
    else:
        return (x * z**2) % n

def miller_rabin(N, k=1):
    for i in range(0, k):
        nMin1 = N-1
        expIsEven = True
        rand = random.randint(1, nMin1)

        while expIsEven:
            p1 = mod_exp(rand, nMin1, N)
            ans = p1 % N
            if ans == -1%N:
                break
            elif ans % N != 1%N:
                return 'composite'

            if (nMin1 % 2) == 0:
                nMin1 = nMin1 / 2
            else:
                expIsEven = False

    return 'prime'

print(mod_exp(41, 3, 391))

#print("MR Primality: " + miller_rabin(97,1))



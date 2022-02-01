import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


#Time complexity - O(n^3), as n recursive calls each entail at least one division or multiplication operation (O[n^2]),
#for O(n * n^2) total complexity
#Space complexity - O(n^2), as each call of n recursive calls allocates another n-bit amount of memory
def mod_exp(x, y, N):
    #Ensure that all inputs are integers
    x = int(x)
    y = int(y)
    N = int(N)

    #Base case: stop recursing once y is equal to 0
    if y == 0:
        return 1
    #Recursively call mod_exp(), integer-dividing y in half each time, until y is equal to 0
    z = mod_exp(x, y / 2, N)                    #O(n^2) time
    #If y is even, return z squared modulo N
    if y % 2 == 0:
        return (z ** 2) % N                     #O(n^2) time
    #If y is odd, return x times z squared, quantity modulo N
    else:
        return (x * z ** 2) % N                 #O(n^2) time


#Time complexity - O(n), with respect to the number of bits of k, as 2 is multiplied n times
#Space complexity - O(n), as a bit is added to the stored return value with each step of 2^-n
def fprobability(k):
    return 1-(2 ** -k)


#Time complexity - O(n) with respect to the number of bits n of k, as 4 is multiplied n times
#Space complexity - O(n), as a bit is added to the stored return value with each step of 4^-n
def mprobability(k):
    return 1-(4 ** -k)


#Time complexity - O(n^3), randint() takes constant time, mod_exp() completes in O(n^3) time, and the two
#together happen k times. This function completes in O(k*n^3), which is big_theta(n^3).
#Space complexity - O(n^2), as mod_exp() has O(n^2) space complexity, repeated k times, for O(k * n^2), big_theta(n)
def fermat(N, k=3):
    #Conduct Fermat's test k times to increase the probability of a correct primality determination
    for i in range(0, k):                       #O(k) time
        #Select a random integer (rand) between 1 and N-1 inclusive, and conduct modular exponentiation to
        #find the solution to (rand^(N-1))%N. If the solution is not equavalent to 1%N, return "composite."
        #Otherwise, return "prime."
        rand = random.randint(1, N-1)           #O(1) time
        if mod_exp(rand, N-1, N) != (1 % N):    #O(n^3) time
            return 'composite'
    #Return "prime" if no trials returned "composite" upon evaluation
    return 'prime'


#Time complexity - O(n^4), as randint() takes constant time, mod_exp() completes in O(n^3) time, and random.randint()
#along with mod_exp() happen together k times. This function completes in O(k*n^3), which is big_theta(n^3).
#Space complexity - O(n^3), as mod_exp() has n^2 space complexity, repeated n times for k trials (k * n^3)
def miller_rabin(N, k=3):
    #Repeat the Miller-Rabin test k times
    for i in range(0, k):                       #O(k) time
        nMin1 = N-1
        expIsEven = True
        #Create a random number rand between 1 and N exclusive in order to plug into (rand^N-1) % N
        rand = random.randint(1, nMin1)         #O(1) time

        #Conduct modular exponentiation on y, halving it each time, until it cannot be halved anymore
        while expIsEven:                        #O(n) time
            p1 = mod_exp(rand, nMin1, N)      #O(n^3) time
            ans = p1 % N
            #End the while loop if mod_exp() returned -1
            if ans == -1%N:
                break
            #Return "composite" if the previous mod_exp() solution was not -1 and the current mod_exp solution is
            #not equal to 1
            elif ans % N != 1%N:
                return 'composite'
            if (nMin1 % 2) == 0:
                nMin1 = nMin1 / 2               #O(n^2) time
            else:
                expIsEven = False
    #Return prime if all trials do not return "composite" upon evaluation
    return 'prime'

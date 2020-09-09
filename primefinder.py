import timeit
import math

def getGCD(n1, n2):
    while (n1 != 0 and n2 != 0):
        if (n1 >= n2):
            n1 %= n2
        else:
            n2 %= n1
    return max(n1, n2)

def isCoprime(n1, n2):
    return (getGCD(n1, n2) == 1)

def validatePrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    for x in range(2, math.ceil(math.sqrt(n))+1):
        if (n % x == 0):
            return False
    return True

print("How many primes should we find?")
primesToFind = int(input())

print("What should the base be for the coprime method?")
base = int(input())

print("Starting coprime method")

start = timeit.default_timer()

coprimes = []
totalPrimes = 0
for x in range(1, base):
    if (isCoprime(x, base)):
        coprimes.append(x)
    if (validatePrime(x)):
        totalPrimes += 1

currentVicinity = base
while (True):
    shouldQuit = False
    for x in coprimes:
        if (validatePrime(currentVicinity+x)):
            totalPrimes += 1
            if (totalPrimes == primesToFind):
                shouldQuit = True
                break
    if (shouldQuit):
        break
    currentVicinity += base

stop = timeit.default_timer()

print("Time: ", stop - start)
print("Total primes: ", totalPrimes)

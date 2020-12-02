import timeit
import math

def get_gcd(n1, n2):
    while (n1 != 0 and n2 != 0):
        if (n1 >= n2):
            n1 %= n2
        else:
            n2 %= n1
    return max(n1, n2)

def is_comprime(n1, n2):
    return (get_gcd(n1, n2) == 1)

def validate_prime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    for x in range(2, math.ceil(math.sqrt(n))+1):
        if (n % x == 0):
            return False
    return True

print("How many primes should we find?")
primes_to_find = int(input())

print("What should the base be for the coprime method?")
base = int(input())

print("Starting coprime method")

start = timeit.default_timer()

coprimes = []
total_primes = 0
for x in range(1, base):
    if (is_comprime(x, base)):
        coprimes.append(x)
        if (validate_prime(x)):
            total_primes += 1

current_vicinity = base
while total_primes < primes_to_find:
    for x in coprimes:
        if (validate_prime(current_vicinity+x)):
            total_primes += 1
    current_vicinity += base

stop = timeit.default_timer()

print("Time: ", stop - start)
print("Total primes: ", total_primes)

print("\nStarting sieve of eratosthenes")
start = timeit.default_timer()
primes_found = []
iterator = 1
while len(primes_found) < primes_to_find:
    iterator += 1
    is_prime = True
    for prime in primes_found:
        if iterator % prime == 0:
            is_prime = False
            break
    if not is_prime:
        continue
    primes_found.append(iterator)
stop = timeit.default_timer()

print("Time: ", stop - start)
print("Total primes: ", len(primes_found))

print("\nStarting combined method")
start = timeit.default_timer()

primes_found = []
coprimes = []
for x in range(1, base):
    if (is_comprime(x, base)):
        coprimes.append(x)
        if (validate_prime(x)):
            primes_found.append(x)

current_vicinity = base
while len(primes_found) < primes_to_find:
    for x in coprimes:
        check = current_vicinity + x
        is_prime = True
        for prime in primes_found:
            if check % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes_found.append(check)
    current_vicinity += base

stop = timeit.default_timer()

print("Time: ", stop - start)
print("Total primes: ", len(primes_found))

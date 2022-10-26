"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math

def isPrime(n):
    n = abs(int(n))
    if n == 2: return True
    if n % 2 == 0: return False
    r = math.sqrt(n)
    x = 3
    while x <= r:
        if n % x == 0: return False  # A factor was found, so number is not prime
        x += 2 # Increment to the next odd number
    return True

counter =0
i=2
while (counter < 10001):
    if isPrime(i):
        counter+=1
        print("the count is ",counter,i)
        if (counter == 10001):
            print("the 10 001st prime number is", i)
    i+=1

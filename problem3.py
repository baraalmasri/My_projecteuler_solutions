"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
def PrimeFactors(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        while n%i==0:#find all the occurrences of a prime factor
            print((int)(i)),
            n=n/i
    if n!=1:#if the number was originally a prime
        print((int)(n))


n=600851475143
PrimeFactors(n)
"""
outPut:
71
839
1471
6857
"""

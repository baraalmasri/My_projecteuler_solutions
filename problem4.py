"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


largest = 0
for i in range (999,100-1,-1):
    for j in range (i,100-1,-1):
        product=i*j
        if largest> product:
            break

        temp = product
        rev = 0
        while (temp != 0):
            rev = rev * 10 + temp % 10
            temp = temp // 10

        if (product == rev and product> largest):
            largest = product




print(largest) #906609





def eratosthenes2(n):
    #Declare a set - an unordered collection of unique elements
    multiples = set()

    #Iterate through [2,2000000]
    for i in range(2, n+1):

        #If i has not been eliminated already
        if i not in multiples:

            #Yay prime!
            yield i

            #Add multiples of the prime in the range to the 'invalid' set
            multiples.update(range(i*i, n+1, i))

#Now sum it up
iter = 0
ml = list(eratosthenes2(2000000))
for x in ml:
    iter = int(x) + iter

print(iter)

# def testyield():
#   yield "Welcome to Guru99 Python Tutorials"
#
# output = testyield()
#
# for i in output :
#
#     print(i)

# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

num = 600851475143
i = 1

while(i <= num):
    count = 0
    if(num % i == 0):
        j = 1
        while(j <= i):
            if(i % j == 0):
                count = count + 1
            j = j + 1
        if (count == 2):
            print(" %d is a Prime Factor of a Given Number %d" %(i, num))
            print (i)
    i = i + 1

print ('Este es el largest prime number: ', i)

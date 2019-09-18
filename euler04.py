# Largest palindrome product
#
# 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

# Python Program to Reverse a Number using While loop


record = 0
for i in range(100,1000):
   for j in range(100,1000):
      num = i * j
      numero = num
      reverse = 0
      while(num > 0):
         reminder = num %10
         reverse = (reverse *10) + reminder
         num = num //10
      if numero == reverse and numero > record:
         record = reverse
         print ('Record parcial: ', record)
     


print ('El record es: ', record)
            





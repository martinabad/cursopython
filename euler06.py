# Sum square difference
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum1 = 0
sum2 = 0

for i in range(1,101):
   sum1 = sum1 + i**2

for i in range(1,101):
   sum2 = sum2 + i

sum2 = sum2**2
print('La suma del cuadrado de los numeros es: ',sum1)
print('La suma de los numeros al cuadrado es: ',sum2)
print('La diferencia de las sumas es: ',sum2 - sum1)




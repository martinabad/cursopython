fin = int(input('Cuantos numeros buscamos? '))
num1 = 1
num2 = 1
a = 0

while a < fin:
   print(num1, end=' ')
   num3 = num1 + num2
   num1 = num2
   num2 = num3
   a = a + 1
print ()


num = input('Ingrese un numero: ')
dig = len(num) -1

num2 = (num[dig::-1])

if num == num2:
   print (num, " es igual a ", num2, "ES CAPICUA")
else:
   print (num, "es distinto a ", num2, "NO ES CAPICUA ")

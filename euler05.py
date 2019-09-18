# Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

smal = 0
flag = 0 
num = 20

while True:
#   print ('entro al while el numero ', num)
   if num %20 == 0:
      if num %19 == 0:
         if num %18 == 0:
            if num %17 == 0:
               if num %16 == 0:
                  if num %15 == 0:
                     if num %14 == 0:
                        if num %13 == 0:
                           if num%12 == 0:
                              if num%11 == 0:
                                 smal = num
                                 break
                              else:
                                num += 20
                           else:
                             num += 20
                        else: 
                           num += 20
                     else:
                        num += 20
                  else:
                     num += 20
               else:
                  num += 20
            else:
               num += 20
         else: 
             num += 20
      else: 
            num += 20
   else:
      num += 20

print (smal)

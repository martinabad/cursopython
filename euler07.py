# 10001st prime
#
# What is the 10 001st prime number?

end = 10000
pr = 0
x = 1


while pr <= end:
  x += 1
  for k in range (2, x//2):
     if x %k == 0:
        break
  else:
#     print (x)
     pr += 1

print (pr)
print (x)


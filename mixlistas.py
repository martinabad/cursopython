l1 = ['a','b','c','c','0','9']
l2 = ['a','1','4','caracol','0']
l3 = []

print (l1)
print (l2)
print (l3)
largo = len(l1)
largo2 = len(l2)
print(largo)

for i in range(0, largo):
   if l1[i] not in l3:
      l3.append(l1[i])

for j in range(0, len(l2)):
   if l2[j] not in l3:
      l3.append(l2[j])

print (l3)

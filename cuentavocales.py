palabra = input ('Ingrese una palabra: ')
vocales = ['a','e','i','o','u']   
vocal = 0
cont = len(palabra) -1
a = e = i = o =  u = 0

while cont >= 0:
   if palabra[cont] == vocales [4]: 
      u = u +1
      cont = cont -1
      vocal = vocal + 1
   if palabra[cont] == vocales [3]: 
      o = o + 1
      cont = cont - 1
      vocal = vocal + 1
   if palabra[cont] == vocales [2]:
      i = i + 1
      cont = cont -1
      vocal = vocal + 1
   if palabra[cont] == vocales [1]:
      e = e + 1
      cont = cont -1
      vocal = vocal + 1
   if palabra[cont] == vocales [0]:
      a = a +1
      vocal = vocal +1
      cont = cont -1
   else:
      cont = cont -1

print (palabra, ' tiene ', vocal, ' vocales')
print ('============= ')
print ('Letras A: ',a)
print ('Letras E: ',e)
print ('Letras I: ',i)
print ('Letras O: ',o)
print ('Letras U: ',u)

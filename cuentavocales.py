palabra = input ('Ingrese una palabra: ')
vocales = ['a','e','i','o','u']   
vocal = 0
cont = len(palabra) -1

while cont >= 0:
   if palabra[cont] == vocales [4] or palabra[cont] == vocales [3] or palabra[cont] == vocales [2] or palabra[cont] == vocales [1] or palabra[cont] == vocales [0]:
      vocal = vocal +1
      cont = cont -1
   else:
      cont = cont -1

print (palabra, ' tiene ', vocal, ' vocales')

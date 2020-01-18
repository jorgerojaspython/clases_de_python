  #################################################
 #             N U ME R O S   P R I M O S        #
#################################################
def isPrime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(isPrime(67))

#to print the list of numeros primos
for i in range(1, 2000):
	if isPrime(i + 1):
			print(i + 1, end=" ") # EN ELND LE DEJA UN ESPACIO Y NO NO UN ENTER
print()

#segunda forma de resolver
def isPrime (num):
  if num<2:
    return False
  for i in range(2,num):
    if num % i==0:
      return False
  return True
isPrime(7)

  #################################################
 #                   R A N G E                   #
#################################################
result=0
n=5
for i in range (1,n+1):
    result+=i
print(result)


for i in range (100,-1,-5):# decrementa de dos en dos el rango
    print(i)

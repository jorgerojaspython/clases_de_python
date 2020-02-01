try:
    x=int(input("Enter a number"))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("no puede dividir para cero")
except ValueError:
    print("debe ser un entero")
print("the end")



import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)



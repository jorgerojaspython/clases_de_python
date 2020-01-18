# usted es joven?
while True:
    x=input("Cual es su edad?:")
    if x == 'q' or x=='quit':
        break
    x=int(x)
    if x>=1 and x <=9:
        print("Usted es niño porque tiene ",x," años.")
    elif x>=10 and x<=17:
        print("Usted es joven porque tiene ",x," años.")
    else:
        print("Usted es mayor de edad porque tiene ",x," años.")
# FORMAT

pi=22/7
print(pi)
print("{:.2f}".format(pi))



###############################################
# estableciendo funciones #####################
###############################################
# FORMAT print("{:.2f}".format(pi))

def message():
    print("Enter next value")
print("we start here")
message()
print("the end is here")


def hi(name):
    print("Hi",name)
hi("george")


def hiall(name1,name2):
    print("hi ", name2)
    print("hi ", name1)
hiall("Sebas", "Jorge")


def direccion (calle,ciudad,postal):
    print("Tu direccion es: ",calle,"en la ciudad de ",ciudad, " con codigo postal ", postal)
s=input("calle: ")
c=input("ciudad: ")
pp=input("codigo postal: ")
direccion(s,c,pp)


def resta(a,b):
    print(a-b)
resta(5,2)
resta(a=2,b=5)
resta(2,b=5)


def multi(a,b):
    return a*b
print(multi(3,4))
def multi(a,b):
    return
print(multi(3,4))


def deseo():
    return "feliz cumpleaños"
w=deseo()
print(w)



def deseo():
    print("Mi deseo")
    return "feliz cumpleaños"
deseo()
print(deseo())



def holass(lista): # saluda a todos los compañeros
    for i in lista:
        print("hola,", i)
holass(["Jorge","Javier","Rojas","Aguilar"])



def crearlista(n):
    lista=[]
    for i in range(n):
        lista.append(i)
    return lista
print(crearlista(5))




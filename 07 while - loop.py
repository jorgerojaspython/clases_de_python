# while
x=input("cuantas veces desea repetir?:")
x=int(x)
y=1
while y<=x:
    print(y)
    y=y+1
    
    
# while true
x=input("cuantas veces desea repetir?:")
x=int(x)
y=1
while True:
    print(y)
    y=y+1
    if y>x:
        break
    
    
# while true dentro de while true
while True:
    x=input("cuantas veces desea repetir?:")
    if x == 'q' or x=='quit':
        break # rompe el bucle
    x=int(x)
    y=1 
    while True:
        print(y)
        y=y+1
        if y>x:
            break
# ingrese 4 datos
while True:
    x=input("cuantas veces desea repetir?:")
    if x == 'q' or x=='quit':
        break # rompe el bucle
    x=int(x)
    y=1 
    while True:
        print(y)
        y=y+1
        if y>x:
            break
    
    
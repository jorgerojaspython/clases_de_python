devices=["x1","x2","r3","r4"]
for item in devices:
    print(item)
#### comando
for item in devices:
    if "r" in devices:
            print(item)
##### permite que el resultado,
switches=[]
for item in devices:
    if "x" in item:
        switches.append(item)
print(switches)